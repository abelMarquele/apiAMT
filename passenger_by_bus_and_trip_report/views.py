# from django.http import JsonResponse
# from CSVS.decorators import allowed_users
# from passenger_by_bus_and_trip_report.models import passenger_by_bus_and_trip_report
# from index_translation.models import Routa, Bus

# from django.shortcuts import render
# from CSVS.forms import CsvModelForm
# from dateutil import parser
# from CSVS.models import Csv
# import pandas
# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import MultipleObjectsReturned


# @login_required(login_url='csvs:login-view')
# @allowed_users(allowed_roles=['AMT','Maxcom','Admin'])
# def passenger_view(request):
#     passenger = passenger_by_bus_and_trip_report.objects.all()
#     form = CsvModelForm(request.POST or None, request.FILES or None)

#     if form.is_valid(): 	
#         form.save()
#         form = CsvModelForm()
#         try:
#             obj = Csv.objects.get(activated=False)
#             status = 200
#             msg = 'Documento preparado com sucesso!'
#             with open(obj.file_name.path, 'r', encoding="cp1252") as f:
#                 pd = pandas.read_csv(f)
#                 inicio = parser.parse(pd.timestamp1.min()).date()
#                 fim = parser.parse(pd.timestamp1.max()).date()
#                 passenger_by_bus_and_trip_report.objects.filter(
#                             timestamp1__range =[inicio, fim]
#                 ).delete()
                
#                 try:
#                     for i in range(len(pd.index)):
#                         device_location1  = pd.device_location1[i].split(' - ', 1)
#                         datetime_obj = parser.parse(pd.timestamp1[i]).date()
#                         timestamp = parser.parse(pd.timestamp[i]).time() 
#                         chout_timestamp = parser.parse(pd.chout_timestamp[i]).time()				
#                         passenger_by_bus_and_trip_report.objects.create(
#                                 timestamp1 = datetime_obj,
#                                 device_location1 = pd.device_location1[i],
#                                 line_reg_no1 = Routa.objects.get(id=int(pd.line_reg_no1[i])),
#                                 route_reg_no1 = int(pd.route_reg_no1[i]),
#                                 route_reg_no = int(pd.route_reg_no[i]),
#                                 customer_profile_name = pd.customer_profile_name[i],
#                                 card_uid3 = pd.card_uid3[i],
#                                 timestamp = timestamp,
#                                 stationfrom_short_name = pd.stationfrom_short_name[i],
#                                 chout_timestamp = chout_timestamp,
#                                 stationto_short_name = pd.stationto_short_name[i],
#                                 money_value = float(pd.money_value[i]),
#                                 transaction_count = int(pd.transaction_count[i]),
#                                 money_value1 = float(pd.money_value1[i]),
#                                 transaction_count2 = int(pd.transaction_count2[i]),
#                                 money_value3 = float(pd.money_value3[i]),
#                                 bus_nr = int(device_location1[0]),
#                                 spz =  Bus.objects.get(spz=device_location1[1]),
#                         )
#                     obj.activated=True
#                     obj.file_row=i
#                     obj.name='Passenger by bus and trip report'
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


#     context = {'passenger': passenger, 'form': form}
#     return render(request, 'passenger_by_bus_and_trip_report.html', context)


from django.http import JsonResponse
from CSVS.decorators import allowed_users
from passenger_by_bus_and_trip_report.models import passenger_by_bus_and_trip_report
from index_translation.models import Routa, Bus
from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT', 'Maxcom', 'Admin'])
def passenger_view(request):
    passenger = passenger_by_bus_and_trip_report.objects.all()
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
                    df = pd.read_csv(f, delimiter=';')
                    
                    print(f"Colunas do CSV: {df.columns.tolist()}")  # Verificar as colunas do CSV
                    if 'timestamp1' not in df.columns:
                        raise Exception("A coluna 'timestamp1' não foi encontrada no arquivo CSV.")

                    # Converter 'timestamp1' para datetime com o formato 'dd/mm/yyyy'
                    df['timestamp1'] = pd.to_datetime(df['timestamp1'], format='%d/%m/%Y', errors='coerce')
                    if df['timestamp1'].isnull().any():
                        raise Exception("Algumas datas na coluna 'timestamp1' não são válidas.")

                    inicio = df['timestamp1'].min().date()
                    fim = df['timestamp1'].max().date()
                    print(f"Datas de início e fim extraídas: {inicio} a {fim}")

                    passenger_by_bus_and_trip_report.objects.filter(
                        timestamp1__range=[inicio, fim]
                    ).delete()

                    for i in range(len(df.index)):
                        row = df.iloc[i]
                        device_location1 = row['device_location1'].split(' - ', 1)
                        if len(device_location1) != 2:
                            print(f"Linha {i+1} ignorada: formato inesperado em 'device_location1'.")
                            continue
                        
                        datetime_obj = row['timestamp1'].date()
                        timestamp = parser.parse(row['timestamp']).time()
                        chout_timestamp = parser.parse(row['chout_timestamp']).time()

                        try:
                            new_record = passenger_by_bus_and_trip_report.objects.create(
                                timestamp1=datetime_obj,
                                device_location1=row['device_location1'],
                                line_reg_no1=Routa.objects.get(id=int(row['line_reg_no1'])),
                                route_reg_no1=int(row['route_reg_no1']),
                                route_reg_no=int(row['route_reg_no']),
                                customer_profile_name=row['customer_profile_name'],
                                card_uid3=row['card_uid3'],
                                timestamp=timestamp,
                                stationfrom_short_name=row['stationfrom_short_name'],
                                chout_timestamp=chout_timestamp,
                                stationto_short_name=row['stationto_short_name'],
                                money_value=float(row['money_value']),
                                transaction_count=int(row['transaction_count']),
                                money_value1=float(row['money_value1']),
                                transaction_count2=int(row['transaction_count2']),
                                money_value3=float(row['money_value3']),
                                bus_nr=int(device_location1[0]),
                                spz=Bus.objects.get(spz=device_location1[1]),
                            )
                            print(f"Novo registro criado: {new_record}")
                        except Exception as e:
                            print(f"Erro ao criar registro na linha {i+1}: {e}")
                            continue

                    obj.activated = True
                    obj.file_row = i
                    obj.name = 'Passenger by bus and trip report'
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

    context = {'passenger': passenger, 'form': form}
    return render(request, 'passenger_by_bus_and_trip_report.html', context)
