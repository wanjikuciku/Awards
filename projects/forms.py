from .models import Project,UserProfile
from django.contrib.auth.models import User
from .models import UserProfile,Project
from django.forms import ModelForm

class NewProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title','description','landing_page')


class VoteForm(ModelForm):
    class Meta:
        model = Project
        fields = ('design','usability','content')


class ProfileEditForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic','bio')