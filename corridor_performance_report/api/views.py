from rest_framework.response import Response
from rest_framework import viewsets

from index_translation.models import Cooperative

from .serializers import corridor_performance_reportSerializer
from corridor_performance_report.models import corridor_performance_report
from django.db.models import Sum
from django.shortcuts import render


# from corridor_performance_report.Dash_Apps import corridor_plot
from corridor_performance_report.utils import *


class corridor_performance_reportViewSet(viewsets.ModelViewSet):
    serializer_class = corridor_performance_reportSerializer
    
    def get_queryset(self):
        operator = self.request.query_params.get('operator')
        dateI= self.request.query_params.get('dateI')
        dateF = self.request.query_params.get('dateF')

        corridor = corridor_performance_report.objects.select_related('corridor', 'line_nr', 'spz').filter(
            operator = operator,
            date__range =(dateI, dateF)).values('date','operator','spz_1','line_nr_1').order_by('spz_1'
                ).annotate(
                    passenger_count=Sum('passenger_count'),
                    qr_ticket_count=Sum('qr_ticket_count'),
                    operator_income=Sum('operator_income'),
                    amount_ticket=Sum('amount_ticket'),
            )

        # print('corridor.query: ',corridor.query)
        # print('corridor: ', corridor) 

        return corridor
    
   

def corridor_report_view(request, template_name="dashboard/report.html", **kwargs):
   
    dash_context = request.session.get("django_plotly_dash", dict())
    # dash_context['django_to_dash_context'] = "we are Dash and Abel receiving context from Django"
    # request.session['django_plotly_dash'] = dash_context

    context = {}
    return render(request, template_name=template_name, context=context)

  