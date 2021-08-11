import datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from scraping.models import City, Language, Vacancy
from .serializers import *

period = datetime.date.today() - datetime.timedelta(1)


class DateFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        city_slug = request.query_params.get('city', None)
        lang_slug = request.query_params.get('language', None)
        return queryset.filter(city__slug=city_slug, language__slug=lang_slug, timestamp__gte=period)


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class VacancyViewSet(ModelViewSet):
    """
    ?city=moskvа&language=python
    """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend, DateFilterBackend]
    filterset_fields = ['city__slug', 'language__slug']


    # def get_queryset(self):
    #     city_slug = self.request.query_params.get('city', None)
    #     lang_slug = self.request.query_params.get('language', None)
    #     qs = None
    #     if city_slug and lang_slug:
    #         qs = Vacancy.objects.filter(city__slug=city_slug, language__slug=lang_slug, timestamp__gte=period)
    #     self.queryset = qs
    #     return self.queryset



    # def get_queryset(self):
    #     city_slug = self.request.query_params.get('city', None)
    #     lang_slug = self.request.query_params.get('language', None)
    #     qs = None
    #     if city_slug and lang_slug:
    #         city = City.objects.filter(slug=city_slug).first()
    #         lang = Language.objects.filter(slug=lang_slug).first()
    #         if city and lang:
    #             qs = Vacancy.objects.filter(city=city, language=lang, timestamp__gte=period)
    #     self.queryset = qs
    #     return self.queryset




