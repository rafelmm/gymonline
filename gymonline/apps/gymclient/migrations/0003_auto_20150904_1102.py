# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymclient', '0002_auto_20150901_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='descripcion',
            field=models.CharField(help_text='Escribe una descripcion para la clase (opcional)', max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='clase',
            name='fecha_baja',
            field=models.DateField(null=True, verbose_name='Fecha baja', blank=True),
        ),
    ]
