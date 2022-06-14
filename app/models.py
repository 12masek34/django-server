from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
