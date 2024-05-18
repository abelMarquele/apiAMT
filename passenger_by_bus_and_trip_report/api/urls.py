from django.urls import path
from passenger_by_bus_and_trip_report.views import passenger_view

urlpatterns = [
    path('passenger/',passenger_view, name='passenger-view'),
]
