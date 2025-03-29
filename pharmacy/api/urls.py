from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pharmacy.api.views import WarehouseViewSet


router = DefaultRouter()

router.register("warehouse", WarehouseViewSet, basename="warehouse")


urlpatterns = [
    path("", include(router.urls)),
]
