from django.conf import settings

from cartodbsync.synchronize import synchronize
from celery import shared_task

from .mailinglist import subscribe


@shared_task
def synchronize_canrequests():
    if settings.DEBUG:
        print('Would be uploading can request now, but we are in debug mode')
    else:
        synchronize()


@shared_task
def subscribe_to_mailinglist():
    if settings.DEBUG:
        print('Would be subscribing to mailinglist, but we are in debug mode')
    else:
        subscribe()
