# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canrequests', '0006_auto_20150902_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canrequest',
            name='can_type',
            field=models.CharField(choices=[('litter', 'litter'), ('recycling', 'recycling')], null=True, blank=True, max_length=25),
        ),
    ]
