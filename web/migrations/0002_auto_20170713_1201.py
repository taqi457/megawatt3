# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitedetail',
            options={'ordering': ('detail_date',)},
        ),
        migrations.AddField(
            model_name='sitedetail',
            name='site',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web.Site'),
        ),
    ]
