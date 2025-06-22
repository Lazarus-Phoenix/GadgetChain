from django_filters import rest_framework as filters
from .models import Network


class NetworkFilter(filters.FilterSet):
    country = filters.CharFilter(field_name='country', lookup_expr='iexact')

    class Meta:
        model = Network
        fields = ['country']