#! /usr/bin/python
# -*- coding: utf-8 -*-

class DBMetadata:
	def __init__(self, connection, executor):
		self.connection=connection
		self.executor=executor

class Datos:
	def __init__(self,name,lastname,phone,email):
		self.name=name
		self.lastname=lastname
		self.phone=phone
		self.email=email
