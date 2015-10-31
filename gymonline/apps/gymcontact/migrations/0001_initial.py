# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GymContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('company', models.CharField(max_length=150, verbose_name='Your company')),
                ('name', models.CharField(max_length=150, verbose_name='Your name')),
                ('phone', models.CharField(max_length=20, verbose_name='Your phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Your email')),
                ('message', models.TextField(max_length=1000, verbose_name='Your message')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Created at')),
            ],
        ),
    ]
