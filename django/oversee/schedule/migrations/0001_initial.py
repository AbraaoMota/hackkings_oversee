# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabilities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Availability')),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('calendar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schedule.Calendar')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('availability', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schedule.Availability')),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='user_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.User'),
        ),
    ]