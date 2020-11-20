#! /usr/bin/env python
# -*- coding: utf-8 -*-
def max_in_list(list):
	"""Una funcion para encontrar la cadena mas larga en una lista de strings"""
	max=list[0]
	for att in list[1:]:
		if len(att)>len(max):
			max=att
		elif len(att)==len(max):
			max=max+','+att
	return max

def parse_listOfObjects_to_listOfStrings(list):
	"""Una funcion para convertir una lista de objectos en una lista de strings"""
	result=[]
	for item in list[:]:
		result.append(str(item))
	return result

message="Proporcione la lista de la cual se busca encontrar la cadena mas larga, debe estar en el formato: palabra1,palabra2,palabra3...palabraN; ejemplo: unapalabra,otrapalabra,aquellapalabra,maspalabras  -  "
listAsString=input(message)
if len(listAsString)>0:
	listOfStrings=listAsString.split(',')
	list=parse_listOfObjects_to_listOfStrings(listOfStrings)
	if len(list)>0:
		print("La palabra(s) mas grande(s) es(son): ",max_in_list(list))
else:
	print("No se ha proporcionado una lista")
