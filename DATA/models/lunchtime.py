#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from constants import *

class Lunchtime():
	id	 			= 0
	pin				= ""
	fechavalido	= ""
	minutos			= 1
	def  __init__(self, row_lunchtime):
		self.id			 	= row_lunchtime[0]
		self.pin	 		= row_lunchtime[1]
		self.fechavalido	= str(row_lunchtime[2])
		self.minutos 		= row_lunchtime[3]

	def insert(self,cursor_db):
		insert_lunchtime="""INSERT INTO Lunchtime
								(pin,fechavalido,minutos)
								values('%s','%s','%d'
								)"""%(self.pin,self.fechavalido,self.minutos)
		cursor_db.execute(insert_lunchtime)
		cursor_db.execute("select MAX(id) from Lunchtime")
		for row in cursor_db:
			self.id=row[0]
		return True

	def insert_new_lunchtime(self,new_lunchtime,cursor_db):
		if(new_lunchtime==self.minutos):
			return False
		self.minutos = new_lunchtime
		self.fechavalido = get_actual_date()
		insert_lunchtime="""INSERT INTO Lunchtime
								(pin,fechavalido,minutos)
								values('%s','%s','%d'
								)"""%(self.pin,self.fechavalido,self.minutos)
		cursor_db.execute(insert_lunchtime)
		cursor_db.execute("select MAX(id) from Lunchtime")
		for row in cursor_db:
			self.id=row[0]
		return True
