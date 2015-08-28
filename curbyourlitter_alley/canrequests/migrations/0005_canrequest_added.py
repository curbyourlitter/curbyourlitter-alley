# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('canrequests', '0004_canrequest_can_subtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='canrequest',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 8, 28, 16, 28, 21, 393508, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
