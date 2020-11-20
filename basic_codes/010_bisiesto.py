#! /usr/bin/env python
# -*- coding: utf-8 -*-

def es_bisiesto():
	try:
		ano=int(anoAsString)
		if (ano%4==0 or ano%400==0) and ano%100!=0:
			print("Es bisiesto")
		else:
			print("No es bisiesto")
	except ValueError as e:
		print("El ano debe ser un numero")
		print(e)

anoAsString=input("Inserte el ano que desea saber si es bisiesto  -  ")
es_bisiesto()
