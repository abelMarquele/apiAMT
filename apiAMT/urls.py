from django.views.static import serve
from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view as get_drf_yasg_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views

schema_view = get_drf_yasg_view(
   openapi.Info(
      title="AMT API Docs",
      default_version='v1',
      description=(
          "Bem-vindo à API AMT. A API foi criada para permitir que você crie um aplicativo ou integração funcional "
          "de maneira rápida e fácil. Sabemos por experiência - essas são as APIs que alimentam o aplicativo Famba. "
          "O ecossistema de desenvolvedores que criam integrações em cima das APIs é forte e diversificado, variando de "
          "provedores de webinars a CRMs e mídias sociais. Todas as APIs da AMT são organizadas em torno do REST - se você "
          "já interagiu com uma API REST, muitos dos conceitos serão familiares para você. Todas as chamadas de API para o "
          "Famba devem ser feitas para o domínio base https://mz-myapi.herokuapp.com. Usamos muitos recursos HTTP padrão, como "
          "verbos HTTP, que podem ser entendidos por muitos clientes HTTP. JSON será retornado em todas as respostas, incluindo "
          "erros. As APIs são projetadas para ter URLs previsíveis e diretas e para usar códigos de resposta HTTP para indicar erros de API."
      ),
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="aamarquele@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

handler400 = 'apiAMT.views.error_400_view'
handler403 = 'apiAMT.views.error_403_view'
handler404 = 'apiAMT.views.error_404_view'
handler500 = 'apiAMT.views.error_500_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include(('CSVS.urls'), namespace='csvs')),
    path('capacity_summary_report-app/', include('capacity_summary_report.api.urls')),
    path('conductor_sales_report-app/', include('conductor_sales_report.api.urls')),
    path('corridor_performance_report-app/', include('corridor_performance_report.api.urls')),
    path('index_translation-app/', include('index_translation.api.urls')),
    path('passenger_by_bus_and_trip_report-app/', include('passenger_by_bus_and_trip_report.api.urls')),
    path('settlement_file_operator-app/', include('settlement_file_operator.api.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
