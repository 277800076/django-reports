# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-10 15:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Filter Name')),
                ('type', models.CharField(choices=[(b'Date', 'Date'), (b'Text', 'Text'), (b'Select', 'Select'), (b'Month', 'Month'), (b'SRCSelect', 'Select from a source'), (b'HLDSelect', 'Select from a source')], max_length=64, verbose_name='Filter Type')),
                ('description', models.CharField(max_length=128, verbose_name='Description of This Filter')),
                ('default_value', models.CharField(blank=True, max_length=256, null=True, verbose_name='Default Value of this filter')),
            ],
        ),
        migrations.CreateModel(
            name='FilterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Filter Name')),
                ('default_value', models.CharField(max_length=256, verbose_name='Default Value')),
            ],
        ),
        migrations.CreateModel(
            name='Slice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filters', models.ManyToManyField(to='reports.Filter')),
            ],
        ),
        migrations.CreateModel(
            name='SQL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('datasource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.DataSource')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='slice',
            name='sql',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.SQL'),
        ),
    ]
