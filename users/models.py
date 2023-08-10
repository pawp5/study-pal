<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matric_no = models.CharField(max_length=32)
    dept = models.CharField(max_length=64)
=======
from django.db import models

# Create your models here.
>>>>>>> 8370b914406d0e7e6cc81cdd76708d4004b83da8
