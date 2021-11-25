from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import passenger_by_bus_and_trip_reportSerializer
from passenger_by_bus_and_trip_report.models import passenger_by_bus_and_trip_report


class passenger_by_bus_and_trip_reportViewSet(viewsets.ModelViewSet):
    serializer_class = passenger_by_bus_and_trip_report
    
    def get_queryset(self):
        passenger = passenger_by_bus_and_trip_report.objects.all()
        return passenger

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            passenger = self.get_object()
            passenger.delete()
            response_message = {"message": "Passenger by bus and trip report foi removido com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa ação"}

        return Response(response_message)

    def create(self, request, *args, **kwargs):
        passenger_data = request.data

        new_passenger = passenger_by_bus_and_trip_report.objects.create(
                    pergunta=Pergunta.objects.get(id=passenger_data["pergunta"]), 
                    resposta=passenger_data["resposta"])

        new_passenger.save()

        serializer = passenger_by_bus_and_trip_reportSerializer(new_passenger)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        passenger_data = self.get_object()
        data = request.data

        pergunta = Pergunta.objects.get(id=data["pergunta"])
        passenger_data.pergunta = pergunta
        passenger_data.resposta = data["resposta"]

        passenger_data.save()

        serializer = passenger_by_bus_and_trip_reportSerializer(passenger_data)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        passenger_object = self.get_object()
        data = request.data

        try:
            pergunta = Pergunta.objects.get(id=data["pergunta"])
            passenger_object.pergunta = pergunta
        except KeyError:
            pass

        passenger_object.resposta = data.get("resposta", passenger_object.resposta)

        passenger_object.save()

        serializer = passenger_by_bus_and_trip_reportSerializer(passenger_object)
        return Response(serializer.data)


