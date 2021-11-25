"""apiAMT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CSVS.urls', namespace='csvs')),
    path('capacity_summary_report-app/', include('capacity_summary_report.api.urls')),
    path('conductor_sales_report-app/', include('conductor_sales_report.api.urls')),
    path('corridor_performance_report-app/', include('corridor_performance_report.api.urls')),
    path('index_translation-app/', include('index_translation.api.urls')),
    path('passenger_by_bus_and_trip_report-app/', include('passenger_by_bus_and_trip_report.api.urls')),
    path('settlement_file_operator-app/', include('settlement_file_operator.api.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)