# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20160121_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply_to_disqus',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]