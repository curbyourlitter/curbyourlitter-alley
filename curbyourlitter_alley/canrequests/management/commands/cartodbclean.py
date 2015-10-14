import traceback

from cartodb.cartodb import CartoDBAPIKey, CartoDBException

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


DELETE_SQL_TEMPLATE = 'DELETE FROM {} WHERE NOT the_geom && ST_SetSRID(ST_MakeBox2D(ST_Point({}, {}), ST_Point({}, {})), 4326)'

class Command(BaseCommand):
    help = 'Clean up CartoDB data outside of a given bounding box'

    def handle(self, *args, **options):
        for table in settings.CARTODB_CLEAN_TABLES:
            self.clean_table(table, settings.CARTODB_CLEAN_BBOX)

    def clean_table(self, table, bbox):
        try:
            cl = CartoDBAPIKey(settings.CARTODB_SYNC['API_KEY'],
                               settings.CARTODB_SYNC['DOMAIN'])
            sql = DELETE_SQL_TEMPLATE.format(
                table,
                bbox[0],
                bbox[1],
                bbox[2],
                bbox[3]
            )
            cl.sql(sql)
        except Exception:
            traceback.print_exc()
            raise CommandError('There was a problem cleaning data with cartodbclean')
