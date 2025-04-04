from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pharmacy.api.views import (
    WarehouseViewSet,
    MedicineViewSet,
    MedicineTransactionViewSet,
    MedicineTransactionDetailViewSet,
    MedicineTransactionVViewSet,
    SupplierViewSet,
    ContentTypeViewSet,
)


router = DefaultRouter()

router.register("warehouse", WarehouseViewSet, basename="warehouse")
router.register("medicine", MedicineViewSet, basename="medicine")
router.register(
    "medicine_transaction", MedicineTransactionViewSet, basename="medicine_transaction"
)
router.register(
    "medicine_transaction_detail",
    MedicineTransactionDetailViewSet,
    basename="medicine_transaction_detail",
)
router.register("supplier", SupplierViewSet, basename="supplier")
router.register(
    "medicine_transaction_v",
    MedicineTransactionVViewSet,
    basename="medicine_transaction_v",
)
router.register("content_type", ContentTypeViewSet, basename="content_type")

urlpatterns = [
    path("", include(router.urls)),
]
