#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
import datetime

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from models import mark,trabajador,lunchtime
from constants import *
from controller import *

def get_str_minutes_from_day(pin,strdate,only_activas,db):
	marcaciones=controller_mark.get_marks_day(pin,strdate,db,only_activas,False)
	if(len(marcaciones)>0 and len(marcaciones)%2==0):
		total=0
		cont=0
		while(cont<len(marcaciones)):
			if(marcaciones[cont+1][3] and marcaciones[cont][3]==False):
				total+=(marcaciones[cont+1][2]-marcaciones[cont][2]).seconds
			else:
				return None
			cont+=2
		return int(total/60)
	if(len(marcaciones)==0):
		return -4
	return None

def get_reporte_horas(pin,str_date1,str_date2,db,only_activas=True):
	lista_reporte=[]
	cursor=db.cursor()
	select_quantity="""select DATE(hour),count(id) from marcacion
					where pin='%s' and DATE(Marcacion.hour)>='%s' and DATE(Marcacion.hour)<='%s'"""%(pin,str_date1,str_date2)
	if(only_activas):
		select_quantity+=" and valido=1"
	select_quantity+=" group by DATE(hour) order by DATE(hour)"
	cursor.execute(select_quantity)
	for row in cursor:
		day_reporte=[str(row[0]),None]
		day_reporte[1]=get_str_minutes_from_day(pin,day_reporte[0],only_activas,db)
		if(day_reporte[1]!=-4):
			lista_reporte.append(day_reporte)
	return lista_reporte

def get_total_minutes(matrix):
	if(len(matrix)):
		acum=0
		for row in matrix:
			if(row[1]!=None):
				acum+=row[1]
		return acum
	return -1
