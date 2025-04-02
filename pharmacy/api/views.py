from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


from pharmacy.models import (
    Warehouse,
    Medicine,
    MedicineTransaction,
    MedicineTransactionDetail,
)
from pharmacy.api.serializers import (
    WarehouseSerializers,
    MedicineSerializers,
    MedicineTransactionSerializer,
    MedicineTransactionDetailSerializer,
)


class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "location", "description", "default", "active"]

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user,
        )

    def perform_update(self, serializer):
        serializer.save(
            updated_by=self.request.user,
        )


class MedicineViewSet(ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "active_ingredient", "barcode", "category"]

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user,
        )

    def perform_update(self, serialzer):
        serialzer.save(
            updated_by=self.request.user,
        )


class MedicineTransactionViewSet(ModelViewSet):
    queryset = MedicineTransaction.objects.all()
    serializer_class = MedicineTransactionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["date", "transaction_id", "transaction_label"]

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user,
        )

    def perform_update(self, serialzer):
        serialzer.save(
            updated_by=self.request.user,
        )
