import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class conductorFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date", lookup_expr='gte')
	end_date = DateFilter(field_name="date", lookup_expr='lte')
	conductor_last_name = CharFilter(field_name='conductor_last_name', lookup_expr='icontains')
	conductor_first_name = CharFilter(field_name='conductor_first_name', lookup_expr='icontains')
	company_name = CharFilter(field_name='company_name', lookup_expr='icontains')

	class Meta:
		model = conductor_sales_report
		fields = ['start_date','end_date', 'company_name','conductor_last_name','conductor_first_name']
