# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymclient', '0009_auto_20150915_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('active', models.BooleanField(default=True, editable=False)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('date_created', models.DateTimeField(verbose_name='Created at', auto_now_add=True)),
                ('date_updated', models.DateTimeField(verbose_name='Updated at', auto_now=True)),
                ('email', models.EmailField(verbose_name='Email', max_length=254)),
                ('phone', models.CharField(verbose_name='Phone Number', max_length=20)),
                ('address', models.CharField(verbose_name='Address', max_length=250)),
                ('postal_code', models.CharField(verbose_name='Postal Code', max_length=5)),
                ('region', models.CharField(verbose_name='Region', max_length=20)),
                ('country', models.CharField(default='ES', verbose_name='Country', choices=[('ES', 'Spain'), ('FR', 'France'), ('PT', 'Portugal')], max_length=2)),
                ('date_deleted', models.DateTimeField(verbose_name='Deleted at', editable=False, null=True)),
                ('gym', models.ForeignKey(related_name='gym', verbose_name='Gym', to='gymclient.Gym')),
            ],
            options={
                'verbose_name_plural': 'Gym Centers',
                'ordering': ['name'],
                'verbose_name': 'Gym Center',
            },
        ),
    ]
