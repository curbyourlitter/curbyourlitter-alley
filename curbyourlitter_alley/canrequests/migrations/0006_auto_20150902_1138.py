# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('canrequests', '0005_canrequest_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canrequest',
            name='email',
            field=models.EmailField(blank=True, null=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='canrequest',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='canrequest',
            name='name',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
    ]
