# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gymclient', '0003_auto_20150904_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('birthday', models.DateTimeField(verbose_name='Birthday')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1, verbose_name='Gender')),
                ('postal_code', models.IntegerField(verbose_name='Postal code')),
                ('phone', models.IntegerField(verbose_name='Phone number')),
                ('nif', models.CharField(verbose_name='NIF', max_length=10)),
                ('city', models.CharField(verbose_name='City', max_length=50)),
                ('address', models.CharField(verbose_name='Address', max_length=150)),
                ('date_update', models.DateTimeField(verbose_name='Last update')),
                ('user', models.OneToOneField(related_name='profile', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'ordering': ('user',),
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
