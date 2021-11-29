from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import cooperativeViewSet, corridorViewSet, routaViewSet, index_translation_view, cooperative_view, corridor_view, routa_view

router = DefaultRouter()
router.register('cooperative', cooperativeViewSet, basename='cooperative')
router.register('corridor', corridorViewSet, basename='corridor')
router.register('routa', routaViewSet, basename='routa')

urlpatterns = [
    url('', include(router.urls)),
    path('index_translation/',index_translation_view, name='index_translation-view'),
    path('index_cooperative/',cooperative_view, name='index_cooperative-view'),
    path('index_corridor/',corridor_view, name='index_corridor-view'),
    path('index_routa/',routa_view, name='index_routa-view'),


]
