from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import PrecioCoches
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def concesionario(request):
    lista = PrecioCoches.objects.all()
    salida = "<ul>\n"
    for fila in lista:
        salida += "<li><a href=concesionario/precio/" + fila.marca + ">" + fila.marca + "</a></li>\n"
    salida += "</ul>\n" 
    salida += autenticacion(request)
    return HttpResponse(salida)


@csrf_exempt
def info(request, recurso):
    if request.method == "GET":
        lista = PrecioCoches.objects.filter(marca=recurso)
        if not lista:
            return notFound(request, recurso)
        salida = " "
        for fila in lista:
            salida += "Marca: " + fila.marca + " Modelo: " + fila.modelo + " Precio: " + str(fila.precio)
    if request.method == "PUT":
        if request.user.is_authenticated():
            (modelo, precio) = request.body.split(";")
            nuevoCoche = PrecioCoches(marca=recurso, modelo=modelo, precio=precio)
            nuevoCoche.save()
            salida = ("Recurso(coche) guardado")
        else:
            salida = ("Tienes que registrarte")
    salida += autenticacion(request)
    return HttpResponse(salida)

def autenticacion(request):
    if request.user.is_authenticated():
        return ("<br>Tu usuario es: " + request.user.username + 
                "<br><a href='/admin/logout/'>Logout</a>")
    else:
        return ("<br>No esta registrado,para iniciar sesion haga ===>\n<a href='/admin/'>Login</a>")


def notFound(request, recurso):
    salida = ("La marca " + recurso + " no se encuentra en el concesionario")
    salida += autenticacion(request)
    return HttpResponseNotFound(salida)
