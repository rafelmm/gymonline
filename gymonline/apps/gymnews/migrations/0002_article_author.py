# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gymnews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.OneToOneField(related_name='article_author', default=1, verbose_name='Author', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
