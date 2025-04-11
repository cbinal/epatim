from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from collections import defaultdict

from pharmacy.models import Warehouse

from animal.models import (
    Animal,
    AnimalBreed,
    AnimalSpecies,
    AnimalShelter,
    AnimalTransaction,
    Medication,
    MedicationDetail,
    Examination,
)
from animal.api.serializers import (
    AnimalSerializer,
    AnimalBreedSerializer,
    AnimalSpeciesSerializer,
    AnimalShelterSerializer,
    AnimalTransactionSerializer,
    MedicationSerializer,
    MedicationDetailSerializer,
    ExaminationSerializer,
)
from animal.api.filters import AnimalShelterFilter


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        species = self.request.data.get("species")
        breed = self.request.data.get("breed")

        # raise Exception("perform_create metodu çalıştı!")
        print(self.request.user)
        serializer.save(
            species_id=species,
            breed_id=breed,
            created_by=self.request.user,
            updated_by=self.request.user,
        )

    def perform_update(self, serializer):
        print("perform update")
        serializer.save(
            species_id=self.request.data.get("species"),
            breed_id=self.request.data.get("breed"),
            # owner=self.request.data.get("owner"),
            updated_by=self.request.user,
        )


class AnimalSpeciesViewSet(ModelViewSet):
    queryset = AnimalSpecies.objects.all()
    serializer_class = AnimalSpeciesSerializer
    permission_classes = [IsAuthenticated]


class AnimalBreedViewSet(ModelViewSet):
    queryset = AnimalBreed.objects.all()
    serializer_class = AnimalBreedSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["species", "species__name", "name"]
    permission_classes = [IsAuthenticated]


class AnimalBreedsBySpeciesViewSet(ModelViewSet):
    queryset = AnimalBreed.objects.all()
    serializer_class = AnimalBreedSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        all_species = AnimalSpecies.objects.values_list("id", "name")

        breeds = AnimalBreed.objects.values_list(
            "species__id", "species__name", "id", "name"
        )

        species_dict = {
            species_id: {"id": species_id, "species": species_name, "breeds": []}
            for species_id, species_name in all_species
        }

        for species_id, species_name, breed_id, breed_name in breeds:
            species_dict[species_id]["breeds"].append(
                {"id": breed_id, "name": breed_name}
            )

        return Response(list(species_dict.values()))


class AnimalShelterViewSet(ModelViewSet):
    queryset = AnimalShelter.objects.all()
    serializer_class = AnimalShelterSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnimalShelterFilter

    def perform_update(self, serializer):
        print(self.request.data.get("warehouse"))
        serializer.save(
            warehouse=Warehouse.objects.get(id=self.request.data.get("warehouse"))
        )

    def perform_create(self, serializer):
        print(self.request.data.get("warehouse"))
        serializer.save(
            warehouse=Warehouse.objects.get(id=self.request.data.get("warehouse"))
        )


class AnimalTransactionViewSet(ModelViewSet):
    queryset = AnimalTransaction.objects.all()
    serializer_class = AnimalTransactionSerializer
    permission_classes = [IsAuthenticated]


class MedicationDetailViewSet(ModelViewSet):
    queryset = MedicationDetail.objects.all()
    serializer_class = MedicationDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user,
        )

    def perform_update(self, serializer):
        serializer.save(
            updated_by=self.request.user,
        )


class MedicationViewSet(ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["animal"]

    def perform_create(self, serializer):
        print("view create")
        serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user,
        )

    def perform_update(self, serializer):
        serializer.save(
            updated_by=self.request.user,
        )


class ExaminationViewSet(ModelViewSet):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["animal"]

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            updated_by=self.request.user,
        )

    def perform_update(self, serializer):
        serializer.save(
            updated_by=self.request.user,
        )
