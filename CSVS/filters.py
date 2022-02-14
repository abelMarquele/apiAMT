import django_filters

from corridor_performance_report.models import corridor_performance_report

from .models import *

class csvFilter(django_filters.FilterSet):
	class Meta:
		model = Csv
		fields = [ 'name']

class operator_spzFilter(django_filters.FilterSet):
	class Meta:
		model = corridor_performance_report
		fields = ['cooperative']