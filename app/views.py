from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

def homeView(request):
    return render(request,"index.html")

def concursosView(request):
    return render(request,"concurso/index.html")

def concursoViewID(request, id):
    return render(request, "concurso/id.html", {'id':id})