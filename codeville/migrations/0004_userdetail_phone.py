# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-04 06:07
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('codeville', '0003_auto_20170704_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+918197239822', max_length=128),
        ),
    ]
