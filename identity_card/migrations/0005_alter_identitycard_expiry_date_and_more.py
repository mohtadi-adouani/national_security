# Generated by Django 5.1.3 on 2024-11-29 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity_card', '0004_alter_identitycard_expiry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identitycard',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2034, 11, 26, 16, 23, 44, 425991)),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='number',
            field=models.CharField(default='w4rsKWkTwvk4', max_length=12),
        ),
        migrations.AlterField(
            model_name='passport',
            name='number',
            field=models.CharField(max_length=12),
        ),
    ]
