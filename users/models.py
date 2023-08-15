from django.db import models
from django.contrib.auth.models import User
from .utils.choices import DEPT_CHOICES, LEVEL_CHOICES


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matric_no = models.CharField(max_length=32)
    department = models.CharField(max_length=50, blank=True, null=True, choices=DEPT_CHOICES)
    school_year = models.CharField(max_length=50, blank=True, null=True, choices=LEVEL_CHOICES)