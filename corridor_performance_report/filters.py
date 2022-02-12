import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class corridorFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	cooperative = CharFilter(field_name='cooperative', lookup_expr='icontains')
	operator = CharFilter(field_name='operator', lookup_expr='icontains')
	spz = CharFilter(field_name='spz', lookup_expr='icontains')

	class Meta:
		model = corridor_performance_report
		fields = ['start_date','end_date', 'corridor','line_nr','cooperative','operator','spz']
