from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import passenger_by_bus_and_trip_reportViewSet

router = DefaultRouter()
router.register('passenger_by_bus_and_trip_report', passenger_by_bus_and_trip_reportViewSet, basename='passenger_by_bus_and_trip_report')

urlpatterns = [
    url('', include(router.urls))
]
