from django.contrib import admin
from .models import Color, Patient, AnimalBreed, AnimalType, Person, Organization, Participant, Role
from .forms import PatientForm


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
        'client',
        'author',
    )
    fields = (
        'photo_first_tag',
        'name',
        'natural_key',
        'animal_breed',
        'client',
        'author',
        'color_first',
        'color_second',
        'photo_first',
        'photo_second',
        'photo_third',
    )
    readonly_fields = ('photo_first_tag', 'natural_key',)
    empty_value_display = '-vacio-'
    form = PatientForm


class OrganizationAdmin(admin.ModelAdmin):
    pass


class ParticipantAdmin(admin.ModelAdmin):
    autocomplete_lookup_fields = {
        'generic': [['content_type', 'object_id']],
    }
    readonly_fields = ('object_id', 'content_type',)

    def a(self):
        pass

    def has_delete_permission(self, request, obj=None):
        self.a()
        return False

    def has_add_permission(self, request, obj=None):
        return False

    # def has_change_permission(self, request, obj=None):
    #    return False

class RoleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(AnimalBreed, AnimalBreedAdmin)
admin.site.register(AnimalType, AnimalTypeAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Role, RoleAdmin)
