# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-24 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informationpage', '0009_auto_20171024_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city_park',
            name='imagelink',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='city_park',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='college',
            name='imagelink',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='college',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='imagelink',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='industrie',
            name='imagelink',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='industrie',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='museum',
            name='imagelink',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='museum',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='restaraunt',
            name='imagelink',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='restaraunt',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='shoppingmall',
            name='imagelink',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='shoppingmall',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='zoo',
            name='imagelink',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='zoo',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
