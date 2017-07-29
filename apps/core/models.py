from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from django.core.validators import RegexValidator


class Person(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="person", null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=20) # validators should be a list


class Color(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')


class AnimalType(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')


class AnimalBreed(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')
    animal_type = models.ForeignKey('AnimalType', on_delete=models.CASCADE)


class Patient(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')
    animal_breed = models.ForeignKey('AnimalBreed', on_delete=models.CASCADE)
    author = models.ForeignKey(Person, null=True, blank=True)
    photo_first = models.ImageField(upload_to='patient/%Y/%m/%d/')
    photo_second = models.ImageField(upload_to='patient/%Y/%m/%d/')
    photo_third = models.ImageField(upload_to='patient/%Y/%m/%d/')
