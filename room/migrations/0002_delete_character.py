# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-07 06:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Character',
        ),
    ]