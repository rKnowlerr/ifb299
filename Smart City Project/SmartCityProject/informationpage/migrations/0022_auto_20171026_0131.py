# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-25 15:31
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informationpage', '0021_auto_20171026_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=django.core.files.storage.FileSystemStorage(location='/SmartCityProject/storage')),
        ),
    ]
