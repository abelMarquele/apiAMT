from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from capacity_summary_report.views import capacity_view
#from .views import capacity_upload_file_view
from .views import capacity_summary_reportViewSet

# router = DefaultRouter()
# router.register('capacity_summary_report', capacity_summary_reportViewSet, basename='capacity_summary_report')

urlpatterns = [
    #url('', include(router.urls)),
    path('capacity/',capacity_view, name='capacity-view'),
]

