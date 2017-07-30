from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from .utils import phone_regex, STYLE_IMG_MIN


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

    class Meta:
        verbose_name = 'persona'

    def __str__(self):
        return '{}'.format(self.name)


class Color(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name_plural = 'colores'

    def __str__(self):
        return '{}'.format(self.name)


class AnimalType(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = 'tipo de animal'
        verbose_name_plural = 'tipo de animales'

    def __str__(self):
        return '{}'.format(self.name)


class AnimalBreed(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')
    animal_type = models.ForeignKey('AnimalType', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'raza'
        verbose_name_plural = 'razas'

    def __str__(self):
        return '{} / {}'.format(self.name, self.animal_type)


class Patient(models.Model):
    name = models.CharField(max_length=10, verbose_name='nombre')
    natural_key = AutoSlugField(populate_from='name', verbose_name='nemotécnico') # noqa
    animal_breed = models.ForeignKey('AnimalBreed', on_delete=models.CASCADE, verbose_name='raza / tipo de animal') # noqa
    author = models.ForeignKey(Person, null=True, blank=True, verbose_name='autor') # noqa
    color_first = models.ForeignKey(Color, null=True, blank=True, verbose_name='color primario', related_name='color_first') # noqa
    color_second = models.ForeignKey(Color, null=True, blank=True, verbose_name='color secundario', related_name='color_second') # noqa
    photo_first = models.ImageField(upload_to='patient/%Y/%m/%d/', verbose_name='foto 1') # noqa
    photo_second = models.ImageField(upload_to='patient/%Y/%m/%d/', verbose_name='foto 2') # noqa
    photo_third = models.ImageField(upload_to='patient/%Y/%m/%d/', verbose_name='foto 3') # noqa

    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'

    def photo_first_tag(self):
        return '<img style="{}" src="{}" />\
        <img style="{}" src="{}" />\
        <img style="{}" src="{}" />'.format(
            STYLE_IMG_MIN, self.photo_first.url,
            STYLE_IMG_MIN, self.photo_second.url,
            STYLE_IMG_MIN, self.photo_third.url,
        ) # noqa
    photo_first_tag.short_description = 'miniatura'
    photo_first_tag.allow_tags = True

    def name_tag(self):
        return '<strong>{} - {}</strong></br>{}'.format(self.id, self.name, self.natural_key) # noqa

    name_tag.admin_order_field = 'name'
    name_tag.short_description = 'Nombre'
    name_tag.allow_tags = True

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Patient.objects.get(id=self.id)
            if this.photo_first != self.photo_first:
                this.photo_first.delete()  # save=False
            if this.photo_second != self.photo_second:
                this.photo_second.delete()  # save=False
            if this.photo_third != self.photo_third:
                this.photo_third.delete()  # save=False
        except:
            pass  # when new photo then we do nothing, normal case
        super(Patient, self).save(*args, **kwargs)
