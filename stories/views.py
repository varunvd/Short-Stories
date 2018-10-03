from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'stories/index.html')
    return render(request, 'stories/login.html')


@login_required
def logout_done(request):
    logout(request)
    return render(request, 'stories/login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=name,
                                        email=email)
        user.set_password(password)

        try:
            user.save()
            return render(request, 'stories/login.html')
        except:
            return render(request, 'stories/register.html')
    return render(request, 'stories/register.html')
