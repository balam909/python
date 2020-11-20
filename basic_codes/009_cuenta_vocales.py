#! /usr/bin/env python
# -*- coding: utf-8 -*-

palabra=input("Ingrese la palabra de la cual quiere conocer el numero de vocales contenidas  -  ")
vocales={"a":0,"e":0,"i":0,"o":0,"u":0}
lowerLetras=palabra.lower()
for letra in lowerLetras[:]:
	for vocal in vocales:
		if letra==vocal:
			vocales[vocal]+=1

totalVocales=0
for vocal in vocales:
	print("La vocal",vocal,"esta contenida",vocales[vocal],"veces en la palabra:",palabra)
	totalVocales=totalVocales+vocales[vocal]
	
print("El total de vocales en la palabra",palabra,"es:",totalVocales)
