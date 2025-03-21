from rest_framework import serializers

from animal.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"
        read_only_fields = ("created_by", "updated_by")
