from django.contrib import admin

from .models import CartodbTable, Connection, SocrataResource


class CartodbTableAdmin(admin.ModelAdmin):
    list_display = ('table', 'domain',)


class SocrataResourceAdmin(admin.ModelAdmin):
    list_display = ('endpoint', 'name', 'domain',)


admin.site.register(CartodbTable, CartodbTableAdmin)
admin.site.register(Connection)
admin.site.register(SocrataResource, SocrataResourceAdmin)
