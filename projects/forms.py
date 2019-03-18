from .models import Project,UserProfile
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core import validators

class NewProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title','description','landing_page','live_site')


class VoteForm(ModelForm):
    class Meta:
        model = Project
        fields = ('design','usability','content')


class ProfileEditForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic','bio')