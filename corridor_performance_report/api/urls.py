from django.conf.urls import url, include
from django.db.models import base
from django.urls import path
from rest_framework.routers import DefaultRouter

from corridor_performance_report.views import corridor_view
from .views import corridor_performance_reportViewSet, corridor_performance_reportIDViewSet

router = DefaultRouter()
router.register('corridor_performance_report', corridor_performance_reportViewSet, basename='corridor_performance_report')
router.register('corridor_performance_reportID', corridor_performance_reportIDViewSet, basename='corridor_performance_reportID')


urlpatterns = [
    url('', include(router.urls)),
    path('corridor/',corridor_view, name='corridor-view'),
]
