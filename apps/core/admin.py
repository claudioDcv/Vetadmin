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
    list_display = (
        'photo_first_tag',
        'name_tag',
        'color_first',
        'color_second',
        'animal_breed',
        'author',
    )
    fields = (
        'photo_first_tag',
        'name',
        'natural_key',
        'animal_breed',
        'author',
        'color_first',
        'color_second',
        'photo_first',
        'photo_second',
        'photo_third',
    )
    readonly_fields = ('photo_first_tag', 'natural_key',)
    empty_value_display = '-vacio-'


admin.site.register(Person, PersonAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(AnimalBreed, AnimalBreedAdmin)
admin.site.register(AnimalType, AnimalTypeAdmin)
admin.site.register(Patient, PatientAdmin)
