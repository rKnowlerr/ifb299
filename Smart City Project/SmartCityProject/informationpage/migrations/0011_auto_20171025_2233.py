# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-25 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informationpage', '0010_auto_20171024_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='imagelink',
            field=models.ImageField(upload_to=''),
        ),
    ]