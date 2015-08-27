from django.apps import AppConfig


class CanrequestsAppConfig(AppConfig):
    name = 'canrequests'

    def ready(self):
        from .signals import sync_on_delete, sync_on_save
