from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


from pharmacy.models import Pharmacy
from pharmacy.api.serializers import PharmacySerializer


class PharmacyViewSet(ModelViewSet):
    object = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    permission_classes = [IsAuthenticated]
