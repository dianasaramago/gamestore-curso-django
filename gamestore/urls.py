from django.contrib import admin
from django.urls import path, include

from rest_framework import routers 

from core import views

router = routers.DefaultRouter()
router.register(r'generos', views.GeneroViewSet)
router.register(r'desenvolvedora', views.DesenvolvedoraViewSet)
router.register(r'plataforma', views.PlataformaViewSet)
router.register(r'jogo', views.JogoViewSet)
router.register(r'compra', views.CompraViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste),
    path('pag2/', views.teste2),
    path('generos-class/', views.GeneroView.as_view()),
    path('generos-class/<int:id>/', views.GeneroView.as_view()),
    path('generos-apiview/', views.GeneroList.as_view()),
    path('generos-apiview/<int:id>/', views.GeneroDetail.as_view()),
    path('generos-generic/', views.GeneroListGeneric.as_view()),
    path('generos-generic/<int:id>/', views.GeneroDetailGeneric.as_view()),
    path('', include(router.urls))
]
