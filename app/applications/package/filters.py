import django_filters
from .models import Package


class CustomPackageFilter(django_filters.FilterSet):
    has_delivery_cost = django_filters.BooleanFilter(
        field_name='delivery',
        lookup_expr='exact',
        exclude=True,
    )

    type = django_filters.CharFilter(
        field_name='type__name',
        lookup_expr='exact',
    )

    class Meta:
        model = Package
        fields = ['has_delivery_cost', 'type']
