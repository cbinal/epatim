from rest_framework import serializers


from pharmacy import models


class WarehouseSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Warehouse
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by")


class MedicineSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Medicine
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by")
