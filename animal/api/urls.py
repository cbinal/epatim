from django.urls import path, include
from rest_framework.routers import DefaultRouter

from animal.api.views import (
    AnimalViewSet,
    AnimalBreedViewSet,
    AnimalSpeciesViewSet,
    AnimalBreedsBySpeciesViewSet,
)


router = DefaultRouter()
router.register("animal", AnimalViewSet)
router.register("animal_breed", AnimalBreedViewSet)
router.register("animal_species", AnimalSpeciesViewSet)
router.register(
    "breeds_by_species", AnimalBreedsBySpeciesViewSet, basename="breeds_by_species"
)

urlpatterns = [
    path("", include(router.urls)),
]
