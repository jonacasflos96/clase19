#En views vamos a crear todas las funciones que van a interactuar con el usuario
#Recuerda revisar las carpetas views y urls cuando encuentres un error, en especial las importaciones y los from
# 1) Crear una función, 2)importar la función en urls 3) Escribir el path
from django.http import HttpResponse
import datetime
from django.template import loader

def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("Bienvenido a tu album personal")
def segunda_vista(request):
    return HttpResponse("<br><br>Revive la magia de momentos detenidos en el tiempo""<br><br>Keline Studio")
def diaDeHoy(request):
      dia =datetime.datetime.now()
      documentoDeTexto = f"Hoy es dia <br> {dia}"
      return HttpResponse(documentoDeTexto)
def miNombreEs(self, nombre):
      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"
      return HttpResponse(documentoDeTexto)
def probandoTemplate(self):
    nomb=' Jonathan'
    ap=' Castillo'
    dia = datetime.datetime.now()
    notas= [1,2,3,4,5]
    diccionario={'nombre':nomb, 'apellido':ap,'fecha':dia,'notas':notas}
    #miHtml = open("C:/Users/Windows/Desktop/Curso-Python-Backend/Clase 18/Proyecto1/Proyecto1/plantillas/template1.html")
    #plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context
    #miHtml.close() #Cerramos el archivo
    #miContexto = Context(diccionario) #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
    #documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento
    plantilla= loader.get_template('Template1.html')
    documento = plantilla.render(diccionario) #Aca renderizamos la plantilla en documento
    return HttpResponse(documento)

