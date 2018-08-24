# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-24 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_text', models.TextField(blank=True)),
                ('is_draft', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportEdition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edition_time', models.DateTimeField()),
                ('edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Employee')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Report')),
            ],
        ),
        migrations.CreateModel(
            name='ChildFolder',
            fields=[
                ('folder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio.Folder')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Child')),
            ],
            bases=('portfolio.folder',),
        ),
        migrations.CreateModel(
            name='ClassroomFolder',
            fields=[
                ('folder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio.Folder')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Classroom')),
            ],
            bases=('portfolio.folder',),
        ),
        migrations.CreateModel(
            name='KindergartenFolder',
            fields=[
                ('folder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portfolio.Folder')),
                ('kindergarten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Kindergarten')),
            ],
            bases=('portfolio.folder',),
        ),
        migrations.AddField(
            model_name='report',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Folder'),
        ),
        migrations.AddField(
            model_name='folder',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Employee'),
        ),
    ]
