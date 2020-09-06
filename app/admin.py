from django.contrib import admin
from .models import Commit, License, Project, Skill, UserProfile, FeaturePost

admin.site.register(Commit)
admin.site.register(License)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(UserProfile)
admin.site.register(FeaturePost)
