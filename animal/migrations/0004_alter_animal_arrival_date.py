# Generated by Django 5.1.7 on 2025-03-22 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0003_animal_arrival_date_animal_surrender_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='arrival_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 22, 12, 56, 56, 117905, tzinfo=datetime.timezone.utc)),
        ),
    ]
