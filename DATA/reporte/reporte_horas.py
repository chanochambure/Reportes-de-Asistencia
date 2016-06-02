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

def get_str_minutes_from_day(pin,strdate,only_activas,db,total_marks):
	cursor=db.cursor()
	select_marks="select hour from marcacion where pin='%s' and DATE(hour)='%s'"%(pin,strdate)
	if(only_activas):
		select_marks+=" and valido=1"
	select_marks+=" order by hour"
	cursor.execute(select_marks)
	result=cursor.fetchall()
	if(len(result)==total_marks):
		if(total_marks==TOTAL_MARKS_LIMIT_FOR_DAY):
			p1=result[1][0]-result[0][0]
			p2=result[3][0]-result[2][0]
			return int((p1.seconds+p2.seconds)/60)
		elif(total_marks==TOTAL_MARKS_SATURDAY):
			p1=result[1][0]-result[0][0]
			return int((p1.seconds)/60)
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
		total_marks=TOTAL_MARKS_LIMIT_FOR_DAY
		if(row[0].weekday()==5):
			total_marks=TOTAL_MARKS_SATURDAY
		if(row[1]==total_marks):
			day_reporte[1]=get_str_minutes_from_day(pin,day_reporte[0],only_activas,db,total_marks)
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
