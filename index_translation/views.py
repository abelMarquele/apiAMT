from CSVS.decorators import allowed_users
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
    cooperative_count = cooperative.count()

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

    context = {'cooperative': cooperative,'cooperative_count':cooperative_count, 'form': form}
    return render(request, 'cooperative.html', context)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def corridor_view(request):
    corridor = Corridor.objects.all()
    corridor_count = corridor.count()

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

    context = {'corridor': corridor, 'corridor_count':corridor_count, 'form': form}
    return render(request, 'corridor.html',context)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def routa_view(request):
    routa = Routa.objects.all()
    routa_count = routa.count()

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


    context = {'routa': routa,'routa_count':routa_count, 'form': form}
    return render(request, 'routa.html', context)
