# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0002_auto_20160227_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='url',
            field=models.URLField(unique=True, verbose_name='Repository Clone URL'),
        ),
    ]
