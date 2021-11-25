from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import corridor_performance_reportViewSet

router = DefaultRouter()
router.register('corridor_performance_report', corridor_performance_reportViewSet, basename='corridor_performance_report')

urlpatterns = [
    url('', include(router.urls))
]
