from CSVS.decorators import allowed_users

from index_translation.models import Cooperative, Corridor, Routa
from capacity_summary_report.models import capacity_summary_report

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv

from django.contrib.auth.decorators import login_required

from .filters import capacityFilter



@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def capacity_view(request):
    capacity = capacity_summary_report.objects.all()

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
                    datetime_obj = parser.parse(row[0])	
                    print(datetime_obj)					
                    capacity_summary_report.objects.create(
                        date = datetime_obj,
                        corridor = Corridor.objects.get(id=int(row[1])),  
                        line_nr =  Routa.objects.get(id=int(row[2])),  
                        bus_nr = int(row[3]),
                        spz = row[4],
                        no_of_trips = int(row[5]),
                        passenger_count = int(row[6]),
                        total_income = float(row[7]),
                        maxcom_income = float(row[8]),
                        amt_income = float(row[9]),
                        operator_income = float(row[10]),
                        cooperative = Cooperative.objects.get(id=int(row[11])), 
                        operator = row[12]
                    )
            obj.activated=True
            obj.file_row=i
            obj.nome='Capacity summary report'
            obj.save()

    myFilter = capacityFilter(request.GET, queryset=capacity)
    capacity = myFilter.qs 

    context = {'capacity': capacity, 'myFilter':myFilter, 'form': form}
    return render(request, 'capacity_summary_report.html', context)

