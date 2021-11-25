from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import settlement_file_operatorViewSet

router = DefaultRouter()
router.register('settlement_file_operator', settlement_file_operatorViewSet, basename='settlement_file_operator')

urlpatterns = [
    url('', include(router.urls))
]
