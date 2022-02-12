from CSVS.decorators import allowed_users
from corridor_performance_report.filters import corridorFilter
from index_translation.models import Cooperative, Corridor, Routa
from corridor_performance_report.models import corridor_performance_report

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv

from django.contrib.auth.decorators import login_required


@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def corridor_view(request):
    corridor = corridor_performance_report.objects.all()

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
                    corridor_performance_report.objects.create(
                        date = datetime_obj,
                        corridor = Corridor.objects.get(id=int(row[1])),
                        line_nr = Routa.objects.get(id=int(row[2])),
                        bus_nr = int(row[3]),
                        spz = row[4],
                        cooperative = Cooperative.objects.get(id=int(row[5])), 
                        operator = row[6],
                        passenger_count = int(row[7]),
                        luggage_count = int(row[8]),
                        qr_ticket_count = int(row[9]),
                        amount_ticket = float(row[10]),
                        amount_luggage = float(row[11]),
                        maxcom_income = float(row[12]),
                        amt_income = float(row[13]),
                        operator_income = float(row[14]),
                    )
            obj.activated=True
            obj.file_row=i
            obj.nome='Corridor performance report'
            obj.save()

    myFilter = corridorFilter(request.GET, queryset=corridor)
    corridor = myFilter.qs 
            
    context = {'corridor': corridor,'myFilter':myFilter, 'form': form}
    return render(request, 'corridor_performance_report.html', context)



