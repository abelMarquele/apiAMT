# from django.http import JsonResponse
# from CSVS.decorators import allowed_users
# from index_translation.models import Cooperative, Corridor, Routa, Bus
# from corridor_performance_report.models import corridor_performance_report

# from django.shortcuts import render
# from CSVS.forms import CsvModelForm
# from dateutil import parser
# from CSVS.models import Csv
# import csv

# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import MultipleObjectsReturned


# @login_required(login_url='csvs:login-view')
# @allowed_users(allowed_roles=['AMT','Maxcom','Admin'])
# def corridor_view(request):
#     corridor = corridor_performance_report.objects.all()
#     form = CsvModelForm(request.POST or None, request.FILES or None)

#     if form.is_valid(): 	
#         form.save()
#         form = CsvModelForm()
#         try:
#             obj = Csv.objects.get(activated=False)
#             status = 200
#             msg = 'Documento preparado com sucesso!'
#             with open(obj.file_name.path, 'r', encoding="cp1252") as f:
#                 reader = csv.reader(f)
#                 cells = list(reader)
#                 inicio = parser.parse(cells[4][1])
#                 fim = parser.parse(cells[5][1])
#                 corridor_performance_report.objects.filter(
#                             date__range =[inicio, fim]
#                 ).delete()
#                 try:
#                     for i in range(len(cells)-1):
#                         if (i>=0 and i<13):
#                             pass	
#                         else:
#                             datetime_obj = parser.parse(cells[i][0])
#                             line_nr_1 = getattr(Routa.objects.get(id=int(cells[i][2])),'routa')
#                             corridor_performance_report.objects.create(
#                                 date = datetime_obj,
#                                 corridor = Corridor.objects.get(id=int(cells[i][1])),
#                                 line_nr = Routa.objects.get(id=int(cells[i][2])),
#                                 line_nr_1 = line_nr_1,
#                                 bus_nr = int(cells[i][3]),
#                                 spz = Bus.objects.get(spz=cells[i][4]),
#                                 spz_1 = cells[i][4],
#                                 cooperative = Cooperative.objects.get(id=int(cells[i][5])), 
#                                 operator = cells[i][6],
#                                 passenger_count = int(cells[i][7]),
#                                 luggage_count = int(cells[i][8]),
#                                 qr_ticket_count = int(cells[i][9]),
#                                 amount_ticket = float(cells[i][10]),
#                                 amount_luggage = float(cells[i][11]),
#                                 maxcom_income = float(cells[i][12]),
#                                 amt_income = float(cells[i][13]),
#                                 operator_income = float(cells[i][14]),
#                             )
#                     obj.activated=True
#                     obj.file_row=i
#                     obj.name='Corridor performance report'
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
            
#     context = {'corridor': corridor, 'form': form}
#     return render(request, 'corridor_performance_report.html', context)



from django.http import JsonResponse
from CSVS.decorators import allowed_users
from index_translation.models import Cooperative, Corridor, Routa, Bus
from corridor_performance_report.models import corridor_performance_report
from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv
from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT', 'Maxcom', 'Admin'])
def corridor_view(request):
    corridor = corridor_performance_report.objects.all()
    form = CsvModelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        form = CsvModelForm()
        try:
            obj = Csv.objects.get(activated=False)
            status = 200
            msg = 'Documento preparado com sucesso!'
            try:
                with open(obj.file_name.path, 'r', encoding="cp1252") as f:
                    reader = csv.reader(f, delimiter=';')
                    cells = list(reader)

                    print(f"Linhas do CSV: {len(cells)}")  # Imprime o número de linhas

                    if len(cells) <= 5:
                        raise Exception("O arquivo CSV não contém dados suficientes.")

                    # print(f"Linha 5: {cells[4]}")
                    # print(f"Linha 6: {cells[5]}")

                    try:
                        inicio = parser.parse(cells[4][1])
                        fim = parser.parse(cells[5][1])
                        # print(f"Datas de início e fim extraídas: {inicio} a {fim}")
                    except Exception as e:
                        raise Exception(f"Erro ao analisar as datas: {e}")

                    # Apagar registros dentro do intervalo de datas
                    delete_count = corridor_performance_report.objects.filter(
                        date__range=[inicio, fim]
                    ).delete()
                    print(f"Registros deletados: {delete_count}")

                    for i in range(len(cells)):
                        if i >= 13:  # Ignora as primeiras 13 linhas
                            row = cells[i]
                            if len(row) < 15:
                                print(f"Linha {i+1} ignorada: não possui colunas suficientes.")
                                continue
                            try:
                                datetime_obj = parser.parse(row[0])
                                line_nr_1 = getattr(Routa.objects.get(id=int(row[2])), 'routa')
                                new_record = corridor_performance_report.objects.create(
                                    date=datetime_obj,
                                    corridor=Corridor.objects.get(id=int(row[1])),
                                    line_nr=Routa.objects.get(id=int(row[2])),
                                    line_nr_1=line_nr_1,
                                    bus_nr=int(row[3]),
                                    spz=Bus.objects.get(spz=row[4]),
                                    spz_1=row[4],
                                    cooperative=Cooperative.objects.get(id=int(row[5])),
                                    operator=row[6],
                                    passenger_count=int(row[7]),
                                    luggage_count=int(row[8]),
                                    qr_ticket_count=int(row[9]),
                                    amount_ticket=float(row[10]),
                                    amount_luggage=float(row[11]),
                                    maxcom_income=float(row[12]),
                                    amt_income=float(row[13]),
                                    operator_income=float(row[14]),
                                )
                                print(f"Novo registro criado: {new_record}")
                            except Exception as e:
                                print(f"Erro ao criar registro na linha {i+1}: {e}")
                                continue

                    obj.activated = True
                    obj.file_row = i
                    obj.name = 'Corridor performance report'
                    obj.save()

                    msg = 'A ação foi realizada com sucesso!'
            except Exception as e:
                print(f"Erro ao processar o arquivo CSV: {e}")
                msg = f"Problema de integridade de dados: {e}"
                status = 500

        except MultipleObjectsReturned:
            Csv.objects.filter(activated=False).delete()
            msg = 'Resolvendo problema de documento com várias referências. Tente novamente!'
            status = 400
        except Exception as e:
            print(f"Erro ao abrir o arquivo CSV: {e}")
            Csv.objects.filter(activated=False).delete()
            msg = f"Documento errado ou erro interno do servidor: {e}"
            status = 500

        return JsonResponse({'message': msg}, status=status)

    context = {'corridor': corridor, 'form': form}
    return render(request, 'corridor_performance_report.html', context)
