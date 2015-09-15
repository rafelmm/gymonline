# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymclient', '0008_auto_20150915_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='postal_code',
            field=models.CharField(verbose_name='Postal code', max_length=5),
        ),
    ]
