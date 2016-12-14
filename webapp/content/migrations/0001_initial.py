# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 03:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Msisdn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msisdn', models.CharField(max_length=12)),
                ('verif_code', models.CharField(max_length=12)),
                ('is_verified', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Msisdn',
            },
        ),
        migrations.CreateModel(
            name='MsisdnUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_code', models.CharField(max_length=12)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('msisdn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
