# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='static/images/space-th-sm.jpg', upload_to='static/images/avatar'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='Palo Alto', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(max_length=140, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AddField(
            model_name='user',
            name='receive_updates',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default='CA', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='street',
            field=models.CharField(default='555 Bailey Ave', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(default='eater', max_length=10, choices=[('cook', 'Cook'), ('eater', 'Eater')]),
        ),
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.CharField(default='94087', max_length=6),
            preserve_default=False,
        ),
    ]
