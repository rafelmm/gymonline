# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gymclient', '0010_center'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='center',
            name='email',
        ),
        migrations.RemoveField(
            model_name='center',
            name='phone',
        ),
        migrations.AddField(
            model_name='center',
            name='contact_person',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Contact person', default=1),
            preserve_default=False,
        ),
    ]
