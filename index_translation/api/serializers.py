from rest_framework import serializers
from index_translation.models import Cooperative, Corridor, Routa


class cooperativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooperative
        fields = '__all__'

class corridorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corridor
        fields = '__all__'

class routaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routa
        fields = '__all__'
   

