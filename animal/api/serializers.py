from rest_framework import serializers

from animal.models import (
    Animal,
    AnimalSpecies,
    AnimalBreed,
    AnimalShelter,
    AnimalTransaction,
)

from pharmacy.models import Warehouse


class AnimalSerializer(serializers.ModelSerializer):
    species = serializers.SerializerMethodField()
    breed = serializers.SerializerMethodField()

    class Meta:
        model = Animal
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by")

    def get_species(self, obj):
        return obj.species.name if obj.species else None

    def get_breed(self, obj):
        return obj.breed.name if obj.breed else None


class AnimalSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalSpecies
        fields = "__all__"


class AnimalBreedSerializer(serializers.ModelSerializer):
    # species = AnimalSpeciesSerializer()

    class Meta:
        model = AnimalBreed
        fields = "__all__"


class AnimalShelterSerializer(serializers.ModelSerializer):
    warehouse = serializers.SerializerMethodField()

    class Meta:

        model = AnimalShelter
        fields = "__all__"

    def get_warehouse(self, obj):
        return obj.warehouse.name if obj.warehouse else None


class AnimalTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalTransaction
        fields = "__all__"


# class AnimalShelterListSerializer(serializers.ModelSerializer):
#     animal = AnimalSerializer()

#     class Meta:
#         model = AnimalShelter
#         fields = "__all__"
