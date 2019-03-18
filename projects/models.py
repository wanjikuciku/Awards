from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from url_or_relative_url_field.fields import URLOrRelativeURLField
from pyuploadcare.dj.models import ImageField
from tinymce.models import HTMLField


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_photos',null=True,blank=True)
    bio = HTMLField()
    contact=models.CharField(max_length=12)
    projects = models.ForeignKey('Project',on_delete=models.CASCADE,null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()

    def __str__(self):
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=40)
    description = HTMLField()
    landing_page = models.ImageField(upload_to='landing_pages')
    live_site = URLOrRelativeURLField()
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title