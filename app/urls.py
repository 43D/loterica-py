from django.urls import path
from . import views

app_name = "APP"

urlpatterns = [
    path('', views.homeView, name="home"),
    path('concurso/', views.concursosView, name="concursos"),
    path('concurso/<int:id>', views.concursoView, name="concurso"),
    #path('conjunto/<int:id>', views.concursoView, name="conjunto"),

]
