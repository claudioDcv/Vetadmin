from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from .models import Patient


# SIGNALS
@receiver(pre_delete, sender=Patient)
def patient_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.photo_first.delete(False)
    instance.photo_second.delete(False)
    instance.photo_third.delete(False)
