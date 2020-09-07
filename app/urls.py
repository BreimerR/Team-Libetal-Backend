from django.urls import path, include
from rest_framework import routers
from .views import UserProfileViewSet, CommitViewSet, SkillViewSet, ProjectViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('profiles', UserProfileViewSet)
router.register('users', UserViewSet)
router.register('commits', CommitViewSet)
router.register('skills', SkillViewSet)
router.register('projects', ProjectViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
