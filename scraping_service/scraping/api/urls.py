from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('cities', CityViewSet)
router.register('langs', LanguageViewSet)
router.register('vacs', VacancyViewSet)
urlpatterns = router.urls