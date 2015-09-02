from django.conf import settings
from django.contrib.gis.geos import Point

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from PIL import Image
from pygeoexif import get_exif_data, get_lat_lon

from .models import CanRequest
from .serializers import CanRequestSerializer


class CanRequestViewSet(viewsets.ModelViewSet):
    queryset = CanRequest.objects.all()
    serializer_class = CanRequestSerializer


class PostImage(APIView):

    def post(self, request):
        can_request = CanRequest(image=request.data['image'])
        can_request.save()
        context = {
            'pk': can_request.pk,
            'thumb_url': settings.BASE_URL + can_request.image_thumbnail.url,
        }

        # Attempt to get EXIF GPS data
        img = Image.open(can_request.image.path)
        lat, lon = get_lat_lon(get_exif_data(img))
        if lat and lon:
            can_request.geom = Point(lon, lat, srid=4326)
            can_request.save()
            context.update({
                'lat': lat,
                'lon': lon,
            })

        return Response(context)
