from rest_framework import serializers
from capacity_summary_report.models import capacity_summary_report


class capacity_summary_reportSerializer(serializers.ModelSerializer):
    class Meta:
        model = capacity_summary_report
        fields = '__all__'
       # depth = 1
   

