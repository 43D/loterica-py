from django.urls import path
from . import views

app_name = "APP"

urlpatterns = [
    path('', views.homeView, name="home"),
    path('concurso/', views.concursosView, name="concursos"),
    path('concurso/<int:id>', views.concursoViewID, name="concursoID"),
    path('conjunto/<str:op>', views.conjuntoView, name="conjunto"),
    path('docs/', views.docsView, name="docs"),

]
