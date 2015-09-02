from django.contrib.gis.db import models


class CanRequest(models.Model):
    CAN_TYPES = (
        ('bigbelly', 'bigbelly'),
        ('garbage', 'garbage'),
        ('recycling', 'recycling'),
    )
    can_type = models.CharField(choices=CAN_TYPES, max_length=25, blank=True,
                                null=True)
    can_subtype = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    image = models.ImageField(upload_to='can_requests', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
