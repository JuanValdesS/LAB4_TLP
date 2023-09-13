from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    title = "Home"
    page = "<html>"
    page+= "<head>"
    page+= "<title>"+title+"</title>"
    page+= "</head>"
    page+= "<body>"
    page+= "<h1>Inicio</h1>"
    page+= "</body>"
    page+= "<html>"

    return HttpResponse(page)

def Carreras(request):
    title = "Carreras"
    page = "<html>"
    page+= "<head>"
    page+= "<title>"+title+"</title>"
    page+= "</head>"
    page+= "<body>"
    page+= "<h1>"+title+"</h1>"
    page+= "</body>"
    page+= "<html>"

    return HttpResponse(page)

def Docentes(request):
    title = "Docentes"
    page = "<html>"
    page+= "<head>"
    page+= "<title>"+title+"</title>"
    page+= "</head>"
    page+= "<body>"
    page+= "<h1>"+title+"</h1>"
    page+= "</body>"
    page+= "<html>"

    return HttpResponse(page)