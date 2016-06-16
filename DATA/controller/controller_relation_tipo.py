#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from constants import *
from models import relation_trabajador_tipo

def get_relations_tipos(db,int_id):
	cursor=db.cursor()
	list_relation=[]
	select_tipos="""select * from RelacionTrabajadorTipo where
					id_tipo='%d'"""%(int_id)
	cursor.execute(select_tipos)
	for row in cursor:
		list_relation.append(relation_trabajador_tipo.RelacionTrabajadorTipo(row))
	return list_relation

def relation_exist(db,int_id,str_pin):
	cursor=db.cursor()
	search_relation_tipo="""SELECT * FROM RelacionTrabajadorTipo WHERE id_tipo='%d' and pin='%s'"""%(int_id,str_pin)
	cursor.execute(search_relation_tipo)
	for i in cursor:
		return True
	return False