# Generated by Django 5.1.3 on 2024-12-08 15:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0002_prerequestidc_identity_card'),
        ('identity_card', '0012_identitycard_status_passport_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PreRequestPassport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('sexe', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=50)),
                ('eyes_color', models.IntegerField(choices=[(0, 'Black'), (1, 'Brown'), (2, 'Hazel'), (3, 'Green'), (4, 'Blue'), (5, 'Grey'), (6, 'A')], default=0)),
                ('height', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('P', 'Personal'), ('O', 'Official'), ('D', 'Diplomatic'), ('E', 'Emergency Travel')], default='P', max_length=1)),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('number', models.CharField(blank=True, max_length=12)),
                ('validation', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pre_request_passport_author', to=settings.AUTH_USER_MODEL)),
                ('corrector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pre_request_passport_corrector', to=settings.AUTH_USER_MODEL)),
                ('passport', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='identity_card.passport')),
            ],
        ),
    ]
