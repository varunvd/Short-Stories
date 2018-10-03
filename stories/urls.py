from django.urls import path

from .import views

app_name = 'story'
urlpatterns = [
	path('', views.index, name='index'),
	path('logout', views.logout_done, name='logout'),
	path('register', views.register, name='register'),
]
