# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microgrids', '0015_auto_20180502_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvdigitalquantitydata',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='pvdigitalquantitydata',
            name='DC_overvoltage',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '异常')], null=True, verbose_name='直流过压'),
        ),
    ]