from django.contrib.gis.db import models


class CanRequest(models.Model):
    CAN_TYPES = (
        ('bigbelly', 'bigbelly'),
        ('garbage', 'garbage'),
        ('recycling', 'recycling'),
    )
    can_type = models.CharField(choices=CAN_TYPES, max_length=25, blank=True,
                                null=True)
    comment = models.TextField(blank=True, null=True)
    geom = models.PointField()
    image = models.ImageField(upload_to='can_requests', blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
