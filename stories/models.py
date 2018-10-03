from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='imgs', blank=True)
    follows = models.ManyToManyField('UserProfile', related_name='followed_by')
    # Usage tim.userprofile.follows.add(chris.userprofile)

    def __str__(self):
        return self.user.name


class Story(models.Model):
    story_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    story = models.TextField(blank=True, null=True)
    vote = models.IntegerField(default=0)
    type = models.CharField(max_length=40, null=False, default="Not Specified")
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.story_id


class Comments(models.Model):
    comments = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    story_id = models.ForeignKey(Story, on_delete=models.PROTECT)

    def __str__(self):
        return self.comments


