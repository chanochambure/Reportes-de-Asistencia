#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Trabajador():
	pin 				= ""
	name				= ""
	father_last_name	= ""
	mother_last_name	= ""
	activo				= 1
	def  __init__(self, row_trabajador):
		self.pin	 			= row_trabajador[0]
		self.name		 		= row_trabajador[1]
		self.father_last_name 	= row_trabajador[2]
		self.mother_last_name 	= row_trabajador[3]
		self.activo 			= row_trabajador[4]

	def insert(self,cursor_db):
		insert_worker_sql="""INSERT INTO Trabajador
								(pin,name,father_last_name,mother_last_name,activo)
								values('%s','%s','%s','%s',b'%d'
								)"""%(self.pin,
										self.name,
										self.father_last_name,
										self.mother_last_name,
										self.activo)
		cursor_db.execute(insert_worker_sql)
		return True

	def update(self,cursor_db):
		update_code_worker="""UPDATE Trabajador SET name='%s', father_last_name='%s', mother_last_name='%s', activo=b'%d'
							WHERE pin='%s'"""%(
									self.name,
									self.father_last_name,
									self.mother_last_name,
									self.activo,
									self.pin)
		cursor_db.execute(update_code_worker)
		return True