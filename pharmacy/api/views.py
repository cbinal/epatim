from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


from pharmacy.models import Warehouse
from pharmacy.api.serializers import WarehouseSerializers


class WarehouseViewSet(ModelViewSet):
    object = Warehouse.objects.all()
    serializer_class = WarehouseSerializers
    permission_classes = [IsAuthenticated]
