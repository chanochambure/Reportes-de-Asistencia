#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from models import *

def pin_exist(str_pin,db,active=False):
	cursor=db.cursor()
	select_worker="select * from Trabajador where pin='%s'"%(str_pin)
	if(active):
		select_worker+=" and activo=1"
	cursor.execute(select_worker)
	rows = cursor.fetchall()
	return len(rows)>0

def get_workers(str_name,str_fname,str_mname,db,active):
	cursor=db.cursor()
	list_workers=[]
	select_workers="""select * from Trabajador where
					name LIKE '%s' and 
					father_last_name LIKE '%s' and 
					mother_last_name LIKE '%s'"""%("%"+str_name+"%","%"+str_fname+"%","%"+str_mname+"%")
	if(active):
		select_workers+=" and activo=1"
	select_workers+=" ORDER BY father_last_name,mother_last_name,name"
	cursor.execute(select_workers)
	for row in cursor:
		list_workers.append(trabajador.Trabajador(row))
	return list_workers
