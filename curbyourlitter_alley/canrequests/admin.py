from django.contrib import admin

from .models import CanRequest


class CanRequestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'added', 'can_type', 'can_subtype', 'name', 'email',)
    list_filter = ('can_type', 'can_subtype', 'added',)


admin.site.register(CanRequest, CanRequestAdmin)
