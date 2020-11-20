#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

def is_binary_string(binaryString):
	regexResult=re.search("[0-1]+",binaryString)
	if regexResult is None:
		print("El valor proporcionado no es un numero binario valido")
		return False
	elif str(regexResult.group())!=binaryString:
		print("Un numero binarion solo puede contener '0' y '1'")
		return False
	else:
		return True

def convertToDecimal(binaryString):
	if is_binary_string(binaryString):
		exp=len(binaryString)-1
		decimal=0
		for item in binaryString[:]:
			decimal=decimal+int(item)*2**exp
			exp-=1
		return decimal
	else:
		return "No valido"

binaryString=input("Proporcione un numero binarion valido  -  ")
result=convertToDecimal(binaryString)
if result!="No valido":
	print("El numero binario expresado en numero decimal es: ",result)
