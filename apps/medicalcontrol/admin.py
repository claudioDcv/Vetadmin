from django.contrib import admin
from .models import Medicalcontrol
from .forms import MedicalcontrolForm


class MedicalcontrolAdmin(admin.ModelAdmin):
    list_display = (
        'photo_first_tag',
        'name_tag',
        'make',
        'patient',
        'medic',
    )
    readonly_fields = ('photo_first_tag', 'natural_key',)
    empty_value_display = '-vacio-'
    form = MedicalcontrolForm


admin.site.register(Medicalcontrol, MedicalcontrolAdmin)
