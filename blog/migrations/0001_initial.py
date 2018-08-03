# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('headline', models.CharField(max_length=255, default='')),
                ('slug', models.SlugField(max_length=31, unique=True, help_text='A label for URL config.')),
                ('teaserpic', models.ImageField(blank=True, null=True, upload_to='img/blog/teaser/')),
                ('longtext', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Blog entries',
                'ordering': ['-published_date'],
            },
        ),
        migrations.CreateModel(
            name='MarketingElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(max_length=31, unique=True, help_text='A label for URL config.')),
                ('headline', models.CharField(max_length=255, default='')),
                ('pic', models.ImageField(upload_to='img/marketing/')),
                ('shorttext', models.CharField(max_length=255, default='')),
                ('longtext', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
