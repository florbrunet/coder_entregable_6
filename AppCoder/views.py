from django.shortcuts import render
import datetime
from .models import Familiar
from django.http import  HttpResponse

# Create your views here.

""" def crearFamilia(self):
    
    familia=Familiar(nombre="Eugenia", edad=49, relacion="Hermana", fecha_nacimiento=str(int(datetime.datetime.now().year)-int(49)))
    familia.save()
    texto= f"Familia creada: {familia.nombre} {familia.edad} {familia.relacion} {familia.fecha_nacimiento}"
    return HttpResponse(texto)"""

def plantilla_info(_nombre_, _edad_, _relacion_):

    familia = Familiar(
        nombre= _nombre_,
        edad= _edad_,
        relacion=_relacion_,
        fecha_nacimiento= str(int(datetime.datetime.now().year)- int(_edad_)),
    )

    familia.save()

    return familia

def crearFamilia(self):

    persona_1 =plantilla_info("Luz", 28, "prima" )
    texto_1= f"Familia creada: {persona_1.nombre} {persona_1.edad} {persona_1.relacion} {persona_1.fecha_nacimiento}\n"
    persona_2 =plantilla_info("Estefanía", 28, "hermana")
    texto_2= f"Familia creada: {persona_2.nombre} {persona_2.edad} {persona_2.relacion} {persona_2.fecha_nacimiento}\n"
    persona_3 =plantilla_info("Ginno", 28,"hermano")
    texto_3= f"Familia creada: {persona_3.nombre} {persona_3.edad} {persona_3.relacion} {persona_3.fecha_nacimiento}\n"
   
    return HttpResponse(texto_1 + texto_2 + texto_3)

