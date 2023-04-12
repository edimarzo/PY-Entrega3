from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('crear-agentes/', views.crear_agente, name='crear_agente'),
    path('agentes/', views.lista_agentes, name='listar_agente'),
    
]
