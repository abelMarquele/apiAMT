from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from conductor_sales_report.views import conductor_view

#from .views import conductor_sales_reportViewSet

# router = DefaultRouter()
# router.register('conductor_sales_report', conductor_sales_reportViewSet, basename='conductor_sales_report')


urlpatterns = [
   # url('', include(router.urls)),
    path('conductor/',conductor_view, name='conductor-view'),
]
