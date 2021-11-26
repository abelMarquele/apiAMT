from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import settlement_file_operatorSerializer
from settlement_file_operator.models import settlement_file_operator

from django.shortcuts import render
from CSVS.forms import CsvModelForm
from dateutil import parser
from CSVS.models import Csv
import csv

class settlement_file_operatorViewSet(viewsets.ModelViewSet):
    serializer_class = settlement_file_operator
    
    def get_queryset(self):
        settlement_file = settlement_file_operator.objects.all()
        return settlement_file

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            settlement_file = self.get_object()
            settlement_file.delete()
            response_message = {"message": "O Settlement File Operator foi removido com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa ação"}

        return Response(response_message)

    def create(self, request, *args, **kwargs):
        settlement_file_data = request.data

        new_settlement_file = settlement_file_operator.objects.create(
                    pergunta=Pergunta.objects.get(id=settlement_file_data["pergunta"]), 
                    resposta=settlement_file_data["resposta"]
                    
                    # transaction_type = 
                    # money_value = 
                    # transaction_count = 
                    # money_value4 = 
                    # transaction_type2 = 
                    # Textbox217 = 
                    # Textbox214 =
                    # Textbox218 = 
                    # transaction_count3 = 
                    # Textbox74 = 
                    # Textbox88 = 
                    # transaction_count4 = 
                    # Textbox98 = 
                    # Textbox100 =
                    # rank = 
                    # carrier_name = 
                    # cooperatives = 
                    # money_value3 = 
                    # Textbox220 = 
                    # transaction_count2 = 
                    # Textbox76 = 
                    # Textbox77 = 
                            )


        new_settlement_file.save()

        serializer = settlement_file_operatorSerializer(new_settlement_file)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        settlement_file_data = self.get_object()
        data = request.data

        pergunta = Pergunta.objects.get(id=data["pergunta"])
        settlement_file_data.pergunta = pergunta
        settlement_file_data.resposta = data["resposta"]

        settlement_file_data.save()

        serializer = settlement_file_operatorSerializer(settlement_file_data)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        settlement_file_object = self.get_object()
        data = request.data

        try:
            pergunta = Pergunta.objects.get(id=data["pergunta"])
            settlement_file_object.pergunta = pergunta
        except KeyError:
            pass

        settlement_file_object.resposta = data.get("resposta", settlement_file_object.resposta)

        settlement_file_object.save()

        serializer = settlement_file_operatorSerializer(settlement_file_object)
        return Response(serializer.data)


def settlement_file_upload_file_view(request):
	form = CsvModelForm(request.POST or None, request.FILES or None)
	if form.is_valid(): 	
		form.save()
		form = CsvModelForm()
		obj = Csv.objects.get(activated=False)
		with open(obj.file_name.path, 'r') as f:
			reader = csv.reader(f)
			for i, row in enumerate(reader):
				if i>10:
					pass
				else:
					datetime_obj = parser.parse(row[0])						
					settlement_file_operator.objects.create(
					    date = datetime_obj,
                        corridor = int(row[1]),
                        line_nr = int(row[2]),
                        bus_nr = int(row[3]),
                        spz = row[4],
                        cooperative = int(row[5]),
                        operator = row[6],
                        passenger_count = int(row[7]),
                        luggage_count = int(row[8]),
                        qr_ticket_count = int(row[9]),
                        amount_ticket = float(row[10]),
                        amount_luggage = float(row[11]),
                        maxcom_income = float(row[12]),
                        amt_income = float(row[13]),
                        operator_income = float(row[14]),
                        
                        transaction_type = row[0],
                        money_value = float(row[1]),
                        transaction_count = int(row[2]),
                        money_value4 = float(row[3]),
                        transaction_type2 = int(row[4]),
                        Textbox217 = int(row[5]),
                        Textbox214 = int(row[6]),
                        Textbox218 = int(row[7]), 
                        transaction_count3 = int(row[8]),
                        Textbox74 = float(row[9]),
                        Textbox88 = float(row[10]),
                        transaction_count4 = int(row[11]),
                        Textbox98 = float(row[12]),
                        Textbox100 = float(row[13]),
                        rank = int(row[14]),
                        carrier_name = row[15],
                        cooperatives = row[16],
                        money_value3 = float(row[17]),
                        Textbox220 = float(row[18]),
                        transaction_count2 = float(row[19]),
                        Textbox76 = float(row[20]),
                        Textbox77 = float(row[21]),
                        
					)
					
			obj.activated = True
			obj.save()
			#  index  upload
	return render(request, 'settlement_file_operator.html', {'form': form})






