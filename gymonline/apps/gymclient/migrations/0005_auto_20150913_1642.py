# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymclient', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=50)),
                ('description', models.CharField(blank=True, max_length=150, help_text='Write a description for the class (optional)')),
                ('intensity', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='M', max_length=1)),
                ('date_created', models.DateField(verbose_name='Creation date')),
                ('date_updated', models.DateField(verbose_name='Update date')),
                ('date_deleted', models.DateField(blank=True, null=True, verbose_name='Deleted date')),
                ('popularity', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Classes',
                'verbose_name': 'Class',
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Clase',
        ),
    ]
