from django.http import HttpResponse
from django.template import Template,Context,loader
import datetime
class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        
def vista(request):
    p1=Persona("Juan","Diaz")

    temas=["Plantillas","Modelos","Formularios","Vistas"]

    fecha_actual=datetime.datetime.now()

    doc_externo=loader.get_template("index.html")

    documento=doc_externo.render({
        "nombre_persona":p1.nombre,
        "apellido_persona":p1.apellido,
        "fecha_actual":fecha_actual,
        "temas":temas
        })
    
    return HttpResponse(documento)
def algo(request):
    return HttpResponse("saloe ;V")
def fecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
        <body>
            <h1> Fecha y hora actuales  %s</h1>
        </body>
    </html>"""%fecha_actual
    return HttpResponse(documento)
def edad(request,edad,ano):
    
    periodo=ano-2020
    edad_futura=edad+periodo
    documento="""<html>
        <body>
            <h2> En el año %s tendras %s años</h2>
        </body>
    </html>"""%(ano,edad_futura)
    return HttpResponse(documento)