from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.template.loader import get_template

from cartodbsync.models import SyncEntry

from .models import CanRequest


def send_moderation_email(can_request):
    ctx = {
        'obj': can_request,
        'base_url': settings.BASE_URL,
    }
    text = get_template('canrequests/moderation_email.txt').render(ctx)
    html = get_template('canrequests/moderation_email.html').render(ctx)
    send_mail(settings.EMAIL_SUBJECT_PREFIX + 'New can request', text,
              settings.DEFAULT_FROM_EMAIL, settings.MODERATORS,
              html_message=html)


@receiver(post_save, sender=CanRequest, dispatch_uid='canrequests.models.sync_on_save')
def sync_on_save(sender, instance=None, created=False, **kwargs):
    if instance and created:
        send_moderation_email(instance)
        SyncEntry.objects.mark_as_pending_insert([instance])
    elif instance:
        SyncEntry.objects.mark_as_pending_update([instance])


@receiver(post_delete, sender=CanRequest, dispatch_uid='canrequests.models.sync_on_delete')
def sync_on_delete(sender, instance=None, **kwargs):
    if instance:
        SyncEntry.objects.mark_as_pending_delete([instance])
