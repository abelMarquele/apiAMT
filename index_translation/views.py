from CSVS.decorators import allowed_users
from index_translation.filters import cooperativeFilter, corridorFilter, routaFilter
from index_translation.models import Cooperative, Corridor, Routa

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from CSVS.models import Csv
import csv

from django.contrib.auth.decorators import login_required


@login_required(login_url='csvs:login-view')
def index_translation_view(request):
    return render(request, 'index_translation.html',)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def cooperative_view(request):
    cooperative = Cooperative.objects.all()

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
            obj.activated=True
            obj.file_row=i
            obj.nome='Cooperarive'
            obj.save()

    myFilter = cooperativeFilter(request.GET, queryset=cooperative)
    cooperative = myFilter.qs

    context = {'cooperative': cooperative,'myFilter':myFilter, 'form': form}
    return render(request, 'cooperative.html', context)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def corridor_view(request):
    corridor = Corridor.objects.all()

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
            obj.activated=True
            obj.file_row=i
            obj.nome='Corridor'
            obj.save()

    myFilter = corridorFilter(request.GET, queryset=corridor)
    corridor = myFilter.qs

    context = {'corridor': corridor,'myFilter':myFilter, 'form': form}
    return render(request, 'corridor.html',context)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def routa_view(request):
    routa = Routa.objects.all()

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
            obj.activated=True
            obj.file_row=i
            obj.nome='Routa'
            obj.save()

    myFilter = routaFilter(request.GET, queryset=routa)
    routa = myFilter.qs

    context = {'routa': routa,'myFilter':myFilter, 'form': form}
    return render(request, 'routa.html', context)
