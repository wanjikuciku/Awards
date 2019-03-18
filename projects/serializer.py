from rest_framework import serializers
from .models import Profile,Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','bio','profile_pic','projects')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','description','landing_page','design','usability','content')