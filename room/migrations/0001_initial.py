# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-07 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('race', models.CharField(choices=[('HM', 'Human'), ('EL', 'Elf'), ('OW', 'Orc'), ('DW', 'Dwarf'), ('WW', 'WareWolf')], max_length=3)),
                ('image', models.ImageField(upload_to='Character')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('game_type', models.CharField(choices=[('SP', 'Singleplay'), ('MP', 'Multiplay')], default='SP', max_length=3)),
                ('data_begin', models.DateField(null=True)),
                ('data_end', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='Room')),
            ],
        ),
    ]
