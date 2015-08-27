# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canrequests', '0002_auto_20150827_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canrequest',
            name='can_type',
            field=models.CharField(null=True, choices=[('bigbelly', 'bigbelly'), ('garbage', 'garbage'), ('recycling', 'recycling')], blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='canrequest',
            name='comment',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='canrequest',
            name='image',
            field=models.ImageField(upload_to='can_requests', null=True, blank=True),
        ),
    ]
