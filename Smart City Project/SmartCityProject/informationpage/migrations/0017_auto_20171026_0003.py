# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-25 14:03
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informationpage', '0016_hotel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/SmartCityProject/storage'), upload_to=''),
        ),
    ]