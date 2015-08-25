from django.core.management.base import BaseCommand

from ...models import Connection
from ...sync import sync


class Command(BaseCommand):
    help = 'Synch Socrata resources with their CartoDB tables'

    def handle(self, *args, **options):
        for connection in Connection.objects.all():
            sync(connection)
