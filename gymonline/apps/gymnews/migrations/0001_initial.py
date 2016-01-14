# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('publish_date', models.DateTimeField(verbose_name='Published at', auto_now_add=True)),
                ('text', models.CharField(verbose_name='Text', max_length=2500)),
                ('tags', models.CharField(verbose_name='Tags', max_length=500)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['publish_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('email', models.EmailField(verbose_name='Email', max_length=254)),
                ('date', models.DateTimeField(verbose_name='Published at', auto_now_add=True)),
                ('text', models.CharField(verbose_name='Comment', max_length=500)),
                ('article_id', models.ForeignKey(to='gymnews.Article', verbose_name='Comment', related_name='comment_article')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['date'],
            },
        ),
    ]
