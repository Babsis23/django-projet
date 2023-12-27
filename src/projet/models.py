from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import modelformset_factory


class Project(models.Model):
    period = models.CharField(max_length=100, null=False, blank=False)
    status = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    att1=models.CharField(max_length=100)
    att2=models.CharField(max_length=100)

    def __str__(self):
        return self.period
    
    def save(self, *args, **kwargs):
        print(self.period)
        super().save(*args, **kwargs)
