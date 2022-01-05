from rest_framework.response import Response
from rest_framework import viewsets

from index_translation.models import Cooperative, Corridor, Routa
from .serializers import corridor_performance_reportSerializer
from corridor_performance_report.models import corridor_performance_report

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv


class corridor_performance_reportViewSet(viewsets.ModelViewSet):
    serializer_class = corridor_performance_reportSerializer
    
    def get_queryset(self):
        corridor = corridor_performance_report.objects.all()
        return corridor
    
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        params_list = params['pk'].split('&')
        print(params_list)
        corridor = corridor_performance_report.objects.filter(
            operator = params_list[0],
            date = params_list[1]
            )
        serializer = corridor_performance_reportSerializer(corridor, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            corridor = self.get_object()
            corridor.delete()
            response_message = {"message": "Corridor Performance Report foi removido com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa ação"}

        return Response(response_message)

    # def create(self, request, *args, **kwargs):
    #     corridor_data = request.data

    #     new_corridor = corridor_performance_report.objects.create(
    #                 pergunta=Pergunta.objects.get(id=corridor_data["pergunta"]), 
    #                 resposta=corridor_data["resposta"],
                    
    #                 # company_id	= int(row[0]),
	# 				# company_name = row[1],	
	# 				# device	= row[2],
	# 				# conductor_id = int(row[3]),	
	# 				# conductor_first_name = row[4],
	# 				# conductor_last_name = row[5],
	# 				# number	= int(row[6]),
	# 				# amount	= row[7],
	# 				# date = datetime_obj,
    #                     )

    #     new_corridor.save()

    #     serializer = corridor_performance_reportSerializer(new_corridor)
    #     return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     corridor_data = self.get_object()
    #     data = request.data

    #     pergunta = Pergunta.objects.get(id=data["pergunta"])
    #     corridor_data.pergunta = pergunta
    #     corridor_data.resposta = data["resposta"]

    #     corridor_data.save()

    #     serializer = corridor_performance_reportSerializer(corridor_data)
    #     return Response(serializer.data)

    # def partial_update(self, request, *args, **kwargs):
    #     corridor_object = self.get_object()
    #     data = request.data

    #     try:
    #         pergunta = Pergunta.objects.get(id=data["pergunta"])
    #         corridor_object.pergunta = pergunta
    #     except KeyError:
    #         pass

    #     corridor_object.resposta = data.get("resposta", corridor_object.resposta)

    #     corridor_object.save()

    #     serializer = corridor_performance_reportSerializer(corridor_object)
    #     return Response(serializer.data)


def corridor_upload_file_view(request):
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
            obj.activated = True
            obj.save()
    return render(request, 'corridor_performance_report.html', {'form': form})



