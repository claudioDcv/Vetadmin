from django.db.models.signals import pre_delete, post_save
from django.dispatch.dispatcher import receiver
from .models import Patient, Person, Participant, Organization
from django.contrib.contenttypes.models import ContentType


# SIGNALS
@receiver(pre_delete, sender=Patient)
def patient_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.photo_first.delete(False)
    instance.photo_second.delete(False)
    instance.photo_third.delete(False)


@receiver(post_save, sender=Person)
def create_participant_person(sender, instance, **kwargs):
    c = ContentType.objects.get(app_label="core", model="person")
    if len(Participant.objects.filter(content_type=c, object_id=instance.id)) == 0:
        if instance.rol.pk in [1, 2, 3]:
            Participant.objects.create(content_type=c, object_id=instance.id)
    else:
        if instance.rol.pk in [1, 2, 3]:
            Participant.objects.create(content_type=c, object_id=instance.id)
        elif instance.rol.pk in [4]:
            Participant.objects.filter(content_type=c, object_id=instance.id).delete()


@receiver(pre_delete, sender=Person)
def delete_participant_person(sender, instance, **kwargs):
    c = ContentType.objects.get(app_label="core", model="person")
    Participant.objects.filter(content_type=c, object_id=instance.id).delete()


@receiver(post_save, sender=Organization)
def create_participant_organization(sender, instance, **kwargs):
    c = ContentType.objects.get(app_label="core", model="organization")
    if len(Participant.objects.filter(content_type=c, object_id=instance.id)) == 0:
        Participant.objects.create(content_type=c, object_id=instance.id)


@receiver(pre_delete, sender=Organization)
def delete_participant_organization(sender, instance, **kwargs):
    c = ContentType.objects.get(app_label="core", model="person")
    Participant.objects.filter(content_type=c, object_id=instance.id).delete()
