# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CanRequest',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('can_type', models.CharField(max_length=25, choices=[('garbage', 'garbage'), ('recycling', 'recycling')])),
                ('comment', models.TextField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('image', models.ImageField(upload_to='can_requests')),
            ],
        ),
    ]
