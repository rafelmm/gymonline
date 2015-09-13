# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymclient', '0005_auto_20150913_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='date_created',
            field=models.DateField(verbose_name='Creation date', blank=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='date_updated',
            field=models.DateField(verbose_name='Update date', blank=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='popularity',
            field=models.IntegerField(null=True, verbose_name='Popularity', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(null=True, verbose_name='Address', max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(null=True, verbose_name='City', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_update',
            field=models.DateTimeField(null=True, verbose_name='Last update'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nif',
            field=models.CharField(null=True, verbose_name='NIF', max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(null=True, verbose_name='Phone number', blank=True),
        ),
    ]
