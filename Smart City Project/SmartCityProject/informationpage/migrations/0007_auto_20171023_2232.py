# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-23 12:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informationpage', '0006_auto_20171023_2229'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='museums',
            new_name='hotel',
        ),
        migrations.RenameModel(
            old_name='restaraunts',
            new_name='museum',
        ),
        migrations.RenameModel(
            old_name='hotels',
            new_name='restaraunt',
        ),
        migrations.RenameModel(
            old_name='shoppingmalls',
            new_name='shoppingmall',
        ),
    ]
