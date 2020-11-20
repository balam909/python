#! /usr/bin/env python
# -*- coding: utf-8 -*-

def cuenta_mayusculas(cadena):
	"""La funcion para contar la cantidad de letras mayusculas que contiene una palabra"""
	result=0
	for caracter in cadena[:]:
		if caracter.upper()==caracter:
			result+=1
	return result

palabra=input("Incerte la cadena de caracteres a evaluar  -  ")
palabra=palabra.replace(" ","")
if len(palabra)==0:
	print("No se ha ingresado ninguna cadena de caracteres")
else:
	print("La cadena ingresada cuenta con",cuenta_mayusculas(palabra),"letras mayusculas")
	
