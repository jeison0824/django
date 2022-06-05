from multiprocessing import context
from re import template
from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self ,nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def Saludo (request):
    p1=Persona("Profesor Juan", "Díaz")
    #nombre="Juan"
    #apellido = "Diaz"
    temasdelcurso= ["Plantillas","Modelos","Formularios","Vistas","Despliegues"]
    ahora = datetime.datetime.now()
    doc_externo=open("C:/Users/sebas/OneDrive/Documentos/ProyectoDjango/Proyecto1/Plantillas/miplantilla.html")
    plt = Template(doc_externo.read())
    ctx= Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasdelcurso})
    documento = plt.render(ctx)
    return HttpResponse(documento)
    return HttpResponse(documento)

def dameFecha(request):

    fecha_actual = datetime.datetime.now()

   

def calcEdad(request,edad, agno):
  
    periodo = agno - 2022
    edadFutura = edad + periodo
    documento = """<html>
    <body>
    <h1>
    en el año  %s tendras %s
    </h1>
    </boody>
    </html>""" % (agno, edadFutura)
    return HttpResponse(documento)
