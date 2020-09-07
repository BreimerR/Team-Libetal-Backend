from django.urls import path, include
from rest_framework import routers
from .views import UserProfileViewSet, CommitViewSet, SkillViewSet, ProjectViewSet, UserViewSet, FeaturePostViewset

router = routers.DefaultRouter()
router.register('profiles', UserProfileViewSet)
router.register('users', UserViewSet)
router.register('commits', CommitViewSet)
router.register('skills', SkillViewSet)
router.register('projects', ProjectViewSet)
router.register('features', FeaturePostViewset)
urlpatterns = [
    path('', include(router.urls)),
]
