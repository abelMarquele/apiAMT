from rest_framework.response import Response
from rest_framework import viewsets

from index_translation.models import Cooperative, Corridor, Routa
from .serializers import corridor_performance_reportSerializer
from corridor_performance_report.models import corridor_performance_report

from django.shortcuts import render

from django.db.models import Sum


class corridor_performance_reportViewSet(viewsets.ModelViewSet):
    serializer_class = corridor_performance_reportSerializer
    
    def get_queryset(self):
        corridor = corridor_performance_report.objects.all()
        return corridor
    
    def retrieve(self, request, *args, **kwargs):

        params = kwargs
        params_list = params['pk'].split('&')
        print(params_list)
        
        corridor = corridor_performance_report.objects.filter(
            operator = params_list[0],
            date__range =(params_list[1], params_list[2])
            ).values('date','operator','spz').order_by('spz'
                ).annotate(
                    passenger_count=Sum('passenger_count'),
                    qr_ticket_count=Sum('qr_ticket_count'),
                    operator_income=Sum('operator_income'),
                    amount_ticket=Sum('amount_ticket'),
            )
        #print(corridor.query) 
        #print(corridor) 
        serializer = corridor_performance_reportSerializer(corridor, many=True)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            corridor = self.get_object()
            corridor.delete()
            response_message = {"message": "Corridor Performance Report foi removido com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa ação"}

        return Response(response_message)

    # def create(self, request, *args, **kwargs):
    #     corridor_data = request.data

    #     new_corridor = corridor_performance_report.objects.create(
    #                 pergunta=Pergunta.objects.get(id=corridor_data["pergunta"]), 
    #                 resposta=corridor_data["resposta"],
                    
    #                 # company_id	= int(row[0]),
	# 				# company_name = row[1],	
	# 				# device	= row[2],
	# 				# conductor_id = int(row[3]),	
	# 				# conductor_first_name = row[4],
	# 				# conductor_last_name = row[5],
	# 				# number	= int(row[6]),
	# 				# amount	= row[7],
	# 				# date = datetime_obj,
    #                     )

    #     new_corridor.save()

    #     serializer = corridor_performance_reportSerializer(new_corridor)
    #     return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     corridor_data = self.get_object()
    #     data = request.data

    #     pergunta = Pergunta.objects.get(id=data["pergunta"])
    #     corridor_data.pergunta = pergunta
    #     corridor_data.resposta = data["resposta"]

    #     corridor_data.save()

    #     serializer = corridor_performance_reportSerializer(corridor_data)
    #     return Response(serializer.data)

    # def partial_update(self, request, *args, **kwargs):
    #     corridor_object = self.get_object()
    #     data = request.data

    #     try:
    #         pergunta = Pergunta.objects.get(id=data["pergunta"])
    #         corridor_object.pergunta = pergunta
    #     except KeyError:
    #         pass

    #     corridor_object.resposta = data.get("resposta", corridor_object.resposta)

    #     corridor_object.save()

    #     serializer = corridor_performance_reportSerializer(corridor_object)
    #     return Response(serializer.data)

class corridor_performance_reportIDViewSet(viewsets.ModelViewSet):
    serializer_class = corridor_performance_reportSerializer
        
    def retrieve(self, request, *args, **kwargs):

        params = kwargs
        params_list = params['pk'].split('&')
        print(params_list)
        
        corridor = corridor_performance_report.objects.filter(
            operator = params_list[0],
            date__range =(params_list[1], params_list[2]),
            spz = params_list[3]
            ).values('date','operator','spz').order_by('spz'
                ).annotate(
                    passenger_count=Sum('passenger_count'),
                    qr_ticket_count=Sum('qr_ticket_count'),
                    operator_income=Sum('operator_income'),
                    amount_ticket=Sum('amount_ticket'),
            )
        #print(corridor.query) 
        print(corridor) 
        serializer = corridor_performance_reportSerializer(corridor, many=True)

        return Response(serializer.data)