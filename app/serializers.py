from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Skill, Project, Commit, FeaturePost


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProjectMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('project_name', 'project_url',)


class CommitSerializer(serializers.ModelSerializer):
    # project = ProjectMiniSerializer(many=False)
    user = UserSerializer(many=False)

    class Meta:
        model = Commit
        fields = ('commit_name', 'commit_description', 'user')


class ProjectSerializer(serializers.ModelSerializer):
    commits = CommitSerializer(many=True)

    class Meta:
        model = Project
        fields = ('project_name', 'project_url', 'commits')


class UserProfileSerializer(serializers.ModelSerializer):
    skills_list = SkillSerializer(many=True)
    project = ProjectSerializer(many=True)
    commits = CommitSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ('address', 'payment', 'git_auth_token', 'price_per_hour',
                  'project', 'commits', 'licence_agreement', 'skills_list',)


class FeaturePostSerializer(serializers.ModelSerializer):
    proposed_by = UserSerializer(many=False)
    project = ProjectMiniSerializer(many=False)

    class Meta:

        model = FeaturePost
        fields = ('name', 'description', 'cost',
                  'time_line', 'project', 'proposed_by',)
