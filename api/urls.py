from django.urls import path
from . import views

app_name = "API"

urlpatterns = [
    path('', views.MainView.as_view(), name="home"),
    path('concurso/', views.ConcursoMSView.as_view(), name="concursos"),
    path('concurso/<int:ms_id>/', views.ValoresMSView.as_view(), name="concurso"),
    path('concurso/<int:ms_id>/conjuntos/', views.ConcursoConjuntoView.as_view(), name="concursoConjunto"),
    path('conjunto/', views.ConjuntoView.as_view(), name="conjunto"),
    path('conjunto/<str:url>/', views.ConjuntosView.as_view(), name="conjuntoUnico"),
    path('conjunto/<str:url>/<str:c_id>/', views.ConjuntosDetailView.as_view(), name="conjuntoUnicoDetail"),
    path('atualizar/', views.UpdateView.as_view(), name="Atualizar"),
    path('consultar/<int:v1>/<int:v2>/<int:v3>/<int:v4>/<int:v5>/<int:v6>/', views.ConsultarView.as_view(), name="Consultar6"),
    path('consultar/<int:v1>/<int:v2>/<int:v3>/<int:v4>/<int:v5>/', views.ConsultarView.as_view(), name="Consultar5"),
    path('consultar/<int:v1>/<int:v2>/<int:v3>/<int:v4>/', views.ConsultarView.as_view(), name="Consultar4"),
    path('consultar/<int:v1>/<int:v2>/<int:v3>/', views.ConsultarView.as_view(), name="Consultar3"),
    path('consultar/<int:v1>/<int:v2>/', views.ConsultarView.as_view(), name="Consultar2"),
    path('consultar/<int:v1>/', views.ConsultarView.as_view(), name="Consultar1"),
    path('consultar/', views.ConsultarDetalhesView.as_view(), name="ConsultarDetalhes"),



    #concursa personalizada (de 1 a 6 digitos)
]