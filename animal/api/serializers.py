from rest_framework import serializers

from animal.models import Animal, AnimalSpecies, AnimalBreed


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
