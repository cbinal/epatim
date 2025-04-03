from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType


from pharmacy import models


class WarehouseSerializers(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = models.Warehouse
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by")

    def get_content_type(self, obj):
        content_type = ContentType.objects.get_for_model(models.Warehouse)
        return content_type.id


class MedicineSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Medicine
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by")


class MedicineTransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicineTransactionDetail
        # fields = "__all__"
        exclude = ["medicine_transaction"]


class MedicineTransactionSerializer(serializers.ModelSerializer):
    medicine_transaction_detail = MedicineTransactionDetailSerializer(many=True)

    class Meta:
        model = models.MedicineTransaction
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by")

    def create(self, validated_data):
        medicine_transaction_detail = validated_data.pop("medicine_transaction_detail")
        medicine_transaction = models.MedicineTransaction.objects.create(
            **validated_data
        )
        for detail in medicine_transaction_detail:
            models.MedicineTransactionDetail.objects.create(
                medicine_transaction=medicine_transaction, **detail
            )
        return medicine_transaction


class SupplierSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()

    class Meta:
        model = models.Supplier
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by")

    def get_content_type(self, obj):
        content_type = ContentType.objects.get_for_model(models.Supplier)
        return content_type.id
