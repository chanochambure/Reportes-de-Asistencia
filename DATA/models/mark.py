#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Marcacion():
	id 		= 0
	pin		= ""
	hora	= ""
	tipo	= ""
	valido	= True
	def  __init__(self, row_marcacion):
		self.id	 	= row_marcacion[0]
		self.pin 	= row_marcacion[1]
		self.hora	= str(row_marcacion[2])
		self.tipo	= row_marcacion[3]
		self.valido	= row_marcacion[4]

	def insert(self,cursor_db):
		insert_mark="""INSERT INTO Marcacion
								(pin,hour,tipo,valido)
								values('%s','%s',b'%d',b'%d'
								)"""%(self.pin,self.hora,self.tipo,self.valido)
		cursor_db.execute(insert_mark)
		return True

	def update(self,cursor_db):
		update_code_worker="""UPDATE Marcacion SET hour='%s', valido=b'%d', tipo=b'%d'
							WHERE id='%d'"""%(
									self.hora,
									self.valido,
									self.tipo,
									self.id)
		cursor_db.execute(update_code_worker)
		return True
