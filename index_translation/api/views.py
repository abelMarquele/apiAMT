from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import cooperativeSerializer, corridorSerializer, routaSerializer
from index_translation.models import Cooperative, Corridor, Routa

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from CSVS.models import Csv
import csv

from django.contrib.auth.decorators import login_required


# class cooperativeViewSet(viewsets.ModelViewSet):
#     serializer_class = cooperativeSerializer
    
#     def get_queryset(self):
#         cooperatives = Cooperative.objects.all()
#         return cooperatives

#     def destroy(self, request, *args, **kwargs):
#         logedin_user = request.user
#         if(logedin_user == "admin"):
#             cooperative = self.get_object()
#             cooperative.delete()
#             response_message = {"message": "A Cooperative foi removida com sucesso!"}
#         else:
#             response_message = {"message": "Não tens permissão para executar essa ação"}

#         return Response(response_message)


# class corridorViewSet(viewsets.ModelViewSet):
#     serializer_class = corridorSerializer
    
#     def get_queryset(self):
#         corridores = Corridor.objects.all()
#         return corridores

#     def destroy(self, request, *args, **kwargs):
#         logedin_user = request.user
#         if(logedin_user == "admin"):
#             corridor = self.get_object()
#             corridor.delete()
#             response_message = {"message": "O Corridor foi removido com sucesso!"}
#         else:
#             response_message = {"message": "Não tens permissão para executar essa ação"}

#         return Response(response_message)

# class routaViewSet(viewsets.ModelViewSet):
#     serializer_class = routaSerializer
    
#     def get_queryset(self):
#         routas = Routa.objects.all()
#         return routas

#     def destroy(self, request, *args, **kwargs):
#         logedin_user = request.user
#         if(logedin_user == "admin"):
#             routa = self.get_object()
#             routa.delete()
#             response_message = {"message": "A Routa foi removida com sucesso!"}
#         else:
#             response_message = {"message": "Não tens permissão para executar essa ação"}

#         return Response(response_message)
