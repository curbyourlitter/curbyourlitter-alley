# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('canrequests', '0007_auto_20150928_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canrequest',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='can_requests', blank=True),
        ),
    ]
