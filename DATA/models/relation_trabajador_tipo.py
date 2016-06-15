#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RelacionTrabajadorTipo():
	id_tipo			= 0
	pin				= ""
	def  __init__(self, row_relation):
		self.id_tipo	= row_relation[0]
		self.pin		= row_relation[1]

	def insert(self,cursor_db):
		insert_tipo_sql="""INSERT INTO RelacionTrabajadorTipo values('%d','%s')"""%(self.id_tipo,self.pin)
		cursor_db.execute(insert_tipo_sql)
		return True

	def remove(self,cursor_db):
		delete_relation_tipo="""DELETE FROM RelacionTrabajadorTipo WHERE id_tipo='%d' and pin='%s'"""%(self.id_tipo,self.pin)
		cursor_db.execute(delete_relation_tipo)
		return True
