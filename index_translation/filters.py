import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class routaFilter(django_filters.FilterSet):
	routa = CharFilter(field_name='routa', lookup_expr='icontains')
	via = CharFilter(field_name='via', lookup_expr='icontains')
	corridor = CharFilter(field_name='corridor', lookup_expr='icontains')


	class Meta:
		model = Routa
		fields = [ 'routa', 'via','corridor']

class cooperativeFilter(django_filters.FilterSet):
	cooperative = CharFilter(field_name='cooperative', lookup_expr='icontains')


	class Meta:
		model = Cooperative
		fields = [ 'cooperative']

class corridorFilter(django_filters.FilterSet):
	corridor = CharFilter(field_name='corridor', lookup_expr='icontains')


	class Meta:
		model = Corridor
		fields = [ 'corridor']