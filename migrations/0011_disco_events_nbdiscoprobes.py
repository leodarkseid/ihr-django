# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-12 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ihr', '0010_auto_20170612_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='disco_events',
            name='nbdiscoprobes',
            field=models.IntegerField(default=0),
        ),
    ]