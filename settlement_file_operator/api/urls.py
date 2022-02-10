from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
#from .views import settlement_file_operatorViewSet
from .views import settlement_file_upload_file_view


# router = DefaultRouter()
# router.register('settlement_file_operator', settlement_file_operatorViewSet, basename='settlement_file_operator')


urlpatterns = [
   # url('', include(router.urls)),
    path('settlement_file/',settlement_file_upload_file_view, name='settlement_file-view'),
]

