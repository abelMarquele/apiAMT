from django.conf.urls import url, include
from django.db.models import base
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import corridor_performance_reportViewSet, corridor_performance_reportIDViewSet, corridor_upload_file_view

router = DefaultRouter()
router.register('corridor_performance_report', corridor_performance_reportViewSet, basename='corridor_performance_report')
router.register('corridor_performance_reportID', corridor_performance_reportIDViewSet, basename='corridor_performance_reportID')


urlpatterns = [
    url('', include(router.urls)),
    path('corridor/',corridor_upload_file_view, name='corridor-view'),
]
