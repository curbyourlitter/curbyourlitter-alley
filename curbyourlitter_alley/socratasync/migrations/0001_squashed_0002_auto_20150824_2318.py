# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartodbTable',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('apiKey', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('table', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('adapter', models.CharField(max_length=50, null=True, blank=True)),
                ('cartodb_table', models.ForeignKey(to='socratasync.CartodbTable')),
            ],
        ),
        migrations.CreateModel(
            name='SocrataResource',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('conditions', models.TextField()),
                ('domain', models.CharField(max_length=100)),
                ('endpoint', models.CharField(max_length=500)),
                ('token', models.CharField(max_length=50)),
                ('unique_key', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='connection',
            name='socrata_resource',
            field=models.ForeignKey(to='socratasync.SocrataResource'),
        ),
    ]
