# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymclient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='descripcion',
            field=models.CharField(help_text='Escribe una descripción para la clase (opcional)', max_length=150, blank=True),
        ),
    ]
