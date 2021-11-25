from rest_framework import serializers
from settlement_file_operator.models import settlement_file_operator


class settlement_file_operatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = settlement_file_operator
        fields = '__all__'
       # depth = 1
   

