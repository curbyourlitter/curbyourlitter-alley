from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils.timezone import now

from ...models import CanRequest


class Command(BaseCommand):
    help = 'Clean can requests that are incompete'

    def handle(self, *args, **options):
        can_requests = CanRequest.objects.filter(
            geom=None,
            added__lt=now() - timedelta(minutes=5)
        )
        for can_request in can_requests:
            can_request.delete()
