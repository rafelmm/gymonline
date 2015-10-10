# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gymclient', '0011_auto_20150915_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('es', 'Spanish'), ('ca', 'Catalan')], max_length=2, default='es')),
                ('name', models.CharField(verbose_name='Name', max_length=50)),
            ],
            options={
                'ordering': ['language', 'name'],
                'verbose_name_plural': 'Countries',
                'verbose_name': 'Country',
            },
        ),
        migrations.CreateModel(
            name='GymClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('description', models.CharField(verbose_name='Description', blank=True, max_length=500, help_text='Write a description for the class (optional)')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('date_updated', models.DateTimeField(verbose_name='Updated at', auto_now=True)),
                ('number_of_views', models.IntegerField(verbose_name='Number of views', editable=False, default=0)),
                ('mark', models.DecimalField(decimal_places=1, verbose_name='Mark', max_digits=2, editable=False, default=0)),
                ('date_deleted', models.DateTimeField(verbose_name='Deleted at', null=True, editable=False)),
                ('popularity', models.IntegerField(blank=True, verbose_name='Popularity', null=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Classes',
                'verbose_name': 'Class',
            },
        ),
        migrations.CreateModel(
            name='GymClassSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('description', models.CharField(verbose_name='Description', blank=True, max_length=500, help_text='Write a description for the session (optional)')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('date_updated', models.DateTimeField(verbose_name='Updated at', auto_now=True)),
                ('number_of_views', models.IntegerField(verbose_name='Number of views', editable=False, default=0)),
                ('mark', models.DecimalField(decimal_places=1, verbose_name='Mark', max_digits=2, editable=False, default=0)),
                ('date_deleted', models.DateTimeField(verbose_name='Deleted at', null=True, editable=False)),
                ('popularity', models.IntegerField(blank=True, verbose_name='Popularity', null=True)),
                ('gymClass', models.ForeignKey(to='gymclient.GymClass', related_name='session_of_class', verbose_name='Class')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Class Sessions',
                'verbose_name': 'Class Session',
            },
        ),
        migrations.CreateModel(
            name='IntensityLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('es', 'Spanish'), ('ca', 'Catalan')], max_length=2, default='es')),
                ('description', models.CharField(verbose_name='Description', max_length=20)),
            ],
            options={
                'ordering': ['language', 'description'],
                'verbose_name_plural': 'Intensity Levels',
                'verbose_name': 'Intensity Level',
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('date_updated', models.DateTimeField(verbose_name='Updated at', auto_now=True)),
                ('number_of_views', models.IntegerField(verbose_name='Number of views', editable=False, default=0)),
                ('mark', models.DecimalField(decimal_places=1, verbose_name='Mark', max_digits=2, editable=False, default=0)),
                ('date_deleted', models.DateTimeField(verbose_name='Deleted at', null=True, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Monitors',
                'verbose_name': 'Monitor',
            },
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.AddField(
            model_name='center',
            name='mark',
            field=models.DecimalField(decimal_places=1, verbose_name='Mark', max_digits=2, editable=False, default=0),
        ),
        migrations.AddField(
            model_name='center',
            name='number_of_views',
            field=models.IntegerField(verbose_name='Number of views', editable=False, default=0),
        ),
        migrations.AddField(
            model_name='gym',
            name='contact_person',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='gym_contact_person', verbose_name='Gym Contact person', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gym',
            name='mark',
            field=models.DecimalField(decimal_places=1, verbose_name='Mark', max_digits=2, editable=False, default=0),
        ),
        migrations.AddField(
            model_name='gym',
            name='number_of_views',
            field=models.IntegerField(verbose_name='Number of views', editable=False, default=0),
        ),
        migrations.AlterField(
            model_name='center',
            name='contact_person',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='center_contact_person', verbose_name='Center Contact person'),
        ),
        migrations.AlterField(
            model_name='center',
            name='country',
            field=models.ForeignKey(to='gymclient.Country', related_name='center_country', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='center',
            name='gym',
            field=models.ForeignKey(to='gymclient.Gym', related_name='belongs_to_gym', verbose_name='Gym'),
        ),
        migrations.AlterField(
            model_name='center',
            name='name',
            field=models.CharField(verbose_name='Center Name', max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='custom_user_profile', verbose_name='user'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='gym',
            field=models.ForeignKey(to='gymclient.Gym', related_name='monitor_gym', verbose_name='Gym'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='monitor_user_profile', verbose_name='user'),
        ),
        migrations.AddField(
            model_name='gymclass',
            name='intensity',
            field=models.ForeignKey(to='gymclient.IntensityLevel', related_name='class_intensity', verbose_name='Intensity Level'),
        ),
        migrations.AddField(
            model_name='gymclass',
            name='monitor',
            field=models.ForeignKey(to='gymclient.Monitor', related_name='monitor_of_class', verbose_name='Monitor'),
        ),
    ]
