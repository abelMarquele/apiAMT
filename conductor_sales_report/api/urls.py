from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import conductor_sales_reportViewSet

router = DefaultRouter()
router.register('conductor_sales_report', conductor_sales_reportViewSet, basename='conductor_sales_report')

urlpatterns = [
    url('', include(router.urls))
]
