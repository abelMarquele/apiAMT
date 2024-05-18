# from django.core.exceptions import MultipleObjectsReturned
# from CSVS.decorators import allowed_users
from index_translation.models import Cooperative, Corridor, Routa, Bus, Manager
from capacity_summary_report.models import capacity_summary_report
# from django.shortcuts import render
# from CSVS.forms import CsvModelForm
# from dateutil import parser
from CSVS.models import Csv
# import csv
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse


# @login_required(login_url='csvs:login-view')
# @allowed_users(allowed_roles=['AMT','Maxcom','Admin'])
# def capacity_view(request):
#     capacity = capacity_summary_report.objects.all()
#     form = CsvModelForm(request.POST or None, request.FILES or None)
    
#     if form.is_valid(): 	
#         form.save()
#         form = CsvModelForm()
#         try:
#             obj = Csv.objects.get(activated=False)
#             status = 200
#             msg = 'Documento preparado com sucesso!'
#             with open(obj.file_name.path, 'r' , encoding="cp1252") as f:
#                 reader = csv.reader(f)
#                 cells = list(reader)
#                 inicio = parser.parse(cells[4][1])
#                 fim = parser.parse(cells[5][1])
#                 capacity_summary_report.objects.filter(
#                         date__range =[inicio, fim]
#                 ).delete()

#                 try:
#                     for i in range(len(cells)-1):
#                         if (i>=0 and i<12):
#                             pass	
#                         else:
#                             datetime_obj = parser.parse(cells[i][0])	 				
#                             capacity_summary_report.objects.create(
#                                 date = datetime_obj,
#                                 corridor = Corridor.objects.get(id=int(cells[i][1])),  
#                                 line_nr =  Routa.objects.get(id=int(cells[i][2])),  
#                                 bus_nr = int(cells[i][3]),
#                                 spz = Bus.objects.get(spz=cells[i][4]),
#                                 no_of_trips = int(cells[i][5]),
#                                 passenger_count = int(cells[i][6]),
#                                 total_income = float(cells[i][7]),
#                                 maxcom_income = float(cells[i][8]),
#                                 amt_income = float(cells[i][9]),
#                                 operator_income = float(cells[i][10]),
#                                 cooperative = Cooperative.objects.get(id=int(cells[i][11])), 
#                                 operator = Manager.objects.get(abbreviated=cells[i][12])
#                             )      
#                     obj.activated=True
#                     obj.file_row=i
#                     obj.name='Capacity summary report'
#                     obj.save()  

#                     status = 200
#                     msg = 'A ação foi realizada com sucesso!'
#                 except Exception as e:
#                     status = 500
#                     msg = 'Problema de integridade de dados!'
#                 finally:
#                     return JsonResponse({'message': msg}, status=status)

#         except MultipleObjectsReturned as e:
#             Csv.objects.filter(activated=False).delete()
#             status = 400
#             msg = 'Resolvendo problema de documento com várias referências. Tente novamente!'
#         except Exception as e:
#             Csv.objects.filter(activated=False).delete()
#             status = 500
#             msg = 'Documento errado ou erro interno do servidor!'
#         finally:
#             return JsonResponse({'message': msg}, status=status)

#     context = {'capacity': capacity,'form': form}
#     return render(request, 'capacity_summary_report.html', context)


from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth.decorators import login_required
import csv
from dateutil import parser
# from .models import Csv, capacity_summary_report, Corridor, Routa, Bus, Cooperative, Manager
from CSVS.forms import CsvModelForm
from CSVS.decorators import allowed_users

# @login_required(login_url='csvs:login-view')
# @allowed_users(allowed_roles=['AMT', 'Maxcom', 'Admin'])
# def capacity_view(request):
#     capacity = capacity_summary_report.objects.all()
#     form = CsvModelForm(request.POST or None, request.FILES or None)

#     if form.is_valid():
#         form.save()
#         form = CsvModelForm()
#         try:
#             obj = Csv.objects.get(activated=False)
#             with open(obj.file_name.path, 'r', encoding="cp1252") as f:
#                 reader = csv.reader(f)
#                 cells = list(reader)
#                 inicio = parser.parse(cells[4][1])
#                 fim = parser.parse(cells[5][1])
#                 capacity_summary_report.objects.filter(
#                     date__range=[inicio, fim]
#                 ).delete()

#                 try:
#                     for i in range(len(cells) - 1):
#                         if i >= 0 and i < 12:
#                             pass
#                         else:
#                             datetime_obj = parser.parse(cells[i][0])
#                             capacity_summary_report.objects.create(
#                                 date=datetime_obj,
#                                 corridor=Corridor.objects.get(id=int(cells[i][1])),
#                                 line_nr=Routa.objects.get(id=int(cells[i][2])),
#                                 bus_nr=int(cells[i][3]),
#                                 spz=Bus.objects.get(spz=cells[i][4]),
#                                 no_of_trips=int(cells[i][5]),
#                                 passenger_count=int(cells[i][6]),
#                                 total_income=float(cells[i][7]),
#                                 maxcom_income=float(cells[i][8]),
#                                 amt_income=float(cells[i][9]),
#                                 operator_income=float(cells[i][10]),
#                                 cooperative=Cooperative.objects.get(id=int(cells[i][11])),
#                                 operator=Manager.objects.get(abbreviated=cells[i][12])
#                             )
#                     obj.activated = True
#                     obj.file_row = i
#                     obj.name = 'Capacity summary report'
#                     obj.save()
#                     return JsonResponse({'message': 'A ação foi realizada com sucesso!'}, status=200)

#                 except Exception as e:
#                     return JsonResponse({'message': 'Problema de integridade de dados!', 'error': str(e)}, status=500)

#         except MultipleObjectsReturned:
#             Csv.objects.filter(activated=False).delete()
#             return JsonResponse({'message': 'Resolvendo problema de documento com várias referências. Tente novamente!'}, status=400)
#         except Exception as e:
#             Csv.objects.filter(activated=False).delete()
#             return JsonResponse({'message': 'Documento errado ou erro interno do servidor!', 'error': str(e)}, status=500)

#     context = {'capacity': capacity, 'form': form}
#     return render(request, 'capacity_summary_report.html', context)




@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT', 'Maxcom', 'Admin'])
def capacity_view(request):
    capacity = capacity_summary_report.objects.all()
    form = CsvModelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        form = CsvModelForm()
        try:
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path, 'r', encoding="cp1252") as f:
                reader = csv.reader(f)
                cells = [row[0].split(';') for row in reader]

                # Verificar se há linhas suficientes no arquivo CSV
                if len(cells) < 6:
                    raise Exception("Arquivo CSV não possui linhas suficientes para processar as datas.")
                
                try:
                    inicio = parser.parse(cells[4][1].strip())
                    fim = parser.parse(cells[5][1].strip())
                    print(f"Datas de início e fim extraídas: {inicio} a {fim}")
                except IndexError:
                    raise Exception("Arquivo CSV não possui colunas suficientes para as datas de início e fim.")
                
                # Apagar registros dentro do intervalo de datas
                delete_count = capacity_summary_report.objects.filter(
                    date__range=[inicio, fim]
                ).delete()
                print(f"Registros deletados: {delete_count}")

                try:
                    for i in range(len(cells) - 1):
                        if i >= 0 and i < 12:
                            continue
                        else:
                            # Verificar se há colunas suficientes na linha atual
                            if len(cells[i]) < 13:
                                raise Exception(f"Linha {i+1} do arquivo CSV não possui colunas suficientes.")
                            
                            datetime_obj = parser.parse(cells[i][0].strip())
                            new_record = capacity_summary_report.objects.create(
                                date=datetime_obj,
                                corridor=Corridor.objects.get(id=int(cells[i][1].strip())),
                                line_nr=Routa.objects.get(id=int(cells[i][2].strip())),
                                bus_nr=int(cells[i][3].strip()),
                                spz=Bus.objects.get(spz=cells[i][4].strip()),
                                no_of_trips=int(cells[i][5].strip()),
                                passenger_count=int(cells[i][6].strip()),
                                total_income=float(cells[i][7].strip()),
                                maxcom_income=float(cells[i][8].strip()),
                                amt_income=float(cells[i][9].strip()),
                                operator_income=float(cells[i][10].strip()),
                                cooperative=Cooperative.objects.get(id=int(cells[i][11].strip())),
                                operator=Manager.objects.get(abbreviated=cells[i][12].strip())
                            )
                            print(f"Novo registro criado: {new_record}")

                    obj.activated = True
                    obj.file_row = i
                    obj.name = 'Capacity summary report'
                    obj.save()
                    return JsonResponse({'message': 'A ação foi realizada com sucesso!'}, status=200)

                except Exception as e:
                    print(f"Erro ao processar o arquivo CSV: {e}")  # Imprime o erro no console
                    return JsonResponse({'message': 'Problema de integridade de dados!'}, status=500)

        except MultipleObjectsReturned:
            Csv.objects.filter(activated=False).delete()
            return JsonResponse({'message': 'Resolvendo problema de documento com várias referências. Tente novamente!'}, status=400)
        except Exception as e:
            print(f"Erro ao abrir o arquivo CSV: {e}")  # Imprime o erro no console
            Csv.objects.filter(activated=False).delete()
            return JsonResponse({'message': 'Documento errado ou erro interno do servidor!', 'error': str(e)}, status=500)

    context = {'capacity': capacity, 'form': form}
    return render(request, 'capacity_summary_report.html', context)



