from django.contrib import admin
from .models import Color, Patient, AnimalBreed, AnimalType, Person


class PersonAdmin(admin.ModelAdmin):
    pass


class ColorAdmin(admin.ModelAdmin):
    pass


class AnimalBreedAdmin(admin.ModelAdmin):
    pass


class AnimalTypeAdmin(admin.ModelAdmin):
    pass


class PatientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(AnimalBreed, AnimalBreedAdmin)
admin.site.register(AnimalType, AnimalTypeAdmin)
admin.site.register(Patient, PatientAdmin)
