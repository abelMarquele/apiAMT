from CSVS.decorators import allowed_users
from conductor_sales_report.filters import conductorFilter
from conductor_sales_report.models import conductor_sales_report

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv

from django.contrib.auth.decorators import login_required


@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def conductor_view(request):
    conductor = conductor_sales_report.objects.all()

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
            obj.file_row=i
            obj.save()
    
    myFilter = conductorFilter(request.GET, queryset=conductor)
    conductor = myFilter.qs 

    context = {'conductor': conductor,'myFilter':myFilter, 'form': form}
    return render(request, 'conductor_sales_report.html', context)

