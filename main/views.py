from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Car
from .serializers import CarSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from .filters import CarFilterSet
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


@extend_schema_view(
    list=extend_schema(
        summary="Get all cars"
    )
)
class CarModelViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = PageNumberPagination
    page_size = 5
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    search_fields = ['model']
    ordering_fields = ['price', 'year']
    filterset_class = CarFilterSet
