# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('business_type', models.IntegerField()),
                ('business_name', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
                ('updated_by', models.CharField(max_length=100)),
                ('business_id', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('business_type',),
            },
        ),
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('business_type', models.IntegerField()),
                ('business_name', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
                ('updated_by', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('business_name',),
            },
        ),
    ]
