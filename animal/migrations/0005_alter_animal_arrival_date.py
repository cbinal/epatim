# Generated by Django 5.1.7 on 2025-03-22 13:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0004_alter_animal_arrival_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='arrival_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
