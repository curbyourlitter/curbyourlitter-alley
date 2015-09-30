# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canrequests', '0008_auto_20150930_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canrequest',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='can_requests'),
        ),
    ]
