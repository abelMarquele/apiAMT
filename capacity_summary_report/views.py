from CSVS.decorators import allowed_users

from index_translation.models import Cooperative, Corridor, Routa
from capacity_summary_report.models import capacity_summary_report

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse


@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def capacity_view(request):
    capacity = capacity_summary_report.objects.all()
    form = CsvModelForm(request.POST or None, request.FILES or None)
    
    if form.is_valid(): 	
        form.save()
            
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r',  encoding='utf-8') as f:
            reader = csv.reader(f)
            cells = list(reader)
            inicio = parser.parse(cells[4][1])
            fim = parser.parse(cells[5][1])
            capacity_summary_report.objects.filter(
                        date__range =[inicio, fim]
            ).delete()

            for i in range(len(cells)-1):
                if (i>=0 and i<13):
                    pass	
                else:
                    # print('Linha:',i, 'a', cells[i][2])
                    datetime_obj = parser.parse(cells[i][0])	 				
                    capacity_summary_report.objects.create(
                            date = datetime_obj,
                            corridor = Corridor.objects.get(id=int(cells[i][1])),  
                            line_nr =  Routa.objects.get(id=int(cells[i][2])),  
                            bus_nr = int(cells[i][3]),
                            spz = cells[i][4],
                            no_of_trips = int(cells[i][5]),
                            passenger_count = int(cells[i][6]),
                            total_income = float(cells[i][7]),
                            maxcom_income = float(cells[i][8]),
                            amt_income = float(cells[i][9]),
                            operator_income = float(cells[i][10]),
                            cooperative = Cooperative.objects.get(id=int(cells[i][11])), 
                            operator = cells[i][12]
                    )      
               
               
            obj.activated=True
            obj.file_row=i
            obj.name='Capacity summary report'
            obj.save()
            if request.is_ajax():
                return JsonResponse({'message': 'A ação foi realizada com sucesso!'})

    context = {'capacity': capacity,'form': form}
    return render(request, 'capacity_summary_report.html', context)

