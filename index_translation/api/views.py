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

@login_required(login_url='csvs:login-view')
def index_translation_view(request):
    return render(request, 'index_translation.html',)

@login_required(login_url='csvs:login-view')
def cooperative_view(request):
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
                    # print(row)
                    # print(type(row))					
                    Cooperative.objects.create(
                        id	= int(row[0]),
						cooperative = row[1],
					)
            obj.activated = True
            obj.save()
    return render(request, 'cooperative.html', {'form': form})

@login_required(login_url='csvs:login-view')
def corridor_view(request):
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
                    Corridor.objects.create(
                        id	= int(row[0]),
						corridor = row[1],
					)
            obj.activated = True
            obj.save()

    return render(request, 'corridor.html',{'form': form})

@login_required(login_url='csvs:login-view')
def routa_view(request):
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
                    # print(row)
                    corridor  = row[3].split(' ', 1)
                    #print(row)					
                    Routa.objects.create(
                        id	= int(row[0]),
						routa = row[1],
                        via = row[2],
                        corridor = Corridor.objects.get(id=int(corridor[1])),  
					)
            obj.activated = True
            obj.save()

    return render(request, 'routa.html', {'form': form})
