from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from djrichtextfield.models import RichTextField


class testimony(models.Model):
    name =  models.CharField(null=True,max_length=50)
    post =  models.CharField(null=True,max_length=50)
    detail = models.TextField(null=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.name

class Book_Table(models.Model):
    name =  models.CharField(null=True,max_length=50)
    mobile =  models.IntegerField(null=True)
    time = models.TimeField(null=True)
    persons = models.CharField(null=True,max_length=10)
    date = models.DateField()
    def __str__(self):
        return self.name

class Menu(models.Model):
    CHOICES = [("cakes","cakes"),("chinese","chinese"),("indian","indian"),("italian","italian")]
    menu_choice = models.CharField(max_length=30, choices=CHOICES)
    image = models.FileField(null=True)
    name =  models.CharField(null=True,max_length=50)
    detail = models.TextField(null=True,max_length=500)
    price =  models.IntegerField(null=True)
    def __str__(self):
        return self.name