#! /usr/bin/env python

import re

lista=["Carolina","Juan","Pedro","Luis","Roberto","Cecilia","Julieta","Maria","Rodrigo","Alejandro","Guillermo","Ana","Antonio","Balam","Ernesto","Rodolfo"]
print("Esta es la lista de estudiantes registrados",lista)

while True:
	letra=input("Con que letra debe empezar el nombre de los estudiantes que quieres filtrar?")
	validator=re.search("[a-zA-Z]{1}",letra)
	if len(letra)!=1 or validator==None:
		print("Se debe ingresar solamente una letra")
		continue;
	else:
		break;

result=[]
for item in lista:
	nombre=str(item)
	if nombre[0].lower()==letra.lower():
		result.append(nombre)

if len(result) < 1:
	print("No se han encontrado resultados para tu busqueda")
else:
	print("Esta es la lista de alumnos encontrados: ",result)
