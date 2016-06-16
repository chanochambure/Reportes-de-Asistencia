#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from models import trabajador,mark,lunchtime,area,tipo
from constants import *

def get_r_tipos(db,int_id):
	cursor=db.cursor()
	list_tipos=[]
	select_tipos="select * from Tipo"
	if(int_id>0):
		select_tipos+=""" where id_area='%d'"""%(int_id)
	select_tipos+=" ORDER BY name"
	cursor.execute(select_tipos)
	for row in cursor:
		list_tipos.append(tipo.Tipo(row))
	return list_tipos

def get_tipos(db,int_id):
	cursor=db.cursor()
	list_tipos=[]
	select_tipos="""select * from Tipo where
					id_area='%d'"""%(int_id)
	select_tipos+=" ORDER BY name"
	cursor.execute(select_tipos)
	for row in cursor:
		list_tipos.append(tipo.Tipo(row))
	return list_tipos