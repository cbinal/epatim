from django.urls import path, include
from rest_framework.routers import DefaultRouter

from animal.api.views import AnimalViewSet

router = DefaultRouter()
router.register("animal", AnimalViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
