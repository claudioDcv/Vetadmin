# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CoreAnimalbreed(models.Model):
    name = models.CharField(max_length=100)
    natural_key = models.CharField(max_length=100)
    animal_type = models.ForeignKey('CoreAnimaltype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_animalbreed'


class CoreAnimaltype(models.Model):
    name = models.CharField(max_length=100)
    natural_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'core_animaltype'


class CoreColor(models.Model):
    name = models.CharField(max_length=100)
    natural_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'core_color'


class CorePatient(models.Model):
    name = models.CharField(max_length=100)
    natural_key = models.CharField(max_length=100)
    animal_breed = models.ForeignKey(CoreAnimalbreed, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_patient'


class CorePerson(models.Model):
    name = models.CharField(max_length=100)
    natural_key = models.CharField(max_length=100)
    place = models.ForeignKey(AuthUser, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'core_person'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MedicalcontrolMedicalcontrol(models.Model):
    name = models.CharField(max_length=100)
    natural_key = models.CharField(max_length=100)
    make = models.DateTimeField()
    patient = models.ForeignKey(CorePatient, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'medicalcontrol_medicalcontrol'


class MedicalcontrolMedicalcontrolSuppliesAsign(models.Model):
    medicalcontrol = models.ForeignKey(MedicalcontrolMedicalcontrol, models.DO_NOTHING)
    supplyasigncontrol = models.ForeignKey('PharmacySupplyasigncontrol', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'medicalcontrol_medicalcontrol_supplies_asign'
        unique_together = (('medicalcontrol', 'supplyasigncontrol'),)


class PharmacySupply(models.Model):
    name = models.CharField(max_length=100)
    natural_key = models.CharField(max_length=100)
    description = models.TextField()
    stocks = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    unit_of_measurement = models.ForeignKey('PharmacyUnitofmeasurement', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pharmacy_supply'


class PharmacySupplyasigncontrol(models.Model):
    date = models.DateTimeField()
    code_supply = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    supply = models.ForeignKey(PharmacySupply, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pharmacy_supplyasigncontrol'


class PharmacySupplymovement(models.Model):
    date = models.DateTimeField()
    code_supply = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    supply = models.ForeignKey(PharmacySupply, models.DO_NOTHING)
    type_supply_movement = models.ForeignKey('PharmacyTypesupplymovement', models.DO_NOTHING)
    user_from = models.ForeignKey(AuthUser, models.DO_NOTHING)
    user_to = models.ForeignKey(AuthUser, models.DO_NOTHING)
    expire_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'pharmacy_supplymovement'


class PharmacyTypesupplymovement(models.Model):
    name = models.CharField(max_length=100)
    natural_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pharmacy_typesupplymovement'


class PharmacyUnitofmeasurement(models.Model):
    name = models.CharField(max_length=100)
    natural_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pharmacy_unitofmeasurement'
