# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gymclient', '0012_auto_20150928_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name='profile', verbose_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
