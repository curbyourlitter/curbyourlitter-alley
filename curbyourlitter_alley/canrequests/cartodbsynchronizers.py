from django.conf import settings

from cartodbsync.synchronizers import BaseSynchronizer


class CanRequestSynchronizer(BaseSynchronizer):

    def get_column_names(self):
        return [
            'id',
            'added',
            'can_type',
            'can_subtype',
            'comment',
            'image',
            'name',
            'the_geom',
        ]

    def get_cartodb_mapping(self, instance):
        mapping = {
            'id': instance.pk,
            'added': instance.added,
            'can_type': instance.can_type,
            'can_subtype': instance.can_subtype,
            'comment': instance.comment,
            'image': None,
            'name': instance.name,
            'the_geom': instance.geom,
        }

        try:
            mapping['image'] = settings.BASE_URL + instance.image_medium_thumbnail.url
        except ValueError:
            pass

        return mapping
