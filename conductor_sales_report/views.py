# from django.http import JsonResponse
# from CSVS.decorators import allowed_users
# from conductor_sales_report.models import conductor_sales_report
# from index_translation.models import Bus

# from django.shortcuts import render
# from CSVS.forms import CsvModelForm
# from dateutil import parser
# from CSVS.models import Csv
# import pandas

# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import MultipleObjectsReturned

# @login_required(login_url='csvs:login-view')
# @allowed_users(allowed_roles=['AMT','Maxcom','Admin'])
# def conductor_view(request):
#     conductor = conductor_sales_report.objects.all()
#     form = CsvModelForm(request.POST or None, request.FILES or None)

#     if form.is_valid(): 	
#         form.save()
#         form = CsvModelForm()
#         try:
#             obj = Csv.objects.get(activated=False)
#             status = 200
#             msg = 'Documento preparado com sucesso!'
#             with open(obj.file_name.path, 'r' , encoding="cp1252") as f:
#                 pd = pandas.read_csv(f)
#                 inicio = parser.parse(pd.Date.min())
#                 fim = parser.parse(pd.Date.max())
#                 conductor_sales_report.objects.filter(
#                             date__range =[inicio, fim]
#                 ).delete()

#                 try:
#                     for i in range(len(pd.index)):
#                         datetime_obj = parser.parse(pd.Date[i])						
#                         conductor_sales_report.objects.create(
#                             company_id	= int(pd['Company ID'][i]),
#                             company_name = pd['Company Name'][i],	
#                             device	= pd.Device[i],
#                             conductor_id = int(pd['Conductor ID'][i]),	
#                             conductor_first_name = Bus.objects.get(spz=pd['Conductor First Name'][i]),
#                             conductor_last_name = pd['Conductor Last Name'][i],
#                             number	= int(pd.Number[i]),
#                             amount	= float(pd.Amount[i]),
#                             date = datetime_obj,
#                         )

#                     obj.activated = True
#                     obj.file_row=i
#                     obj.name='Conductor Sales Report'
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

#     context = {'conductor': conductor, 'form': form}
#     return render(request, 'conductor_sales_report.html', context)




from django.http import JsonResponse
from CSVS.decorators import allowed_users
from conductor_sales_report.models import conductor_sales_report
from index_translation.models import Bus
from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned

@login_required(login_url='csvs:login-view')
@allowed_users(allowed_roles=['AMT', 'Maxcom', 'Admin'])
def conductor_view(request):
    conductor = conductor_sales_report.objects.all()
    form = CsvModelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        form = CsvModelForm()
        try:
            obj = Csv.objects.get(activated=False)
            status = 200
            msg = 'Documento preparado com sucesso!'
            try:
                df = pd.read_csv(obj.file_name.path, encoding="cp1252", sep=';')
                print(f"Colunas do CSV: {df.columns.tolist()}")  # Imprime os nomes das colunas

                if 'Date' not in df.columns:
                    raise Exception("A coluna 'Date' não foi encontrada no arquivo CSV.")

                inicio = parser.parse(df['Date'].min())
                fim = parser.parse(df['Date'].max())
                print(f"Datas de início e fim extraídas: {inicio} a {fim}")

                # Apagar registros dentro do intervalo de datas
                delete_count = conductor_sales_report.objects.filter(
                    date__range=[inicio, fim]
                ).delete()
                print(f"Registros deletados: {delete_count}")

                for i in range(len(df.index)):
                    datetime_obj = parser.parse(df['Date'][i])
                    new_record = conductor_sales_report.objects.create(
                        company_id=int(df['Company ID'][i]),
                        company_name=df['Company Name'][i],
                        device=df['Device'][i],
                        conductor_id=int(df['Conductor ID'][i]),
                        conductor_first_name=Bus.objects.get(spz=df['Conductor First Name'][i]),
                        conductor_last_name=df['Conductor Last Name'][i],
                        number=int(df['Number'][i]),
                        amount=float(df['Amount'][i]),
                        date=datetime_obj,
                    )
                    print(f"Novo registro criado: {new_record}")

                obj.activated = True
                obj.file_row = i
                obj.name = 'Conductor Sales Report'
                obj.save()

                msg = 'A ação foi realizada com sucesso!'
            except Exception as e:
                print(f"Erro ao processar o arquivo CSV: {e}")
                msg = 'Problema de integridade de dados!'
                status = 500

        except MultipleObjectsReturned:
            Csv.objects.filter(activated=False).delete()
            msg = 'Resolvendo problema de documento com várias referências. Tente novamente!'
            status = 400
        except Exception as e:
            print(f"Erro ao abrir o arquivo CSV: {e}")
            Csv.objects.filter(activated=False).delete()
            msg = 'Documento errado ou erro interno do servidor!'
            status = 500

        return JsonResponse({'message': msg}, status=status)

    context = {'conductor': conductor, 'form': form}
    return render(request, 'conductor_sales_report.html', context)
