from django.db import models
from django.core import validators
from .models import Login
from django.forms import ValidationError
from django.forms import ModelForm, Field, ValidationError, BooleanField, CharField
from django.forms.widgets import CheckboxInput, Select
from django import forms
from .models import *
class Loginform(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username','password']

    def clean(self):
       email = self.cleaned_data.get('username')
       if Login.objects.filter(username=email).exists():
            raise ValidationError("Email exists")
       return self.cleaned_data