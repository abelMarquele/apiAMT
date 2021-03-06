from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import settlement_file_operatorSerializer
from settlement_file_operator.models import settlement_file_operator

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv

from django.contrib.auth.decorators import login_required

# class settlement_file_operatorViewSet(viewsets.ModelViewSet):
#     serializer_class = settlement_file_operator
    
#     def get_queryset(self):
#         settlement_file = settlement_file_operator.objects.all()
#         return settlement_file

#     def destroy(self, request, *args, **kwargs):
#         logedin_user = request.user
#         if(logedin_user == "admin"):
#             settlement_file = self.get_object()
#             settlement_file.delete()
#             response_message = {"message": "O Settlement File Operator foi removido com sucesso!"}
#         else:
#             response_message = {"message": "Não tens permissão para executar essa ação"}

#         return Response(response_message)

#     def create(self, request, *args, **kwargs):
#         settlement_file_data = request.data

#         new_settlement_file = settlement_file_operator.objects.create(
#                     pergunta=Pergunta.objects.get(id=settlement_file_data["pergunta"]), 
#                     resposta=settlement_file_data["resposta"]
                    
#                     # transaction_type = 
#                     # money_value = 
#                     # transaction_count = 
#                     # money_value4 = 
#                     # transaction_type2 = 
#                     # Textbox217 = 
#                     # Textbox214 =
#                     # Textbox218 = 
#                     # transaction_count3 = 
#                     # Textbox74 = 
#                     # Textbox88 = 
#                     # transaction_count4 = 
#                     # Textbox98 = 
#                     # Textbox100 =
#                     # rank = 
#                     # carrier_name = 
#                     # cooperatives = 
#                     # money_value3 = 
#                     # Textbox220 = 
#                     # transaction_count2 = 
#                     # Textbox76 = 
#                     # Textbox77 = 
#                             )


#         new_settlement_file.save()

#         serializer = settlement_file_operatorSerializer(new_settlement_file)
#         return Response(serializer.data)

#     def update(self, request, *args, **kwargs):
#         settlement_file_data = self.get_object()
#         data = request.data

#         pergunta = Pergunta.objects.get(id=data["pergunta"])
#         settlement_file_data.pergunta = pergunta
#         settlement_file_data.resposta = data["resposta"]

#         settlement_file_data.save()

#         serializer = settlement_file_operatorSerializer(settlement_file_data)
#         return Response(serializer.data)

#     def partial_update(self, request, *args, **kwargs):
#         settlement_file_object = self.get_object()
#         data = request.data

#         try:
#             pergunta = Pergunta.objects.get(id=data["pergunta"])
#             settlement_file_object.pergunta = pergunta
#         except KeyError:
#             pass

#         settlement_file_object.resposta = data.get("resposta", settlement_file_object.resposta)

#         settlement_file_object.save()

#         serializer = settlement_file_operatorSerializer(settlement_file_object)
#         return Response(serializer.data)






