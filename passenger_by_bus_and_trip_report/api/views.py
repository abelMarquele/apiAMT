from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import passenger_by_bus_and_trip_reportSerializer
from passenger_by_bus_and_trip_report.models import passenger_by_bus_and_trip_report

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv
from django.contrib.auth.decorators import login_required

# class passenger_by_bus_and_trip_reportViewSet(viewsets.ModelViewSet):
#     serializer_class = passenger_by_bus_and_trip_report
    
#     def get_queryset(self):
#         passenger = passenger_by_bus_and_trip_report.objects.all()
#         return passenger

#     def destroy(self, request, *args, **kwargs):
#         logedin_user = request.user
#         if(logedin_user == "admin"):
#             passenger = self.get_object()
#             passenger.delete()
#             response_message = {"message": "Passenger by bus and trip report foi removido com sucesso!"}
#         else:
#             response_message = {"message": "Não tens permissão para executar essa ação"}

#         return Response(response_message)

#     def create(self, request, *args, **kwargs):
#         passenger_data = request.data

#         new_passenger = passenger_by_bus_and_trip_report.objects.create(
#                     pergunta=Pergunta.objects.get(id=passenger_data["pergunta"]), 
#                     resposta=passenger_data["resposta"]
                    
#                     # timestamp1 = 
#                     # device_location1 = 
#                     # line_reg_no1 = 
#                     # route_reg_no1 = 
#                     # route_reg_no = 
#                     # customer_profile_name = 
#                     # card_uid3 = 
#                     # timestamp = 
#                     # stationfrom_short_name = 
#                     # chout_timestamp = 
#                     # stationto_short_name = 
#                     # money_value = 
#                     # transaction_count = 
#                     # money_value1 = 
#                     # transaction_count2 = 
#                     # money_value3 = 
#                     # bus_nr = 
#                     # spz = 
#             )
#         new_passenger.save()

#         serializer = passenger_by_bus_and_trip_reportSerializer(new_passenger)
#         return Response(serializer.data)

#     def update(self, request, *args, **kwargs):
#         passenger_data = self.get_object()
#         data = request.data

#         pergunta = Pergunta.objects.get(id=data["pergunta"])
#         passenger_data.pergunta = pergunta
#         passenger_data.resposta = data["resposta"]

#         passenger_data.save()

#         serializer = passenger_by_bus_and_trip_reportSerializer(passenger_data)
#         return Response(serializer.data)

#     def partial_update(self, request, *args, **kwargs):
#         passenger_object = self.get_object()
#         data = request.data

#         try:
#             pergunta = Pergunta.objects.get(id=data["pergunta"])
#             passenger_object.pergunta = pergunta
#         except KeyError:
#             pass

#         passenger_object.resposta = data.get("resposta", passenger_object.resposta)

#         passenger_object.save()

#         serializer = passenger_by_bus_and_trip_reportSerializer(passenger_object)
#         return Response(serializer.data)


@login_required(login_url='csvs:login-view')
def passenger_upload_file_view(request):
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
            obj.activated = True
            obj.save()
    return render(request, 'passenger_by_bus_and_trip_report.html', {'form': form})




