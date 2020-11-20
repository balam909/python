#! /usr/bin/env python
# -*- coding: utf-8 -*-
def filter_list(list,minLengthSize):
	"""Una funcion para filtrar las palabras de una lista que no tengan mas de 'n' caracteres"""
	result=[]
	for att in list[:]:
		if len(att)>minLengthSize:
			result.append(att)
	return result

def parse_listOfObjects_to_listOfStrings(list):
	"""Una funcion para convertir una lista de objectos en una lista de strings"""
	result=[]
	for item in list[:]:
		result.append(str(item))
	return result

def get_valid_integer(inputValue):
	try:
		return int(inputValue)
	except ValueError as e:
		print("El valor para el numero maximo de caracteres soportados para el filtrado debe ser un numero")
		print(e)
		return -1

messageList="Proporcione la lista de la cual se busca encontrar la cadena mas larga, debe estar en el formato: palabra1,palabra2,palabra3...palabraN; ejemplo: unapalabra,otrapalabra,aquellapalabra,maspalabras  -  "
messageLength="Proporciona la longitud que debe sobrepasar una palabra para evitar ser filtrada  -  "
listAsString=input(messageList)
minLengthSize=get_valid_integer(input(messageLength))
if len(listAsString)<=0:
	print("No se ha proporcionado una lista")
elif minLengthSize<=-1:
	print("No se ha proporcionado un numero valido para el filtrado de palabras")
else:
	listOfStrings=listAsString.split(',')
	list=parse_listOfObjects_to_listOfStrings(listOfStrings)
	if len(list)>0:
		print("Las palabras que cuentan con mas de: ", minLengthSize, "caracteres son: ",filter_list(list,minLengthSize))
