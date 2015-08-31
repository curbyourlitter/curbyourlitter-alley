# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socratasync', '0001_squashed_0002_auto_20150824_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='socrataresource',
            name='name',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
