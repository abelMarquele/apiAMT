from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import conductor_sales_reportViewSet, conductor_upload_file_view

router = DefaultRouter()
router.register('conductor_sales_report', conductor_sales_reportViewSet, basename='conductor_sales_report')


urlpatterns = [
    url('', include(router.urls)),
    path('conductor/',conductor_upload_file_view, name='conductor-view'),
]
