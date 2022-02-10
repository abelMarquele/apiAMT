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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from django.contrib.auth.views import login
# from django.contrib.auth.views import logout
#from django.contrib.auth import views as auth_views
# from myapp.views import home, contact django.contrib.auth.views.login

schema_view = get_schema_view(
   openapi.Info(
      title="AMT API Docs",
      default_version='v1',
      description="Bem-vindo à API AMT."+ "\n"+
        " A API foi criada para permitir que você crie um aplicativo ou integração funcional de maneira rápida e fácil."+
        " Sabemos por experiência - essas são as APIs que alimentam o aplicativo Famba."+
        " O ecossistema de desenvolvedores que criam integrações em cima das APIs é forte e diversificado, variando de provedores de webinars a CRMs e mídias sociais."+ "\n"+
        "\n"+
        " Todas as APIs da AMT são organizadas em torno do REST - se você já interagiu com uma API REST, muitos dos conceitos serão familiares para você."+
        " Todas as chamadas de API para o Famba devem ser feitas para o domínio base https://apiamt.herokuapp.com. "+
        " Usamos muitos recursos HTTP padrão, como verbos HTTP, que podem ser entendidos por muitos clientes HTTP. "+
        " JSON será retornado em todas as respostas, incluindo erros."+ 
        " As APIs são projetadas para ter URLs previsíveis e diretas e para usar códigos de resposta HTTP para indicar erros de API.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="aamarquele@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include('CSVS.urls', namespace='csvs')),

    path('capacity_summary_report-app/', include('capacity_summary_report.api.urls')),
    path('conductor_sales_report-app/', include('conductor_sales_report.api.urls')),
    path('corridor_performance_report-app/', include('corridor_performance_report.api.urls')),
    path('index_translation-app/', include('index_translation.api.urls')),
    path('passenger_by_bus_and_trip_report-app/', include('passenger_by_bus_and_trip_report.api.urls')),
    path('settlement_file_operator-app/', include('settlement_file_operator.api.urls')),

    # path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)