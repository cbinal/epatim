# Generated by Django 5.1.7 on 2025-04-02 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0005_remove_medicinetransaction_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinetransactiondetail',
            name='medicine_transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='medicine_transaction_detail', to='pharmacy.medicinetransaction'),
        ),
    ]
