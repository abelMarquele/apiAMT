from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import corridor_performance_reportSerializer
from corridor_performance_report.models import corridor_performance_report


class corridor_performance_reportViewSet(viewsets.ModelViewSet):
    serializer_class = corridor_performance_report
    
    def get_queryset(self):
        corridor = corridor_performance_report.objects.all()
        return corridor

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            corridor = self.get_object()
            corridor.delete()
            response_message = {"message": "Corridor Performance Report foi removido com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa ação"}

        return Response(response_message)

    def create(self, request, *args, **kwargs):
        corridor_data = request.data

        new_corridor = corridor_performance_report.objects.create(
                    pergunta=Pergunta.objects.get(id=corridor_data["pergunta"]), 
                    resposta=corridor_data["resposta"])

        new_corridor.save()

        serializer = corridor_performance_reportSerializer(new_corridor)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        corridor_data = self.get_object()
        data = request.data

        pergunta = Pergunta.objects.get(id=data["pergunta"])
        corridor_data.pergunta = pergunta
        corridor_data.resposta = data["resposta"]

        corridor_data.save()

        serializer = corridor_performance_reportSerializer(corridor_data)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        corridor_object = self.get_object()
        data = request.data

        try:
            pergunta = Pergunta.objects.get(id=data["pergunta"])
            corridor_object.pergunta = pergunta
        except KeyError:
            pass

        corridor_object.resposta = data.get("resposta", corridor_object.resposta)

        corridor_object.save()

        serializer = corridor_performance_reportSerializer(corridor_object)
        return Response(serializer.data)


