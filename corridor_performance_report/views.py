from django.http import JsonResponse
from CSVS.decorators import allowed_users
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
        with open(obj.file_name.path, 'r',  encoding='utf-8') as f:
            reader = csv.reader(f)
            cells = list(reader)
            inicio = parser.parse(cells[4][1])
            fim = parser.parse(cells[5][1])
            print('Inicio :', inicio)
            print('Fim :', fim) 
            corridor_performance_report.objects.filter(
                        date__range =[inicio, fim]
            ).delete()
            for i in range(len(cells)-1):
                if (i>=0 and i<13):
                    pass	
                else:
                    datetime_obj = parser.parse(cells[i][0])						
                    corridor_performance_report.objects.create(
                        date = datetime_obj,
                        corridor = Corridor.objects.get(id=int(cells[i][1])),
                        line_nr = Routa.objects.get(id=int(cells[i][2])),
                        bus_nr = int(cells[i][3]),
                        spz = cells[i][4],
                        cooperative = Cooperative.objects.get(id=int(cells[i][5])), 
                        operator = cells[i][6],
                        passenger_count = int(cells[i][7]),
                        luggage_count = int(cells[i][8]),
                        qr_ticket_count = int(cells[i][9]),
                        amount_ticket = float(cells[i][10]),
                        amount_luggage = float(cells[i][11]),
                        maxcom_income = float(cells[i][12]),
                        amt_income = float(cells[i][13]),
                        operator_income = float(cells[i][14]),
                    )
            obj.activated=True
            obj.file_row=i
            obj.nome='Corridor performance report'
            obj.save()

            if request.is_ajax():
                return JsonResponse({'message': 'A ação foi realizada com sucesso!'})
            
    context = {'corridor': corridor, 'form': form}
    return render(request, 'corridor_performance_report.html', context)



