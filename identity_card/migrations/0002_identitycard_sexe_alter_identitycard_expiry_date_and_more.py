# Generated by Django 5.1.3 on 2024-11-27 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity_card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='identitycard',
            name='sexe',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2034, 11, 24, 19, 40, 15, 795760)),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='number',
            field=models.CharField(default='PPCulkEas0HU', max_length=12),
        ),
    ]
