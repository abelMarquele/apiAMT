from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import conductor_sales_reportSerializer
from conductor_sales_report.models import conductor_sales_report


class conductor_sales_reportViewSet(viewsets.ModelViewSet):
    serializer_class = conductor_sales_report
    
    def get_queryset(self):
        conductor = conductor_sales_report.objects.all()
        return conductor

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            conductor = self.get_object()
            conductor.delete()
            response_message = {"message": "Conductor Sales Report foi removido com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa ação"}

        return Response(response_message)

    def create(self, request, *args, **kwargs):
        conductor_data = request.data

        new_conductor = conductor_sales_report.objects.create(
                    pergunta=Pergunta.objects.get(id=conductor_data["pergunta"]), 
                    resposta=conductor_data["resposta"]
                    # company_id = 
                    # company_name = 
                    # device = 
                    # conductor_id = 
                    # conductor_first_name = 
                    # conductor_last_name = 
                    # number = 
                    # amount = 
                    # date = 

   )

        new_conductor.save()

        serializer = conductor_sales_reportSerializer(new_conductor)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        conductor_data = self.get_object()
        data = request.data

        pergunta = Pergunta.objects.get(id=data["pergunta"])
        conductor_data.pergunta = pergunta
        conductor_data.resposta = data["resposta"]

        conductor_data.save()

        serializer = conductor_sales_reportSerializer(conductor_data)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        conductor_object = self.get_object()
        data = request.data

        try:
            pergunta = Pergunta.objects.get(id=data["pergunta"])
            conductor_object.pergunta = pergunta
        except KeyError:
            pass

        conductor_object.resposta = data.get("resposta", conductor_object.resposta)

        conductor_object.save()

        serializer = conductor_sales_reportSerializer(conductor_object)
        return Response(serializer.data)


