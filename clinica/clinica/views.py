from django.http import HttpResponse
import datetime
from django.template import Template,Context

def ventana(request):  #Primera vista 

  
    fecha_hora=datetime.datetime.now()
    lista=["David", "Fernando","Prueba","Exito"]

    doc_externo=open("C:/Users/david/Desktop/Examen/clinica/clinica/Platillas/ventanaclinica.html")
    plantilla=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"momento":fecha_hora, "listas":lista})
    formato=plantilla.render(ctx)

    return HttpResponse(formato)

def cita(request):  #Primera vista 

  
    fecha_hora=datetime.datetime.now()
    lista=["Moises", "Fernando","Prueba","Exito"]

    doc_externo=open("C:/Users/david/Desktop/Examen/clinica/clinica/Platillas/ventanacita.html")
    plantilla=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"momento":fecha_hora, "listas":lista})
    formato=plantilla.render(ctx)

    return HttpResponse(formato)

#def ventana(request):  #Primera vista 

    #return HttpResponse("Ingrese datos del paciente")