from attr import fields
from rest_framework import serializers
from corridor_performance_report.models import corridor_performance_report

    

class corridor_performance_reportSerializer(serializers.ModelSerializer):

    class Meta:
        model = corridor_performance_report
        fields = ['date','operator','spz_1','passenger_count','qr_ticket_count','amount_ticket','operator_income','line_nr_1']
        # fields = '__all__'
        # depth = 1

   

