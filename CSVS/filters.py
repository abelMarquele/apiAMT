import django_filters

from .models import *

class csvFilter(django_filters.FilterSet):
	class Meta:
		model = Csv
		fields = [ 'name']