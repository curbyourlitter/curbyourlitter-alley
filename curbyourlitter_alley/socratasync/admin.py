from django.contrib import admin

from .models import CartodbTable, Connection, SocrataResource


admin.site.register(CartodbTable)
admin.site.register(Connection)
admin.site.register(SocrataResource)
