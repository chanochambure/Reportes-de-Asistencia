#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tipo():
	id				= 0
	id_area			= 0
	name			= ""
	def  __init__(self, row_tipo):
		self.id 		= row_tipo[0]
		self.id_area	= row_tipo[1]
		self.name 		= row_tipo[2]

	def insert(self,cursor_db):
		insert_tipo_sql="""INSERT INTO Tipo(id_area,name)values('%d','%s')"""%(self.id_area,self.name)
		cursor_db.execute(insert_tipo_sql)
		cursor_db.execute("select MAX(id) from Tipo")
		for row in cursor_db:
			self.id=row[0]
		return True

	def remove(self,cursor_db):
		if(self.id==0):
			return False
		delete_all_relation_tipo="""DELETE FROM RelacionTrabajadorTipo WHERE id_tipo='%d'"""%(self.id)
		cursor_db.execute(delete_all_relation_tipo)
		delete_tipo="""DELETE FROM Tipo WHERE id='%d'"""%(self.id)
		cursor_db.execute(delete_tipo)
		return True
