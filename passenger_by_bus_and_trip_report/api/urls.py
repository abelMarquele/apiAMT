from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from passenger_by_bus_and_trip_report.views import passenger_view
#from .views import passenger_by_bus_and_trip_reportViewSet

# router = DefaultRouter()
# router.register('passenger_by_bus_and_trip_report', passenger_by_bus_and_trip_reportViewSet, basename='passenger_by_bus_and_trip_report')

urlpatterns = [
    #url('', include(router.urls)),
    path('passenger/',passenger_view, name='passenger-view'),
]
