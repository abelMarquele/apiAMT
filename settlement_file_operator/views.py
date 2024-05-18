# from CSVS.decorators import allowed_users
# from django.core.exceptions import MultipleObjectsReturned
# from settlement_file_operator.models import settlement_file_operator
# from index_translation.models import Cooperative
# from django.http import JsonResponse
# from django.shortcuts import render
# from CSVS.forms import CsvModelForm
# from dateutil import parser
# from CSVS.models import Csv
# import csv

# from django.contrib.auth.decorators import login_required

# @login_required(login_url='csvs:login-view')
# @allowed_users(allowed_roles=['AMT','Maxcom','Admin'])
# def settlement_view(request):
#     settlement_file = settlement_file_operator.objects.all()
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
#                 settlement_file_operator.objects.filter(
#                         date__range =[inicio, fim]
#                 ).delete()
#                 try:
#                     for i in range(len(cells)-1):
#                         if (i>=0 and i<12):
#                             pass	
#                         else:	
#                             datetime_obj = parser.parse(cells[9][0])					
#                             settlement_file_operator.objects.create( 
#                                 date =   datetime_obj,
#                                 transaction_type = cells[i][0], 
#                                 money_value = float(cells[i][1]),
#                                 transaction_count = int(cells[i][2]),
#                                 money_value4 = float(cells[i][3]),
#                                 transaction_type2 = cells[i][4],
#                                 Textbox217 = int(cells[i][5]),
#                                 Textbox214 = int(cells[i][6]),
#                                 Textbox218 = int(cells[i][7]), 
#                                 transaction_count3 = int(cells[i][8]),
#                                 Textbox74 = float(cells[i][9]),
#                                 Textbox88 = float(cells[i][10]),
#                                 transaction_count4 = int(cells[i][11]),
#                                 Textbox98 = float(cells[i][12]),
#                                 Textbox100 = float(cells[i][13]),
#                                 rank = int(cells[i][14]),
#                                 carrier_name = cells[i][15],
#                                 cooperatives = cells[i][16],
#                                 money_value3 = float(cells[i][17]),
#                                 Textbox220 = float(cells[i][18]),
#                                 transaction_count2 = float(cells[i][19]),
#                                 Textbox76 = float(cells[i][20]),
#                                 Textbox77 = float(cells[i][21]),                        
#                             )
                            
#                     obj.activated=True
#                     obj.file_row=i
#                     obj.name='Settlement file operator'
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


#     context = {'settlement_file': settlement_file, 'form': form}
#     return render(request, 'settlement_file_operator.html', context)




from CSVS.decorators import allowed_users
from django.core.exceptions import MultipleObjectsReturned
from settlement_file_operator.models import settlement_file_operator
from django.http import JsonResponse
from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv

from django.contrib.auth.decorators import login_required

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT', 'Maxcom', 'Admin'])
def settlement_view(request):
    settlement_file = settlement_file_operator.objects.all()
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
                    # print(f"Linhas do CSV: {len(cells)}")
                    # print(f"Linha 5: {cells[4]}")
                    # print(f"Linha 6: {cells[5]}")

                    inicio = parser.parse(cells[4][1].strip())
                    fim = parser.parse(cells[5][1].strip())
                    # print(f"Datas de início e fim extraídas: {inicio} a {fim}")

                    settlement_file_operator.objects.filter(
                        date__range=[inicio, fim]
                    ).delete()

                    for i in range(12, len(cells)):
                        row = cells[i]
                        if len(row) < 22:
                            print(f"Linha {i+1} ignorada: formato inesperado ou número de colunas insuficiente.")
                            continue
                        
                        datetime_obj = parser.parse(row[9].strip())
                        settlement_file_operator.objects.create(
                            date=datetime_obj,
                            transaction_type=row[0].strip(),
                            money_value=float(row[1].strip()),
                            transaction_count=int(row[2].strip()),
                            money_value4=float(row[3].strip()),
                            transaction_type2=row[4].strip(),
                            Textbox217=int(row[5].strip()),
                            Textbox214=int(row[6].strip()),
                            Textbox218=int(row[7].strip()),
                            transaction_count3=int(row[8].strip()),
                            Textbox74=float(row[9].strip()),
                            Textbox88=float(row[10].strip()),
                            transaction_count4=int(row[11].strip()),
                            Textbox98=float(row[12].strip()),
                            Textbox100=float(row[13].strip()),
                            rank=int(row[14].strip()),
                            carrier_name=row[15].strip(),
                            cooperatives=row[16].strip(),
                            money_value3=float(row[17].strip()),
                            Textbox220=float(row[18].strip()),
                            transaction_count2=int(row[19].strip()),
                            Textbox76=float(row[20].strip()),
                            Textbox77=float(row[21].strip()),
                        )

                    obj.activated = True
                    obj.file_row = i
                    obj.name = 'Settlement file operator'
                    obj.save()

                    status = 200
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

    context = {'settlement_file': settlement_file, 'form': form}
    return render(request, 'settlement_file_operator.html', context)
