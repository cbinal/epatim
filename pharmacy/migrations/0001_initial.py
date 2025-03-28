# Generated by Django 5.1.7 on 2025-03-25 15:01

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('initial_quantity', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='created_medicine_user', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='updated_medicine_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('from_object_id', models.PositiveIntegerField()),
                ('to_object_id', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='created_medicine_transaction_user', to=settings.AUTH_USER_MODEL)),
                ('from_content_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='from_content_type', to='contenttypes.contenttype')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pharmacy.medicine')),
                ('to_content_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='to_content_type', to='contenttypes.contenttype')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='updated_medicine_transaction_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('tax_number', models.CharField(max_length=20)),
                ('tax_office', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='created_supplier_user', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='updated_supplier_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('default', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='created_warehouse_user', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='updated_warehouse_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='medicine',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pharmacy.warehouse'),
        ),
    ]
