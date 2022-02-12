import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class settlement_fileFilter(django_filters.FilterSet):
	carrier_name = CharFilter(field_name='carrier_name', lookup_expr='icontains')
	cooperatives = CharFilter(field_name='cooperatives', lookup_expr='icontains')



	class Meta:
		model = settlement_file_operator
		fields = ['cooperatives', 'carrier_name']