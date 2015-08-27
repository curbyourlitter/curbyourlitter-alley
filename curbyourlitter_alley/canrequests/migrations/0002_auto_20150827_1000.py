# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canrequests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='canrequest',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='canrequest',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='canrequest',
            name='can_type',
            field=models.CharField(max_length=25, choices=[('bigbelly', 'bigbelly'), ('garbage', 'garbage'), ('recycling', 'recycling')]),
        ),
    ]
