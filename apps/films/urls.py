from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.films.views import FilmViewSet

router = DefaultRouter()
router.register('', FilmViewSet)


urlpatterns = [
    path('', include(router.urls)),
]