from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pharmacy.api.views import WarehouseViewSet, MedicineViewSet


router = DefaultRouter()

router.register("warehouse", WarehouseViewSet, basename="warehouse")
router.register("medicine", MedicineViewSet, basename="medicine")

urlpatterns = [
    path("", include(router.urls)),
]
