# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20161026_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecommerceuser',
            name='username',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='ecommerceuser',
            name='phone_number',
            field=models.CharField(help_text='Phone number', max_length=30, verbose_name='phone number'),
        ),
    ]
