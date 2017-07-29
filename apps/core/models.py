from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from .utils import phone_regex


class Person(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        related_name='person',
        null=True, blank=True,
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        blank=True, max_length=20,
    )

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
