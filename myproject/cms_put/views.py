from django.shortcuts import render
from django.http import HttpResponse
from cms_put.models import Pages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def pagina(request, identificador):
    try:
        pag = Pages.objects.get(id = int(identificador))
        respuesta = pag.page
    except Pages.DoesNotExist:
        respuesta = "No se encuentra en la base de datos"
    return HttpResponse(respuesta)
def mostrar(resquest):
    lista=Pages.objects.all()
    respuesta ="<ol>"
    for pag in lista:
        respuesta +='<li><a href="' + str(pag.id) +'">' + pag.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)
@csrf_exempt
def pagina_nueva(request, nombre, contenido):
    if request.method == "GET":
        pag_nueva = Pages(name = nombre, page = contenido)
        pag_nueva.save()
    elif request.method == "PUT" or request.method == "POST":
        pag_nueva = Pages(name= nombre, page = request.body)
        pag_nueva.save()
    return HttpResponse("La página ha sido añadida")
