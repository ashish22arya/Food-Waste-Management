# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roomNum',
            field=models.CharField(max_length=10),
        ),
    ]
