# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.contrib.auth import get_user_model

#
# # Create your models here.
class Logs(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100,null=True)





