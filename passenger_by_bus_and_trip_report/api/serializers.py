from rest_framework import serializers
from passenger_by_bus_and_trip_report.models import passenger_by_bus_and_trip_report


class passenger_by_bus_and_trip_reportSerializer(serializers.ModelSerializer):
    class Meta:
        model = passenger_by_bus_and_trip_report
        fields = '__all__'
       # depth = 1
   

