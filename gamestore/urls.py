from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers 

from core import views

router = routers.DefaultRouter()
router.register(r'generos', views.GeneroViewSet)
router.register(r'desenvolvedoras', views.DesenvolvedoraViewSet)
router.register(r'plataformas', views.PlataformaViewSet)
router.register(r'jogos', views.JogoViewSet)
router.register(r'compras', views.CompraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
     # OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # Autenticação
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Outros Endpoints
    path('teste/', views.teste),
    path('pag2/', views.teste2),
    path('generos-class/', views.GeneroView.as_view()),
    path('generos-class/<int:id>/', views.GeneroView.as_view()),
    path('generos-apiview/', views.GeneroList.as_view()),
    path('generos-apiview/<int:id>/', views.GeneroDetail.as_view()),
    path('generos-generic/', views.GeneroListGeneric.as_view()),
    path('generos-generic/<int:id>/', views.GeneroDetailGeneric.as_view()),
    path('api/', include(router.urls))
]
