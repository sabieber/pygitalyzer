# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='updated',
            field=models.DateTimeField(null=True),
        ),
    ]