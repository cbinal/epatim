from django.urls import path, include
from rest_framework.routers import DefaultRouter

from animal.api.views import (
    AnimalViewSet,
    AnimalBreedViewSet,
    AnimalSpeciesViewSet,
    AnimalBreedsBySpeciesViewSet,
    AnimalShelterViewSet,
    AnimalTransactionViewSet,
    MedicationViewSet,
    ExaminationViewSet,
)


router = DefaultRouter()
router.register("animal", AnimalViewSet)
router.register("animal_breed", AnimalBreedViewSet)
router.register("animal_species", AnimalSpeciesViewSet)
router.register(
    "breeds_by_species", AnimalBreedsBySpeciesViewSet, basename="breeds_by_species"
)
router.register("animal_shelter", AnimalShelterViewSet, basename="animal_shelter")
router.register("animal_transaction", AnimalTransactionViewSet)
router.register("medication", MedicationViewSet, basename="medication")
router.register("examination", ExaminationViewSet, basename="examination")


urlpatterns = [
    path("", include(router.urls)),
]
