from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    is_instructor = models.BooleanField(default=False)
    is_learner = models.BooleanField(default=False)
    
    