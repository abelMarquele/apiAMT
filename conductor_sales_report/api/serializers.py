from rest_framework import serializers
from conductor_sales_report.models import conductor_sales_report


class conductor_sales_reportSerializer(serializers.ModelSerializer):
    class Meta:
        model = conductor_sales_report
        fields = '__all__'
       # depth = 1
   

