# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseballStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=6)),
                ('number', models.IntegerField()),
                ('avg', models.FloatField()),
                ('hr', models.IntegerField()),
                ('rbi', models.IntegerField()),
                ('runs', models.IntegerField()),
            ],
        ),
    ]
