from rest_framework import serializers


from pharmacy import models


class WarehouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Warehouse
        fields = "__all__"
