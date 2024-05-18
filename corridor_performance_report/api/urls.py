from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from corridor_performance_report.views import corridor_view
from .views import corridor_performance_reportViewSet, corridor_report_view

router = DefaultRouter()
router.register('corridor_performance_report', corridor_performance_reportViewSet, basename='corridor_performance_report')

app_name = 'corridor_performance_report'

urlpatterns = [
    path('', include(router.urls)),
    path('corridor/', corridor_view, name='corridor-view'),
    path('report/', corridor_report_view, name='report-view'),
]

