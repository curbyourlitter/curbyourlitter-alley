# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socratasync', '0002_socrataresource_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socrataresource',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
