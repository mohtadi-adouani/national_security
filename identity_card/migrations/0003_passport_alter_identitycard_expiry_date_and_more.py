# Generated by Django 5.1.3 on 2024-11-28 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity_card', '0002_identitycard_sexe_alter_identitycard_expiry_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('number', models.CharField(default='n2jUwWtVCrV7', max_length=12)),
                ('sexe', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=50)),
                ('eyes_color', models.CharField(choices=[(0, 'Black'), (1, 'Brown'), (2, 'Hazel'), (3, 'Green'), (4, 'Blue'), (5, 'Grey'), (6, 'A')], default=0, max_length=1)),
                ('height', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('P', 'Personal'), ('O', 'Official'), ('D', 'Diplomatic'), ('E', 'Emergency Travel')], default='P', max_length=1)),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2034, 11, 25, 17, 33, 41, 758196)),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='number',
            field=models.CharField(default='I1O0cXwBjolu', max_length=12),
        ),
        migrations.AlterField(
            model_name='identitycard',
            name='sexe',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1),
        ),
    ]