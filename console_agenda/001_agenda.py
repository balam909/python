#! /usr/bin/python
# -*- coding: utf-8 -*-

import time
import os
import dbops
from DBMetadata import Datos

print('Inicializando agenda')

def cleanScreen():
	"""Limpiar la pantalla"""
	if os.name=="posix":
		os.system("clear")
	elif os.name==("ce","nt","dos"):
		os.system("cls")

def takeUserInput(var=""):
	userInput=input(var)
	if userInput==None:
		print("La Informacion proporcionada para el campo",var,"no es valida, por favor, intente nuevamente")
		return takeUserInput(var)
	userInputAsStr=str(userInput)
	if len(userInputAsStr.strip())>0:
		return userInput
	else:
		print("La Informacion proporcionada para el campo",var,"no es valida, por favor, intente nuevamente")
		return takeUserInput(var)

def doPrintTask(task):
	print(task)
	print('----------------')
	print('')

def newContact():
	"""Agregar nuevo contacto a la agenda"""
	doPrintTask("Agregar contacto")
	nombre=takeUserInput("Nombre: ")
	apellido=takeUserInput("Apellido: ")
	telefono=takeUserInput("Telefono: ")
	correo=takeUserInput("Correo: ")
	dbops.doInsert(nombre,apellido,telefono,correo)
	print("Se anadio un nuevo contacto de manera satisfactoria")
	time.sleep(2)
	main()

def deleteContact():
	"""Eliminar un contacto de la agenda mediante el nombre"""
	doPrintTask("Eliminar contacto")
	nombre=takeUserInput("Nombre: ")
	dbops.doDelete(nombre)
	print("Se elimino el contacto de manera satisfactoria")
	time.sleep(2)
	main()

def selectAllContacts():
	"""Devuelve todos los contactos de la agenda"""
	doPrintTask("Lista de Contactos")
	resultList=dbops.doSelect(None)
	for contacto in resultList:
		print("%s %s %s %s"%(contacto.name,contacto.lastname,contacto.phone,contacto.email))
	print("")
	input("Presiona una tecla para continuar...")
	main()

def selectContact():
	"""Busca un contacto mediante el Nombre"""
	doPrintTask("Buscar contacto")
	nombre=takeUserInput("Nombre: ")
	resultList=dbops.doSelect(nombre)
	for contacto in resultList:
		print("Nombre: ",contacto.name,"Apellido: ",contacto.lastname,"Telefono: ",contacto.phone,"Correo: ",contacto.email)
	input("Presiona una tecla para continuar...")
	main()

def main():
	"""Funcion principal de la agenda"""
	cleanScreen()
	print('------------------------------------------------')
	print('Esta es una agenda sencilla')
	print('------------------------------------------------')
	print('')
	print("""
	[1] Nuevo Contacto
	[2] Ver todos los contactos
	[3] Buscar contacto
	[4] Eliminar contacto
	[0] Salir
	""")
	option=input("Opcion: ")
	if option=="1":
		cleanScreen()
		newContact()
	elif option=="2":
		cleanScreen()
		selectAllContacts()
	elif option=="3":
		cleanScreen()
		selectContact()
	elif option=="4":
		cleanScreen()
		deleteContact()
	elif option=="0":
		print("")
		print("Bye...")
		print("")
		time.sleep(3)
		exit()
	else:
		print("Opcion no valida, porfavor, intenta nuevamente")
		time.sleep(2)
		main()

dbops.createOrConnectDB()
main()
