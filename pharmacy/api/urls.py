from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pharmacy.api.views import (
    WarehouseViewSet,
    MedicineViewSet,
    MedicineTransactionViewSet,
    SupplierViewSet,
)


router = DefaultRouter()

router.register("warehouse", WarehouseViewSet, basename="warehouse")
router.register("medicine", MedicineViewSet, basename="medicine")
router.register(
    "medicine_transaction", MedicineTransactionViewSet, basename="medicine_transaction"
)
router.register("supplier", SupplierViewSet, basename="supplier")


urlpatterns = [
    path("", include(router.urls)),
]
