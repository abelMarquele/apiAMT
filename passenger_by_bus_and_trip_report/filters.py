import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class passengerFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="timestamp1", lookup_expr='gte')
	end_date = DateFilter(field_name="timestamp1", lookup_expr='lte')
	line_reg_no1 = CharFilter(field_name='line_reg_no1', lookup_expr='icontains')
	spz = CharFilter(field_name='spz', lookup_expr='icontains')
	customer_profile_name = CharFilter(field_name='customer_profile_name', lookup_expr='icontains')

	class Meta:
		model = passenger_by_bus_and_trip_report
		fields = ['start_date','end_date', 'line_reg_no1','spz','customer_profile_name']
