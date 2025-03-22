from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from collections import defaultdict

from animal.models import Animal, AnimalBreed, AnimalSpecies
from animal.api.serializers import (
    AnimalSerializer,
    AnimalBreedSerializer,
    AnimalSpeciesSerializer,
)


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # raise Exception("perform_create metodu çalıştı!")
        print(self.request.user)
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.id)


class AnimalSpeciesViewSet(ModelViewSet):
    queryset = AnimalSpecies.objects.all()
    serializer_class = AnimalSpeciesSerializer
    permission_classes = [IsAuthenticated]


class AnimalBreedViewSet(ModelViewSet):
    queryset = AnimalBreed.objects.all()
    serializer_class = AnimalBreedSerializer
    permission_classes = [IsAuthenticated]


class AnimalBreedsBySpeciesViewSet(ModelViewSet):
    queryset = AnimalBreed.objects.all()
    serializer_class = AnimalBreedSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        breeds = AnimalBreed.objects.values_list("species__name", "name")

        species_dict = defaultdict(list)
        for species, breed in breeds:
            species_dict[species].append(breed)

        formatted_data = [
            {"species": key, "breeds": value} for key, value in species_dict.items()
        ]

        return Response(formatted_data)
