#! /usr/bin/env python

def ingresa_edades(edades=10):
	edadesValidadas=0
	result=[]
	while edadesValidadas<edades:
		edadAsString=input("Inserte la edad de una persona: ")
		try:
			edad=int(edadAsString)
			edadesValidadas+=1
			result.append(edad)
		except ValueError as e:
			print("La edad ingresada debe ser un numero...")
			print(e)
	return result

def remueve_menores(edades, minoriaEdad=20):
	mayores=[]
	for edad in edades:
		if edad > minoriaEdad:
			mayores.append(edad)
	return mayores

edades=ingresa_edades()
mayores=remueve_menores(edades)
print("Las edades proporcionadas con mayoria de edad son: ",mayores)
