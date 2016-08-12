#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from constants import *

class Horario():
	id	 			= 0
	pin				= ""
	fechavalido		= ""
	entrada			= ""
	salida			= ""
	def  __init__(self, row_lunchtime):
		self.id			 	= row_lunchtime[0]
		self.pin	 		= row_lunchtime[1]
		self.fechavalido	= str(row_lunchtime[2])
		self.entrada 		= str(row_lunchtime[3])
		self.salida 		= str(row_lunchtime[4])

	def insert(self,cursor_db):
		insert="""INSERT INTO Horario
								(pin,fechavalido,entrada,salida)
								values('%s','%s','%s','%s'
								)"""%(self.pin,self.fechavalido,self.entrada,self.salida)
		cursor_db.execute(insert)
		cursor_db.execute("select MAX(id) from Horario")
		for row in cursor_db:
			self.id=row[0]
		return True

	def insert_new_horario(self,new_entrada,new_salida,cursor_db):
		if(new_entrada==self.entrada and new_salida==self.salida):
			return False
		self.entrada = new_entrada
		self.salida = new_salida
		insert="""INSERT INTO Horario
								(pin,fechavalido,entrada,salida)
								values('%s','%s','%s','%s'
								)"""%(self.pin,self.fechavalido,self.entrada,self.salida)
		cursor_db.execute(insert)
		cursor_db.execute("select MAX(id) from Horario")
		for row in cursor_db:
			self.id=row[0]
		return True
