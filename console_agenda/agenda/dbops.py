#! /usr/bin/python
# -*- coding: utf-8 -*-

from db_manager import executeDDL
from db_manager import executeDML
from db_manager import executeSearch

print('Inicializando agenda')

def createOrConnectDB():
        executeDDL('''CREATE TABLE IF NOT EXISTS datos (nombre TEXT, apellido TEXT, telefono TEXT, correo TEXT)''')

def doInsert(nombre, apellido, telefono, correo):
        executeDML("insert into datos (nombre, apellido, telefono, correo) values ('%s','%s','%s','%s')"%(nombre,apellido, telefono, correo))

def doDelete(nombre):
        executeDML("delete from datos where nombre='%s'"%(nombre))

def doSelect(nombre=None):
        if nombre is None:
                return executeSearch("select * from datos")
        else:
                return executeSearch("select * from datos where nombre='%s'"%(nombre))
