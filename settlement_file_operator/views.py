from CSVS.decorators import allowed_users
from settlement_file_operator.filters import settlement_fileFilter
from settlement_file_operator.models import settlement_file_operator

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv

from django.contrib.auth.decorators import login_required

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def settlement_view(request):
    settlement_file = settlement_file_operator.objects.all()
    
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid(): 	
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i>10:
                    pass
                else:
                    datetime_obj = parser.parse(row[0])						
                    settlement_file_operator.objects.create(
					    date = datetime_obj,
                        corridor = int(row[1]),
                        line_nr = int(row[2]),
                        bus_nr = int(row[3]),
                        spz = row[4],
                        cooperative = int(row[5]),
                        operator = row[6],
                        passenger_count = int(row[7]),
                        luggage_count = int(row[8]),
                        qr_ticket_count = int(row[9]),
                        amount_ticket = float(row[10]),
                        amount_luggage = float(row[11]),
                        maxcom_income = float(row[12]),
                        amt_income = float(row[13]),
                        operator_income = float(row[14]),
                        
                        transaction_type = row[0],
                        money_value = float(row[1]),
                        transaction_count = int(row[2]),
                        money_value4 = float(row[3]),
                        transaction_type2 = int(row[4]),
                        Textbox217 = int(row[5]),
                        Textbox214 = int(row[6]),
                        Textbox218 = int(row[7]), 
                        transaction_count3 = int(row[8]),
                        Textbox74 = float(row[9]),
                        Textbox88 = float(row[10]),
                        transaction_count4 = int(row[11]),
                        Textbox98 = float(row[12]),
                        Textbox100 = float(row[13]),
                        rank = int(row[14]),
                        carrier_name = row[15],
                        cooperatives = row[16],
                        money_value3 = float(row[17]),
                        Textbox220 = float(row[18]),
                        transaction_count2 = float(row[19]),
                        Textbox76 = float(row[20]),
                        Textbox77 = float(row[21]),
                        
					)
					
            obj.activated=True
            obj.file_row=i
            obj.save()

    myFilter = settlement_fileFilter(request.GET, queryset=settlement_file)
    settlement_file = myFilter.qs

    context = {'settlement_file': settlement_file,'myFilter':myFilter, 'form': form}
    return render(request, 'settlement_file_operator.html', context)






