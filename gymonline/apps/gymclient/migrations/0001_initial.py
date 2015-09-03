# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('intensidad', models.CharField(default='M', max_length=1, choices=[('A', 'Alta'), ('M', 'Media'), ('B', 'Baja')])),
                ('fecha_alta', models.DateField(verbose_name='Fecha alta')),
                ('fecha_modificacion', models.DateField(verbose_name='Fecha modificacion')),
                ('fecha_baja', models.DateField(verbose_name='Fecha baja')),
                ('popularidad', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Classes',
                'verbose_name': 'Clase',
                'ordering': ['-id'],
            },
        ),
    ]
