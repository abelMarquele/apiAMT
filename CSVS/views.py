from django.shortcuts import render
from .forms import CsvModelForm
from datetime import datetime, date
from dateutil import parser
from .models import Csv
from conductor_sales_report.models import conductor_sales_report
import csv


def upload_file_view(request):
	form = CsvModelForm(request.POST or None, request.FILES or None)
	if form.is_valid(): 	
		form.save()
		form = CsvModelForm()
		obj = Csv.objects.get(activated=False)
		with open(obj.file_name.path, 'r') as f:
			reader = csv.reader(f)
			for i, row in enumerate(reader):
				if i==0:
					pass
				else:
					datetime_obj = parser.parse(row[8])						
					conductor_sales_report.objects.create(
						company_id	= int(row[0]),
						company_name = row[1],	
						device	= row[2],
						conductor_id = int(row[3]),	
						conductor_first_name = row[4],
						conductor_last_name = row[5],
						number	= int(row[6]),
						amount	= row[7],
						date = datetime_obj,
					)
					
			obj.activated = True
			obj.save()
	return render(request, 'upload.html', {'form': form})

