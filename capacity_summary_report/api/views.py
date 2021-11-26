from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import capacity_summary_reportSerializer
from capacity_summary_report.models import capacity_summary_report

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv


class capacity_summary_reportViewSet(viewsets.ModelViewSet):
    serializer_class = capacity_summary_report
    
    def get_queryset(self):
        capacity = capacity_summary_report.objects.all()
        return capacity

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            capacity = self.get_object()
            capacity.delete()
            response_message = {"message": "Capacity Summary Report foi removido com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa ação"}

        return Response(response_message)

    def create(self, request, *args, **kwargs):
        capacity_data = request.data

        new_capacity = capacity_summary_report.objects.create(
                    pergunta=Pergunta.objects.get(id=capacity_data["pergunta"]), 
                    resposta=capacity_data["resposta"]
                    # date = 
                    # corridor = 
                    # line_nr = 
                    # bus_nr = 
                    # spz = 
                    # no_of_trips = 
                    # passenger_count = 
                    # total_income = 
                    # maxcom_income = 
                    # amt_income = 
                    # operator_income = 
                    # cooperative = 
                    # operator = 
        )
        new_capacity.save()

        serializer = capacity_summary_reportSerializer(new_capacity)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        capacity_data = self.get_object()
        data = request.data

        pergunta = Pergunta.objects.get(id=data["pergunta"])
        capacity_data.pergunta = pergunta
        capacity_data.resposta = data["resposta"]

        capacity_data.save()

        serializer = capacity_summary_reportSerializer(capacity_data)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        capacity_object = self.get_object()
        data = request.data

        try:
            pergunta = Pergunta.objects.get(id=data["pergunta"])
            capacity_object.pergunta = pergunta
        except KeyError:
            pass

        capacity_object.resposta = data.get("resposta", capacity_object.resposta)

        capacity_object.save()

        serializer = capacity_summary_reportSerializer(capacity_object)
        return Response(serializer.data)


def capacity_upload_file_view(request):
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
					capacity_summary_report.objects.create(
						date = datetime_obj,
                        corridor = int(row[1]),
                        line_nr = int(row[2]),
                        bus_nr = int(row[3]),
                        spz = row[4],
                        no_of_trips = int(row[5]),
                        passenger_count = int(row[6]),
                        total_income = float(row[7]),
                        maxcom_income = float(row[8]),
                        amt_income = float(row[9]),
                        operator_income = float(row[10]),
                        cooperative = int(row[11]),
                        operator = row[12],
					)
					
			obj.activated = True
			obj.save()
	return render(request, 'capacity_summary_report.html', {'form': form})

