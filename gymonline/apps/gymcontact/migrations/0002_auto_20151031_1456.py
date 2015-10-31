# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymcontact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymcontact',
            name='message',
            field=models.TextField(verbose_name='Your message', max_length=1000, blank=True, null=True),
        ),
    ]
