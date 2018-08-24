# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-24 08:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import librekids.core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityStreamEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('target_id', models.PositiveIntegerField(null=True)),
                ('verb', models.CharField(max_length=50)),
                ('time_stamp', models.DateTimeField()),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_stream_entry_as_object_type', to='contenttypes.ContentType')),
                ('target_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activity_stream_entry_as_target_type', to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorisedPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address_primary', models.TextField(blank=True)),
                ('address_secondary', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[librekids.core.models.PhoneValidator()])),
                ('work_number', models.CharField(blank=True, max_length=15, validators=[librekids.core.models.PhoneValidator()])),
                ('mobile_number', models.CharField(blank=True, max_length=15, validators=[librekids.core.models.PhoneValidator()])),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('join_date', models.DateField(blank=True, null=True)),
                ('leave_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChildAuthorisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('is_enclosed', models.BooleanField()),
                ('date_start', models.DateField(null=True)),
                ('date_end', models.DateField(null=True)),
                ('authorised_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AuthorisedPerson')),
                ('on_children', models.ManyToManyField(to='core.Child')),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DataIntoAreaRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_id', models.PositiveIntegerField()),
                ('data_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DataArea')),
                ('data_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Kindergarten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[librekids.core.models.PhoneValidator()])),
                ('name', models.CharField(max_length=50)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[librekids.core.models.PhoneValidator()])),
                ('mobile_number', models.CharField(blank=True, max_length=15, validators=[librekids.core.models.PhoneValidator()])),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('description', models.TextField(blank=True)),
            ],
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Profile')),
                ('position', models.CharField(blank=True, max_length=50)),
                ('join_date', models.DateField(blank=True, null=True)),
                ('leave_date', models.DateField(blank=True, null=True)),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisor_of', to='core.Employee')),
            ],
            bases=('core.profile',),
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Profile')),
                ('address_primary', models.TextField(blank=True)),
                ('address_secondary', models.TextField(blank=True)),
                ('work_number', models.CharField(blank=True, max_length=15, validators=[librekids.core.models.PhoneValidator()])),
            ],
            bases=('core.profile',),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classroom',
            name='kindergarten',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='core.Kindergarten'),
        ),
        migrations.AddField(
            model_name='child',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='core.Classroom'),
        ),
        migrations.AddField(
            model_name='kindergarten',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Employee'),
        ),
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Employee'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='educators',
            field=models.ManyToManyField(related_name='classrooms', to='core.Employee'),
        ),
        migrations.AddField(
            model_name='child',
            name='educator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Employee'),
        ),
        migrations.AddField(
            model_name='child',
            name='parents',
            field=models.ManyToManyField(related_name='children', to='core.Parent'),
        ),
    ]
