#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Area():
	id					= 0
	name				= ""
	def  __init__(self, row_area):
		self.id	 			= row_area[0]
		self.name	 		= row_area[1]

	def insert(self,cursor_db):
		insert_area_sql="""INSERT INTO Area(name)values('%s')"""%(self.name)
		cursor_db.execute(insert_area_sql)
		cursor_db.execute("select MAX(id) from Area")
		for row in cursor_db:
			self.id=row[0]
		return True

	def remove(self,cursor_db):
		if(self.id==0):
			return False
		select_tipos_area="""SELECT id FROM Tipo WHERE id_area='%d'"""%(self.id)
		cursor_db.execute(select_tipos_area)
		for row in cursor_db:
			delete_all_relation_tipo_area="""DELETE FROM RelacionTrabajadorTipo WHERE id_tipo='%d'"""%(row[0])
			cursor_db.execute(delete_all_relation_tipo_area)
		delete_tipos_area="""DELETE FROM Tipo WHERE id_area='%d'"""%(self.id)
		cursor_db.execute(delete_tipos_area)
		delete_area_sql="""DELETE FROM Area WHERE id='%d'"""%(self.id)
		cursor_db.execute(delete_area_sql)
		return True