from django.http import JsonResponse
from CSVS.decorators import allowed_users
from passenger_by_bus_and_trip_report.models import passenger_by_bus_and_trip_report

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv
from django.contrib.auth.decorators import login_required


@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def passenger_view(request):
    passenger = passenger_by_bus_and_trip_report.objects.all()

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
                    device_location1  = row[1].split('-', 1)
                    datetime_obj = parser.parse(row[0]).date()
                    timestamp = parser.parse(row[7]).time() 
                    chout_timestamp = parser.parse(row[9]).time()				
                    passenger_by_bus_and_trip_report.objects.create(
                        timestamp1 = datetime_obj,
                        device_location1 = row[1],
                        line_reg_no1 = int(row[2]),
                        route_reg_no1 = int(row[3]),
                        route_reg_no = int(row[4]),
                        customer_profile_name = row[5],
                        card_uid3 = row[6],
                        timestamp = timestamp,
                        stationfrom_short_name = row[8],
                        chout_timestamp = chout_timestamp,
                        stationto_short_name = row[10],
                        money_value = float(row[11]),
                        transaction_count = int(row[12]),
                        money_value1 = float(row[13]),
                        transaction_count2 = int(row[14]),
                        money_value3 = float(row[15]),
                        bus_nr = int(device_location1[0]),
                        spz =  device_location1[1],
                    )
            obj.activated=True
            obj.file_row=i
            obj.name='Passenger by bus and trip report'
            obj.save()

            if request.is_ajax():
                return JsonResponse({'message': 'A ação foi realizada com sucesso!'})
    
    context = {'passenger': passenger, 'form': form}
    return render(request, 'passenger_by_bus_and_trip_report.html', context)




