import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class capacityFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	operator = CharFilter(field_name='operator', lookup_expr='icontains')
	spz = CharFilter(field_name='spz', lookup_expr='icontains')


	class Meta:
		model = capacity_summary_report
		fields = ['start_date','end_date', 'corridor', 'cooperative','operator','spz']
		#fields = '__all__'
		#exclude = ['customer', 'date_created']