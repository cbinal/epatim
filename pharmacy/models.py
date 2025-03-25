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

    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT)

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

    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.RESTRICT)
    description = models.TextField()
    initial_quantity = models.PositiveIntegerField()

    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MedicineTransaction(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    date = models.DateTimeField(default=now)
    from_content_type = models.ForeignKey(
        ContentType, on_delete=models.RESTRICT, related_name="from_content_type"
    )
    from_where = GenericForeignKey("from_content_type", "from_object_id")
    to_content_type = models.ForeignKey(
        ContentType, on_delete=models.RESTRICT, related_name="to_content_type"
    )
    to_where = GenericForeignKey("to_content_type", "to_object_id")
    description = models.TextField()

    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    updated_by = models.ForeignKey(User, on_delete=models.RESTRICT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} adet {self.medicine.name}, {self.from_where} -> {self.to_where}"
