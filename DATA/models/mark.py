#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Marcacion():
	id 		= 0
	pin		= ""
	hora	= ""
	valido	= True
	def  __init__(self, row_marcacion):
		self.id	 	= row_marcacion[0]
		self.pin 	= row_marcacion[1]
		self.hora	= str(row_marcacion[2])
		self.valido	= row_marcacion[3]

	def insert(self,cursor_db):
		insert_mark="""INSERT INTO Marcacion
								(pin,hour,valido)
								values('%s','%s',b'%d'
								)"""%(self.pin,self.hora,self.valido)
		cursor_db.execute(insert_mark)
		return True