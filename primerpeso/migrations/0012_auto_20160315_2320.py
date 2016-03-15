# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-15 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerpeso', '0011_remove_opportunitysearch_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunity',
            name='requirement',
        ),
        migrations.AddField(
            model_name='opportunity',
            name='requirements',
            field=models.ManyToManyField(through='primerpeso.RequirementRelationship', to='primerpeso.Requirement', verbose_name='requirements'),
        ),
    ]
