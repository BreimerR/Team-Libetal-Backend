from django.db import models
from django.contrib.auth.models import User

PAYMENT_OPTIONS = (
    ('VISA', ' Visa Card'),
    ('PAYPAL', 'Paypal'),
    ('MASTER CARD', 'Master Card'),
    ('MPESA', 'MPESA'),
)

SKILL_EXPERIENCE = (
    ('B', 'Beginner'),
    ('I', 'Intermediate'),
    ('E', 'Expert'),
)

SKILL_NAMES = (
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('C/C++', 'C/C++'),
    ('Node', 'Nodejs'),
    ('Typescript', 'Typescript'),
    ('Django', 'Django'),
    ('React', 'React'),
    ('Angular', 'Angular'),
    ('Flask', 'Flask'),
    ('Vue', 'Vue'),
    ('Javascript', 'Javascript'),
    ('Web', 'HTML/CSS'),
)

LICENSE_ACCEPTANCE_STATE = (
    ('Y', 'YES'),
    ('N', 'NO'),
)

PROJECT_ACCESSIBILITY_TYPE = (
    ('Public', 'Public'),
    ('Private', 'Private'),
    ('Restricted', 'Restricted'),
)


class Skill(models.Model):
    skill_name = models.CharField(max_length=12, choices=SKILL_NAMES)
    skill_experience = models.CharField(
        max_length=12, choices=SKILL_EXPERIENCE)
    years_of_experience = models.IntegerField()


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_decription = models.TextField()
    project_url = models.URLField()
    accessibility = models.CharField(
        max_length=10, choices=PROJECT_ACCESSIBILITY_TYPE)


class Commit(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    commit_name = models.CharField(max_length=256)


class License(models.Model):
    license_terms = models.TextField()
    license_acceptance = models.CharField(
        max_length=1, choices=LICENSE_ACCEPTANCE_STATE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    payment = models.CharField(
        choices=PAYMENT_OPTIONS, blank=True, max_length=15)
    git_auth_token = models.CharField(max_length=512, blank=True, null=True)
    price_per_hour = models.DecimalField(
        max_digits=7, decimal_places=2, default=0)
    skills_list = models.ManyToManyField(Skill)
    project = models.ManyToManyField(Project)
    commits = models.ManyToManyField(Commit)
    licence_agreement = models.OneToOneField(License, on_delete=models.CASCADE)


class FeaturePost(models.Model):
    commit = models.ForeignKey(Commit, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    time_line = models.IntegerField()
    licence_agreement = models.OneToOneField(License, on_delete=models.CASCADE)
    proposed_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
