from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from cartodbsync.models import SyncEntry

from .models import CanRequest
from .tasks import subscribe_to_mailinglist, synchronize_canrequests


@receiver(post_save, sender=CanRequest, dispatch_uid='canrequests.models.subscribe_on_save')
def subscribe_on_save(sender, instance=None, created=False, **kwargs):
    if instance and instance.mailing_list_opt_in:
        subscribe_to_mailinglist.delay(instance.email)


@receiver(post_save, sender=CanRequest, dispatch_uid='canrequests.models.sync_on_save')
def sync_on_save(sender, instance=None, created=False, **kwargs):
    if instance and created:
        SyncEntry.objects.mark_as_pending_insert([instance])
    elif instance:
        SyncEntry.objects.mark_as_pending_update([instance])
    synchronize_canrequests.delay()


@receiver(post_delete, sender=CanRequest, dispatch_uid='canrequests.models.sync_on_delete')
def sync_on_delete(sender, instance=None, **kwargs):
    if instance:
        SyncEntry.objects.mark_as_pending_delete([instance])
        synchronize_canrequests.delay()
