#! /usr/bin/env python

def ingresa_nombre_ano_nacimiento(personas=3):
	personasValidadas=0
	result={}
	while personasValidadas<personas:
		nombre=input("Inserte el nombre de la Persona: ")
		anoNacimientoAsString=input("Ingrese el ano de nacimiento de la Persona: ")
		try:
			edad=int(anoNacimientoAsString)
			personasValidadas+=1
			result[nombre]=edad
		except ValueError as e:
			print("En ano de nacimeinto ingresado no es valido, por favor, intente nuevamente...")
			print(e)
	return result

anoActual=input("Ingrese el ano en que nos encontramos: ")
personasNacimiento=ingresa_nombre_ano_nacimiento()
for persona in personasNacimiento:
	print(persona, "cumplira",int(anoActual)-int(personasNacimiento[persona]),"este ano")
