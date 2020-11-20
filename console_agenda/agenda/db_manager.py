#! /usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from DBMetadata import DBMetadata
from DBMetadata import Datos

def connectDb(db_name='agenda.db'):
	print('Conectando a la base de datos...')
	connection=sqlite3.connect(db_name)
	print('Conexion a base de datos: Exitosa')
	return connection

def getDbMetadata(connection=connectDb()):
	print('Openning DB...')
	executor=connection.cursor()
	print('DB Oppened successful')
	return DBMetadata(connection, executor)

def executeDBCommand(command):
	dbMetadata=getDbMetadata()
	dbMetadata.executor.execute(command)
	return dbMetadata

def executeDDL(command):
	dbMetadata=executeDBCommand(command)
	dbMetadata.executor.close()

def executeDML(command):
	dbMetadata=executeDBCommand(command)
	dbMetadata.connection.commit()
	dbMetadata.executor.close()

def executeSearch(command):
	dbMetadata=executeDBCommand(command)
	queryresult=dbMetadata.executor.fetchall()
	listResult=list()
	for item in queryresult:
		listResult.append(Datos(item[0],item[1],item[2],item[3]))
	return listResult

