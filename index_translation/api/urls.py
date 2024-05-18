from django.urls import path
from index_translation.views import assign_bus_view, assign_view, bus_view, cooperative_view, cooperative_bus_view, corridor_view, manager_view, routa_view



urlpatterns = [
    path('index_cooperative/',cooperative_view, name='index_cooperative-view'),
    path('index_corridor/',corridor_view, name='index_corridor-view'),
    path('index_routa/',routa_view, name='index_routa-view'),
    path('index_bus/',bus_view, name='index_bus-view'),
    path('index_manager/',manager_view, name='index_manager-view'),
    path('assign_bus/<str:pk>/',assign_bus_view, name='assign_bus-view'), 
    path('cooperative_bus/<str:pk>/',cooperative_bus_view, name='cooperative_bus-view'),  
    path('index_assign/',assign_view, name='index_assign-view'),

]
