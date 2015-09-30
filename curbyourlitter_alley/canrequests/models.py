from django.contrib.gis.db import models

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, Transpose

from .mail import send_moderation_email


class CanRequest(models.Model):
    CAN_TYPES = (
        ('litter', 'litter'),
        ('recycling', 'recycling'),
    )
    can_type = models.CharField(choices=CAN_TYPES, max_length=25, blank=True,
                                null=True)
    can_subtype = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    image = ProcessedImageField(upload_to='can_requests', blank=True,
                                null=True, processors=[Transpose()],
                                format='JPEG', options={'quality': 60})
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Transpose(), ResizeToFill(150, 150)],
        format='JPEG',
        options={'quality': 60}
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)

    __original_name = None
    __original_email = None

    def __init__(self, *args, **kwargs):
        super(CanRequest, self).__init__(*args, **kwargs)
        self.__original_name = self.name
        self.__original_email = self.email

    def save(self, *args, **kwargs):
        # If we're newly adding name and email--a newly complete request--send
        # the moderation email
        if self.name and self.email and (not self.pk or not \
                                           (self.__original_name or self.__original_email)):
            send_moderation_email(self)
        super(CanRequest, self).save(*args, **kwargs)
        self.__original_name = self.name
        self.__original_email = self.email
