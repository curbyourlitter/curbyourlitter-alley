# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canrequests', '0003_auto_20150827_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='canrequest',
            name='can_subtype',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
