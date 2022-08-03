from django.http import JsonResponse
from CSVS.decorators import allowed_users
from index_translation.models import Assign, Bus, Manager, Cooperative, Corridor, Routa

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from CSVS.models import Csv, Profile
import csv

from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned


@login_required(login_url='csvs:login-view')
def index_translation_view(request):
    return render(request, 'dashboard/index_translation.html',)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def cooperative_view(request):
    cooperative = Cooperative.objects.all()
    cooperative_count = cooperative.count()

    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid(): 	
        form.save()
        form = CsvModelForm()
        try:
            obj = Csv.objects.get(activated=False)
            status = 200
            msg = 'Documento preparado com sucesso!'
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)
                try:
                    for i, row in enumerate(reader):
                        if i==0:
                            pass
                        else:						
                            objj, created =  Cooperative.objects.get_or_create(
                                    id	= int(row[0]),
                                    cooperative = row[1],
                                )
                    obj.activated=True
                    obj.file_row=i
                    obj.name='Cooperarive'
                    obj.save()

                    status = 200
                    msg = 'A ação foi realizada com sucesso!'
                except Exception as e:
                    status = 500
                    msg = 'Problema de integridade de dados!'
                finally:
                    return JsonResponse({'message': msg}, status=status)

        except MultipleObjectsReturned as e:
            Csv.objects.filter(activated=False).delete()
            status = 400
            msg = 'Resolvendo problema de documento com várias referências. Tente novamente!'
        except Exception as e:
            Csv.objects.filter(activated=False).delete()
            status = 500
            msg = 'Documento errado ou erro interno do servidor!'
        finally:
            return JsonResponse({'message': msg}, status=status)

    context = {'cooperative': cooperative,'cooperative_count':cooperative_count, 'form': form}
    return render(request, 'dashboard/cooperative.html', context)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def corridor_view(request):
    corridor = Corridor.objects.all()
    corridor_count = corridor.count()

    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid(): 	
        form.save()
        form = CsvModelForm()
        try:
            obj = Csv.objects.get(activated=False)
            status = 200
            msg = 'Documento preparado com sucesso!'
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)
                try:
                    for i, row in enumerate(reader):
                        if i==0:
                            pass
                        else:					
                            objj, created = Corridor.objects.get_or_create(
                                    id	= int(row[0]),
                                    corridor = row[1],
                                )
                    obj.activated=True
                    obj.file_row=i
                    obj.name='Corridor'
                    obj.save()

                    status = 200
                    msg = 'A ação foi realizada com sucesso!'
                except Exception as e:
                    status = 500
                    msg = 'Problema de integridade de dados!'
                finally:
                    return JsonResponse({'message': msg}, status=status)

        except MultipleObjectsReturned as e:
            Csv.objects.filter(activated=False).delete()
            status = 400
            msg = 'Resolvendo problema de documento com várias referências. Tente novamente!'
        except Exception as e:
            Csv.objects.filter(activated=False).delete()
            status = 500
            msg = 'Documento errado ou erro interno do servidor!'
        finally:
            return JsonResponse({'message': msg}, status=status)

    context = {'corridor': corridor, 'corridor_count':corridor_count, 'form': form}
    return render(request, 'dashboard/corridor.html',context)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def routa_view(request):
    routa = Routa.objects.all()
    routa_count = routa.count()

    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid(): 	
        form.save()
        form = CsvModelForm()
        try:
            obj = Csv.objects.get(activated=False)
            status = 200
            msg = 'Documento preparado com sucesso!'
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)
                try:
                    for i, row in enumerate(reader):
                        if i==0 or row[0] == '':
                            pass
                        else:
                            # print(row)
                            corridor  = row[3].split(' ', 1)				
                            objj, created = Routa.objects.get_or_create(
                                    id	= int(row[0]),
                                    routa = row[1],
                                    via = row[2],
                                    corridor = Corridor.objects.get(id=int(corridor[1])), 
                                )
                    obj.activated=True
                    obj.file_row=i
                    obj.name='Routa'
                    obj.save()

                    status = 200
                    msg = 'A ação foi realizada com sucesso!'
                except Exception as e:
                    status = 500
                    msg = 'Problema de integridade de dados!'
                finally:
                    return JsonResponse({'message': msg}, status=status)

        except MultipleObjectsReturned as e:
            Csv.objects.filter(activated=False).delete()
            status = 400
            msg = 'Resolvendo problema de documento com várias referências. Tente novamente!'
        except Exception as e:
            Csv.objects.filter(activated=False).delete()
            status = 500
            msg = 'Documento errado ou erro interno do servidor!'
        finally:
            return JsonResponse({'message': msg}, status=status)

    context = {'routa': routa,'routa_count':routa_count, 'form': form}
    return render(request, 'dashboard/routa.html', context)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def bus_view(request):
    bus = Bus.objects.all()
    bus_count = bus.count()

    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid(): 	
        form.save()
        form = CsvModelForm()
        try:
            obj = Csv.objects.get(activated=False)
            status = 200
            msg = 'Documento preparado com sucesso!'
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)
                try:
                    for i, row in enumerate(reader):
                        if i==0:
                            pass
                        else:
                            objj, created = Bus.objects.get_or_create(
                                spz	= row[0],
                                brand = row[1],
                            )
        
                    obj.activated=True
                    obj.file_row=i
                    obj.name='Bus'
                    obj.save()

                    status = 200
                    msg = 'A ação foi realizada com sucesso!'
                except Exception as e:
                    status = 500
                    msg = 'Problema de integridade de dados!'
                finally:
                    return JsonResponse({'message': msg}, status=status)         


        except MultipleObjectsReturned as e:
            Csv.objects.filter(activated=False).delete()
            status = 400
            msg = 'Resolvendo problema de documento com várias referências. Tente novamente!'
        except Exception as e:
            Csv.objects.filter(activated=False).delete()
            status = 500
            msg = 'Documento errado ou erro interno do servidor!'
        finally:
            return JsonResponse({'message': msg}, status=status)

    context = {'bus': bus, 'bus_count':bus_count, 'form': form}
    return render(request, 'dashboard/bus.html',context)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def manager_view(request):
    manager = Manager.objects.all()
    manager_count = manager.count()

    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid(): 	
        form.save()
        form = CsvModelForm()
        try:
            obj = Csv.objects.get(activated=False)
            status = 200
            msg = 'Documento preparado com sucesso!'
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)
                try:
                    for i, row in enumerate(reader):
                        if i==0:
                            pass
                        else:					
                            objj, created = Manager.objects.get_or_create(
                                operator= row[0],
                                abbreviated = row[1],
                            )
                    obj.activated=True
                    obj.file_row=i
                    obj.name='Manager'
                    obj.save()
                    
                    status = 200
                    msg = 'A ação foi realizada com sucesso!'
                except Exception as e:
                    status = 500
                    msg = 'Problema de integridade de dados!'
                finally:
                    return JsonResponse({'message': msg}, status=status)

        except MultipleObjectsReturned as e:
            Csv.objects.filter(activated=False).delete()
            status = 400
            msg = 'Resolvendo problema de documento com várias referências. Tente novamente!'
        except Exception as e:
            Csv.objects.filter(activated=False).delete()
            status = 500
            msg = 'Documento errado ou erro interno do servidor!'
        finally:
            return JsonResponse({'message': msg}, status=status)

    context = {'manager': manager, 'manager_count':manager_count, 'form': form}
    return render(request, 'dashboard/manager.html',context)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def assign_bus_view(request, pk):
    assign_bus = Assign.objects.filter(manager=pk)
    assign_bus_count = assign_bus.count() 
    assign_bus_name= assign_bus.first()
    
    manager = Manager.objects.get(id= assign_bus_name.manager.id)
    profiles = Profile.objects.get(user=manager.user)

    context = {'assign_bus': assign_bus, 'assign_bus_count':assign_bus_count, 'assign_bus_name':assign_bus_name
    , 'profiles':profiles}
    return render(request, 'dashboard/assign_bus.html', context)

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT','Maxcom'])
def assign_view(request):
    assign = Assign.objects.all()
    assign_count = assign.count()

    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid(): 	
        form.save()
        form = CsvModelForm()
        try:
            obj = Csv.objects.get(activated=False)
            status = 200
            msg = 'Documento preparado com sucesso!'
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)
                try:
                    for i, row in enumerate(reader):
                        if i==0:
                            pass
                        else:			
                            objj, created = Assign.objects.get_or_create(
                                        cooperative = Cooperative.objects.get(cooperative=row[0]),
                                        cooperativeR = row[0],
                                        manager = Manager.objects.get(operator=row[1]),  
                                        managerR = row[1],  
                                        bus = Bus.objects.get(spz=row[2]), 
                                        activated= True,   
                                )
                    obj.activated=True
                    obj.file_row=i
                    obj.name='Assign'
                    obj.save()
                    status = 200
                    msg = 'A ação foi realizada com sucesso!'
                except Exception as e:
                    status = 500
                    msg = 'Problema de integridade de dados!'
                finally:
                    return JsonResponse({'message': msg}, status=status)

        except MultipleObjectsReturned as e:
            Csv.objects.filter(activated=False).delete()
            status = 400
            msg = 'Resolvendo problema de documento com várias referências. Tente novamente!'
        except Exception as e:
            Csv.objects.filter(activated=False).delete()
            status = 500
            msg = 'Documento errado ou erro interno do servidor!'
        finally:
            return JsonResponse({'message': msg}, status=status)

    context = {'assign': assign,'assign_count':assign_count, 'form': form}
    return render(request, 'dashboard/assign.html', context)