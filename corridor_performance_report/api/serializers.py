from rest_framework import serializers
from corridor_performance_report.models import corridor_performance_report


class corridor_performance_reportSerializer(serializers.ModelSerializer):
    class Meta:
        model = corridor_performance_report
        fields = '__all__'
        # fields = 'date, operator, spz, passenger_count,qr_ticket_count, operator_income'
       # depth = 1
   

