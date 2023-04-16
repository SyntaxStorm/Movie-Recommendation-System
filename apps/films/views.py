from django.shortcuts import render
import django_filters
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from apps.films.models import Film, Tag
from apps.films.serializers import FilmSerializer

User = get_user_model()


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100000


class FilmFilter(django_filters.FilterSet):
    tags = django_filters.ModelChoiceFilter(queryset=Tag.objects.all(), field_name='tags')

    class Meta:
        model = Film
        fields = ['tags', 'release_year',]


class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_class = FilmFilter
    pagination_class = LargeResultsSetPagination
    search_fields = ['tags__name', 'title']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]