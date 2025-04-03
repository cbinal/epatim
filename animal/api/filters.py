import django_filters
from animal.models import AnimalShelter


class AnimalShelterFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
