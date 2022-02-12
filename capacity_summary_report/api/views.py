from datetime import date
from rest_framework.response import Response
from rest_framework import viewsets
from CSVS.decorators import allowed_users

from index_translation.models import Cooperative, Corridor, Routa
from .serializers import capacity_summary_reportSerializer
from capacity_summary_report.models import capacity_summary_report

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv

from django.contrib.auth.decorators import login_required


class capacity_summary_reportViewSet(viewsets.ModelViewSet):
    serializer_class = capacity_summary_report
    
    def get_queryset(self):
        capacity = capacity_summary_report.objects.all()
        return capacity

#     def destroy(self, request, *args, **kwargs):
#         logedin_user = request.user
#         if(logedin_user == "admin"):
#             capacity = self.get_object()
#             capacity.delete()
#             response_message = {"message": "Capacity Summary Report foi removido com sucesso!"}
#         else:
#             response_message = {"message": "Não tens permissão para executar essa ação"}

#         return Response(response_message)

    # def create(self, request, *args, **kwargs):
    #     capacity_data = request.data

    #     new_capacity = capacity_summary_report.objects.create(
    #                 pergunta=Pergunta.objects.get(id=capacity_data["pergunta"]), 
    #                 resposta=capacity_data["resposta"]
    #                 # date = 
    #                 # corridor = 
    #                 # line_nr = 
    #                 # bus_nr = 
    #                 # spz = 
    #                 # no_of_trips = 
    #                 # passenger_count = 
    #                 # total_income = 
    #                 # maxcom_income = 
    #                 # amt_income = 
    #                 # operator_income = 
    #                 # cooperative = 
    #                 # operator = 
    #     )
    #     new_capacity.save()

    #     serializer = capacity_summary_reportSerializer(new_capacity)
    #     return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     capacity_data = self.get_object()
    #     data = request.data

    #     pergunta = Pergunta.objects.get(id=data["pergunta"])
    #     capacity_data.pergunta = pergunta
    #     capacity_data.resposta = data["resposta"]

    #     capacity_data.save()

    #     serializer = capacity_summary_reportSerializer(capacity_data)
    #     return Response(serializer.data)

    # def partial_update(self, request, *args, **kwargs):
    #     capacity_object = self.get_object()
    #     data = request.data

    #     try:
    #         pergunta = Pergunta.objects.get(id=data["pergunta"])
    #         capacity_object.pergunta = pergunta
    #     except KeyError:
    #         pass

    #     capacity_object.resposta = data.get("resposta", capacity_object.resposta)

    #     capacity_object.save()

    #     serializer = capacity_summary_reportSerializer(capacity_object)
    #     return Response(serializer.data)

# @login_required(login_url='csvs:login-view')
# @allowed_users(allowed_roles=['AMT'])
# def capacity(request):
#     capacity = capacity_summary_report.objects.all()

#     return render(request, 'capacity_summary_report.html', {'capacity': capacity})
