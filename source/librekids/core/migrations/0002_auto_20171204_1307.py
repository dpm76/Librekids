# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educator',
            name='employee_ptr',
        ),
        migrations.RemoveField(
            model_name='educator',
            name='main_classroom',
        ),
        migrations.AddField(
            model_name='child',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='core.Classroom'),
        ),
        migrations.AddField(
            model_name='child',
            name='join_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='child',
            name='leave_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='classroom',
            name='educators',
            field=models.ManyToManyField(related_name='classrooms', to='core.Employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='join_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='leave_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='educator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Employee'),
        ),
        migrations.AlterField(
            model_name='child',
            name='parents',
            field=models.ManyToManyField(related_name='children', to='core.Parent'),
        ),
        migrations.DeleteModel(
            name='Educator',
        ),
    ]
