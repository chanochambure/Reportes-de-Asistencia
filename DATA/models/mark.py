#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Marcacion():
	id 		= 0
	pin		= ""
	hora	= ""
	def  __init__(self, row_marcacion):
		self.id	 	= row_marcacion[0]
		self.pin 	= row_marcacion[1]
		self.hora	= str(row_marcacion[2])
	def insert(self,cursor_db):
		insert_mark="""INSERT INTO Marcacion
								(pin,hour)
								values('%s','%s'
								)"""%(self.pin,
										self.hora)
		cursor_db.execute(insert_mark)
		return True