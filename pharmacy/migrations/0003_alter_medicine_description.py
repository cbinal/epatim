# Generated by Django 5.1.7 on 2025-03-31 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_remove_medicine_warehouse_medicine_active_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
