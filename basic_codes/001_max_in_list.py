#! /usr/bin/env python
# -*- coding: utf-8 -*-
def max_in_list(list):
	"""Una funcion para encontrar el numero maximo de una lista de enteros"""
	max=list[0]
	for att in list[1:]:
		if att>max:
			max=att
	return max

def parse_listOfStrings_to_listOfIntegers(list):
	"""Una funcion para convertir una lista de string en una lista de enteros"""
	result=[]
	error=""
	try:
		for item in list[:]:
			result.append(int(item))
		return result
	except ValueError as e:
		print("La lista debe contener unicamente enteros positivos y negativos")
		print(e)
		return []


message="Proporcione la lista de la cual se busca encontrar el numero maximo, debe estar en el formato: number1,number2,number3...numberN; ejemplo: 23,5456,123,4653,-123 -  "
listAsString=input(message)
if len(listAsString)>0:
	listOfStrings=listAsString.split(',')
	list=parse_listOfStrings_to_listOfIntegers(listOfStrings)
	if len(list)>0:
		print("El numero maximo es: ",max_in_list(list))
else:
	print("No se ha proporcionado una lista")
