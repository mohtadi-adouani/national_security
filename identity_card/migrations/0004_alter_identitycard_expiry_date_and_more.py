# Generated by Django 5.1.3 on 2024-11-28 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity_card', '0003_passport_alter_identitycard_expiry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identitycard',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2034, 11, 25, 17, 42, 13, 255870)),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='number',
            field=models.CharField(default='2ERd9a6p4F56', max_length=12),
        ),
        migrations.AlterField(
            model_name='passport',
            name='eyes_color',
            field=models.IntegerField(choices=[(0, 'Black'), (1, 'Brown'), (2, 'Hazel'), (3, 'Green'), (4, 'Blue'), (5, 'Grey'), (6, 'A')], default=0),
        ),
        migrations.AlterField(
            model_name='passport',
            name='number',
            field=models.CharField(default='JxqNKlMEoyou', max_length=12),
        ),
    ]
