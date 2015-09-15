# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gymclient', '0006_auto_20150913_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('cif', models.CharField(max_length=10, verbose_name='CIF')),
                ('active', models.BooleanField(editable=False, verbose_name='Active', default=True)),
                ('profile', models.CharField(max_length=50, verbose_name='Profile')),
                ('date_create', models.DateTimeField(verbose_name='Created at', auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True, verbose_name='Updated at')),
                ('date_deleted', models.DateField(null=True, editable=False, verbose_name='Deleted at', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Gyms',
                'verbose_name': 'Gym',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='class',
            name='active',
            field=models.BooleanField(verbose_name='Active', default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_deleted',
            field=models.DateTimeField(editable=False, verbose_name='Deleted at', default=datetime.datetime(2015, 9, 15, 17, 53, 18, 451868, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class',
            name='date_created',
            field=models.DateTimeField(verbose_name='Created at', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='date_deleted',
            field=models.DateTimeField(null=True, verbose_name='Deleted at', blank=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at', default=datetime.datetime(2015, 9, 15, 17, 53, 42, 731146, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
