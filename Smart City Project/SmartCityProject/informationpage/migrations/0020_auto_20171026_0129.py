# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-25 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informationpage', '0019_auto_20171026_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='storage'),
        ),
    ]
