from django.conf import settings

from cartodbsync.synchronize import synchronize
from celery import shared_task


@shared_task
def synchronize_canrequests():
    if settings.DEBUG:
        print('Would be uploading can request now, but we are in debug mode')
    else:
        synchronize()
