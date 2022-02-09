from rest_framework import serializers
from corridor_performance_report.models import corridor_performance_report


class corridor_performance_reportSerializer(serializers.ModelSerializer):
    class Meta:
        model = corridor_performance_report
        fields = '__all__'
        # depth = 1
   

