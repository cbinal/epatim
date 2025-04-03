import django_filters
from pharmacy.models import Supplier


class SupplierFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    address = django_filters.CharFilter(lookup_expr="icontains")
    phone = django_filters.CharFilter(lookup_expr="icontains")
    email = django_filters.CharFilter(lookup_expr="icontains")
    tax_number = django_filters.CharFilter(lookup_expr="icontains")
    tax_office = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Supplier
        fields = ["name", "address", "phone", "email", "tax_number", "tax_office"]
