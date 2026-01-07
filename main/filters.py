from django_filters.rest_framework import FilterSet
from django_filters import NumberFilter
from .models import Car

class CarFilterSet(FilterSet):
    class Meta:
        model = Car
        fields = ['brand', 'color', 'is_new']