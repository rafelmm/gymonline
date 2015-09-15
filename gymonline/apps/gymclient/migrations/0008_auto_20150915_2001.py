# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gymclient', '0007_auto_20150915_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gym',
            old_name='date_create',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='date_update',
            new_name='date_updated',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='date_update',
        ),
        migrations.AddField(
            model_name='gym',
            name='date_updated',
            field=models.DateTimeField(verbose_name='Updated at', default=datetime.datetime(2015, 9, 15, 18, 1, 14, 542749, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class',
            name='date_deleted',
            field=models.DateTimeField(null=True, editable=False, verbose_name='Deleted at'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='date_deleted',
            field=models.DateTimeField(null=True, editable=False, verbose_name='Deleted at'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_deleted',
            field=models.DateTimeField(null=True, editable=False, verbose_name='Deleted at'),
        ),
    ]
