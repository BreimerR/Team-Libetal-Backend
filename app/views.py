from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserProfileSerializer, UserSerializer, CommitSerializer, SkillSerializer, ProjectSerializer, FeaturePostSerializer
from .models import UserProfile, Commit, Skill, Project, FeaturePost


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommitViewSet(viewsets.ModelViewSet):
    queryset = Commit.objects.all()
    serializer_class = CommitSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class FeaturePostViewset(viewsets.ModelViewSet):
    queryset = FeaturePost.objects.all()
    serializer_class = FeaturePostSerializer
