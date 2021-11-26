from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import capacity_summary_reportViewSet, capacity_upload_file_view

router = DefaultRouter()
router.register('capacity_summary_report', capacity_summary_reportViewSet, basename='capacity_summary_report')

urlpatterns = [
    url('', include(router.urls)),
    path('capacity/',capacity_upload_file_view, name='capacity-view'),
]

