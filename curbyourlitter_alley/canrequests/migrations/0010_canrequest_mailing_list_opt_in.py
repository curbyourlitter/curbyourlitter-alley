# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canrequests', '0009_auto_20150930_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='canrequest',
            name='mailing_list_opt_in',
            field=models.BooleanField(default=False),
        ),
    ]
