from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import capacity_summary_reportViewSet

router = DefaultRouter()
router.register('capacity_summary_report', capacity_summary_reportViewSet, basename='capacity_summary_report')

urlpatterns = [
    url('', include(router.urls))
]
