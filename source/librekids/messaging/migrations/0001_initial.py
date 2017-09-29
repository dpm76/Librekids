# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 12:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_text', models.TextField()),
                ('creation_time', models.DateTimeField()),
                ('delivery_time', models.DateTimeField(null=True)),
                ('is_draft', models.BooleanField()),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent_message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='messaging.Message')),
            ],
        ),
        migrations.CreateModel(
            name='MessageDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField()),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messaging.Message')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]