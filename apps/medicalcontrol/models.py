from django.db import models
from apps.core.models import Patient, Person
from django_extensions.db.fields import AutoSlugField
from apps.core.utils import STYLE_IMG_MIN
from apps.pharmacy.models import SupplyAssignControl


class Medicalcontrol(models.Model):
    name = models.CharField(max_length=100)
    natural_key = AutoSlugField(populate_from='name', verbose_name='nemotécnico')
    make = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medic = models.ForeignKey(Person, null=True, blank=True, verbose_name='medic', limit_choices_to={'rol__id': 1}) # noqa

    supplies = models.ManyToManyField(SupplyAssignControl, blank=True)

    photo_first = models.ImageField(upload_to='medicalcontrol/%Y/%m/%d/', verbose_name='foto 1', null=True, blank=True) # noqa
    photo_second = models.ImageField(upload_to='medicalcontrol/%Y/%m/%d/', verbose_name='foto 2', null=True, blank=True) # noqa
    photo_third = models.ImageField(upload_to='medicalcontrol/%Y/%m/%d/', verbose_name='foto 3', null=True, blank=True) # noqa

    def photo_first_tag(self):

        if not self.photo_first:
            p1 = '/media/none.jpg'
        else:
            p1 = self.photo_first.url

        if not self.photo_second:
            p2 = '/media/none.jpg'
        else:
            p2 = self.photo_second.url

        if not self.photo_third:
            p3 = '/media/none.jpg'
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
            this = Medicalcontrol.objects.get(id=self.id)
            if this.photo_first != self.photo_first:
                this.photo_first.delete()  # save=False
            if this.photo_second != self.photo_second and this.photo_second is not None:
                this.photo_second.delete()  # save=False
            if this.photo_third != self.photo_third and this.photo_third is not None:
                this.photo_third.delete()  # save=False
        except:
            pass  # when new photo then we do nothing, normal case
        super(Medicalcontrol, self).save(*args, **kwargs)
