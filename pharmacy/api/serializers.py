from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum

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
    stock_balance = serializers.SerializerMethodField()

    class Meta:
        model = models.Medicine
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by")

    def get_stock_balance(self, obj):
        # MedicineTransactionDetail üzerinden tüm hareketleri al
        print(obj.id)
        all_details = models.MedicineTransactionDetail.objects.filter(
            medicine=obj.id
        ).select_related(
            "medicine_transaction__to_content_type",
            "medicine_transaction__from_content_type",
        )

        total_in = 0
        total_out = 0

        for detail in all_details:
            trx = detail.medicine_transaction

            print(trx.to_content_type.model)
            print(trx.from_content_type.model)
            # Giriş mi? (ilaç 'to' alanına gidiyorsa ve gittiği yer depo gibi bir yerse)
            if trx.to_content_type.model not in ["animal", "supplier"]:
                total_in += detail.quantity

            # Çıkış mı? (ilaç 'from' alanından çıkıyorsa ve çıktığı yer depo gibi bir yerse)
            if trx.to_content_type.model in ["animal", "supplier"]:
                total_out += detail.quantity

        return total_in - total_out


class MedicineTransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicineTransactionDetail
        # fields = "__all__"
        exclude = ["medicine_transaction"]


class MedicineTransactionSerializer(serializers.ModelSerializer):
    transaction_detail = MedicineTransactionDetailSerializer(many=True)

    class Meta:
        model = models.MedicineTransaction
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by")

    def create(self, validated_data):
        transaction_detail = validated_data.pop("transaction_detail")
        medicine_transaction = models.MedicineTransaction.objects.create(
            **validated_data
        )
        for detail in transaction_detail:
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


class MedicineTransactionDetailVSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source="medicine.name")
    medicine_id = serializers.IntegerField(source="medicine.id")

    class Meta:
        model = models.MedicineTransactionDetail
        fields = [
            "id",
            "medicine_id",
            "medicine_name",
            "quantity",
            "expiration_date",
        ]


class MedicineTransactionVSerializer(serializers.ModelSerializer):
    from_where_name = serializers.SerializerMethodField()
    to_where_name = serializers.SerializerMethodField()
    from_object_name = serializers.SerializerMethodField()
    to_object_name = serializers.SerializerMethodField()
    created_by = serializers.CharField(
        source="created_by.username"
    )  # Kullanıcı adını almak için
    updated_by = serializers.CharField(
        source="updated_by.username"
    )  # Kullanıcı adını almak için
    transaction_detail = MedicineTransactionDetailVSerializer(many=True, read_only=True)

    class Meta:
        model = models.MedicineTransaction
        fields = [
            "id",
            "date",
            "transaction_id",
            "transaction_label",
            "from_content_type",
            "from_where_name",
            "from_object_id",
            "from_object_name",
            "to_content_type",
            "to_where_name",
            "to_object_id",
            "to_object_name",
            "description",
            "created_by",
            "updated_by",
            "created_at",
            "updated_at",
            "transaction_detail",
        ]

    def get_from_where_name(self, obj):
        """from_where alanını model ismi olarak döndür"""
        # return ContentType.objects.get_for_model(obj.from_content_type.model).name

        table = obj.from_content_type.model if obj.from_content_type else None
        translated_table = None
        if table:
            if table == "supplier":
                translated_table = "Tedarikçi"
            elif table == "warehouse":
                translated_table = "Depo"

        return translated_table

    def get_to_where_name(self, obj):
        """to_where alanını model ismi olarak döndür"""
        table = obj.to_content_type.model if obj.to_content_type else None
        translated_table = None
        if table:
            if table == "supplier":
                translated_table = "Tedarikçi"
            elif table == "warehouse":
                translated_table = "Depo"

        return translated_table

    def get_to_object_name(self, obj):
        return str(obj.to_where) if obj.to_where else None

    def get_from_object_name(self, obj):
        return str(obj.from_where) if obj.from_where else None


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ["id", "name"]
