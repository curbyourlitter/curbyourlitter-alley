from django.conf import settings
from django.contrib.gis.geos import Point
from django.utils.timezone import now

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

    def update(self, request, pk=None):
        # Only allow updating CanRequest objects within five minutes
        can_request = CanRequest.objects.get(pk=pk)
        if can_request:
            if (now() - can_request.added).seconds <= 5 * 60:
                return super(CanRequestViewSet, self).update(request, pk=pk)
        return Response({ 'error': 'too late!' })


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
