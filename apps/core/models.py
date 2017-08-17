from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from .utils import phone_regex, STYLE_IMG_MIN, STYLE_IMG_NONE
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Role(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name_plural = 'roles'

    def __str__(self):
        return '{}'.format(self.name)


class Participant(models.Model):
    limit_choices = models.Q(
        app_label='core', model='person') | models.Q(
        app_label='core', model='organization')
    content_type = models.ForeignKey(ContentType, limit_choices_to=limit_choices)
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        rol = 'Org'
        if str(self.content_type) == 'persona':
            rol = self.content_object.rol
        return '{}({})'.format(self.content_object.name, rol)


class Organization(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')
    phone_number = models.CharField(
        validators=[phone_regex],
        blank=True, max_length=20,
    )

    class Meta:
        verbose_name = 'organización'

    def __str__(self):
        return '{}'.format(self.name)


class Person(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name')
    rol = models.ForeignKey(Role, null=False, blank=False, verbose_name='rol') # noqa
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
    client = models.ForeignKey(Person, null=True, blank=True, verbose_name='cliente', related_name='client', limit_choices_to={'rol__id': 4}) # noqa
    author = models.ForeignKey(Person, null=True, blank=True, verbose_name='autor', limit_choices_to={'rol__id': 1}) # noqa
    color_first = models.ForeignKey(Color, null=True, blank=True, verbose_name='color primario', related_name='color_first') # noqa
    color_second = models.ForeignKey(Color, null=True, blank=True, verbose_name='color secundario', related_name='color_second') # noqa
    photo_first = models.ImageField(upload_to='patient/%Y/%m/%d/', verbose_name='foto 1', null=True, blank=True) # noqa
    photo_second = models.ImageField(upload_to='patient/%Y/%m/%d/', verbose_name='foto 2', null=True, blank=True) # noqa
    photo_third = models.ImageField(upload_to='patient/%Y/%m/%d/', verbose_name='foto 3', null=True, blank=True) # noqa

    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'pacientes'

    def __str__(self):
        return '{} / {}'.format(self.name, self.animal_breed)

    def photo_first_tag(self):

        if not self.photo_first:
            p1 = STYLE_IMG_NONE
        else:
            p1 = self.photo_first.url

        if not self.photo_second:
            p2 = STYLE_IMG_NONE
        else:
            p2 = self.photo_second.url

        if not self.photo_third:
            p3 = STYLE_IMG_NONE
        else:
            p3 = self.photo_third.url

        return '<img style="{}" src="{}" />\
        <img style="{}" src="{}" />\
        <img style="{}" src="{}" />'.format(
            STYLE_IMG_MIN, p1,
            STYLE_IMG_MIN, p2,
            STYLE_IMG_MIN, p3,
        )
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
