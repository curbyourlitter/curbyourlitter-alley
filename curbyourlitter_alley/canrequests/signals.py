from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from cartodbsync.models import SyncEntry

from .models import CanRequest


@receiver(post_save, sender=CanRequest, dispatch_uid='canrequests.models.sync_on_save')
def sync_on_save(sender, instance=None, created=False, **kwargs):
    if instance and created:
        SyncEntry.objects.mark_as_pending_insert([instance])
    elif instance:
        SyncEntry.objects.mark_as_pending_update([instance])


@receiver(post_delete, sender=CanRequest, dispatch_uid='canrequests.models.sync_on_delete')
def sync_on_delete(sender, instance=None, **kwargs):
    if instance:
        SyncEntry.objects.mark_as_pending_delete([instance])
