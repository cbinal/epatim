from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils.timezone import now


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()
    default = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    created_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="created_warehouse_user"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="updated_warehouse_user"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    tax_number = models.CharField(max_length=20)
    tax_office = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    created_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="created_supplier_user"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="updated_supplier_user"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    active_ingredient = models.CharField(
        max_length=100, blank=True, null=True
    )  # Etken madde
    barcode = models.CharField(max_length=50, default="")
    category = models.CharField(
        max_length=100, blank=True, null=True
    )  # Antibiyotik, Ağrı kesici
    usage_purpose = models.TextField(blank=True, null=True)  # Kullanım amacı
    storage_conditions = models.TextField(blank=True, null=True)  # Saklama koşulları
    description = models.TextField(blank=True, null=True)
    initial_quantity = models.PositiveIntegerField()

    created_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="created_medicine_user"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="updated_medicine_user"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MedicineTransaction(models.Model):
    date = models.DateTimeField(default=now)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    transaction_label = models.CharField(max_length=100, blank=True, null=True)
    from_content_type = models.ForeignKey(
        ContentType, on_delete=models.RESTRICT, related_name="from_content_type"
    )
    from_object_id = models.PositiveIntegerField()
    from_where = GenericForeignKey("from_content_type", "from_object_id")
    to_content_type = models.ForeignKey(
        ContentType, on_delete=models.RESTRICT, related_name="to_content_type"
    )
    to_object_id = models.PositiveIntegerField()
    to_where = GenericForeignKey("to_content_type", "to_object_id")
    description = models.TextField()

    created_by = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name="created_medicine_transaction_user",
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name="updated_medicine_transaction_user",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} adet {self.medicine.name}, {self.from_where} -> {self.to_where}"


class MedicineTransactionDetail(models.Model):
    medicine_transaction = models.ForeignKey(
        MedicineTransaction, on_delete=models.RESTRICT
    )
    medicine = models.ForeignKey(Medicine, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    expiration_date = models.DateField(blank=True, null=True)
