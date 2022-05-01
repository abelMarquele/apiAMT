from django.http import JsonResponse
from CSVS.decorators import allowed_users
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
        with open(obj.file_name.path, 'r',  encoding='utf-8') as f:
            reader = csv.reader(f)
            cells = list(reader)
            inicio = parser.parse(cells[4][1])
            fim = parser.parse(cells[5][1])
            conductor_sales_report.objects.filter(
                        date__range =[inicio, fim]
            ).delete()

            for i in range(len(cells)-1):
                if (i>=0 and i<13):
                    pass	
                else:
                    datetime_obj = parser.parse(cells[i][8])						
                    conductor_sales_report.objects.create(
						company_id	= int(cells[i][0]),
						company_name = cells[i][1],	
						device	= cells[i][2],
						conductor_id = int(cells[i][3]),	
						conductor_first_name = cells[i][4],
						conductor_last_name = cells[i][5],
						number	= int(cells[i][6]),
						amount	= cells[i][7],
						date = datetime_obj,
					)
					
            obj.activated = True
            obj.file_row=i
            obj.nome='Conductor Sales Report'
            obj.save()
    
            if request.is_ajax():
                return JsonResponse({'message': 'A ação foi realizada com sucesso!'})

    context = {'conductor': conductor, 'form': form}
    return render(request, 'conductor_sales_report.html', context)

