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
from controller import controller_trabajador,controller_lunchtime

def complete_day_reporte(list_reporte,pin,strdate,only_activas,db,total_marks):
	cursor=db.cursor()
	select_marks="select hour from marcacion where pin='%s' and DATE(hour)='%s'"%(pin,strdate)
	if(only_activas):
		select_marks+=" and valido=1"
	select_marks+=" order by hour"
	cursor.execute(select_marks)
	result=cursor.fetchall()
	worker=controller_trabajador.get_worker(pin,db)
	lunchtime_v=controller_lunchtime.get_lunchtime_minutes_by_date_pin(strdate,worker.pin,db)
	if(len(result)==total_marks):
		if(total_marks==TOTAL_MARKS_LIMIT_FOR_DAY):
			datetime_e=to_datetime(datetime_to_str(str(result[0][0].day),str(result[0][0].month),str(result[0][0].year),
									str(time_get_hour(worker.hora_entrada)),str(time_get_min(worker.hora_entrada))),True)
			datetime_s=to_datetime(datetime_to_str(str(result[3][0].day),str(result[3][0].month),str(result[3][0].year),
									str(time_get_hour(worker.hora_salida)),str(time_get_min(worker.hora_salida))),True)
			ent_r=result[0][0]-datetime_e
			if(ent_r.days>=0):
				time_minutes = ent_r.seconds/60
				if(time_minutes>TOTAL_TIME_TARDANZA_LIMIT):
					list_reporte[2]=time_minutes
			else:
				list_reporte[2]=(-1)*((86400-ent_r.seconds)/60)
			sal_r=datetime_s-result[3][0]
			if(sal_r.days>=0):
				list_reporte[3]=(sal_r.seconds/60)
			else:
				list_reporte[3]=(-1)*((86400-sal_r.seconds)/60)
			list_reporte[4]=((result[2][0]-result[1][0]).seconds/60)-lunchtime_v
			if(list_reporte[4]<=TOTAL_TIME_TARDANZA_LIMIT and list_reporte[4]>=0):
				list_reporte[4]=0
		elif(total_marks==TOTAL_MARKS_SATURDAY):
			datetime_e=to_datetime(datetime_to_str(str(result[0][0].day),str(result[0][0].month),str(result[0][0].year),
									str(time_get_hour(worker.hora_entrada)),str(time_get_min(worker.hora_entrada))),True)
			ent_r=result[0][0]-datetime_e
			if(ent_r.days>=0):
				time_minutes = ent_r.seconds/60
				if(time_minutes>TOTAL_TIME_TARDANZA_LIMIT):
					list_reporte[2]=time_minutes
			else:
				list_reporte[2]=(-1)*((86400-ent_r.seconds)/60)
			list_reporte[3]=0
			list_reporte[4]=0
		list_reporte[5]=list_reporte[4]+list_reporte[2]+list_reporte[3]
		if(total_marks==TOTAL_MARKS_SATURDAY):
			list_reporte[3]=0
			list_reporte[4]=0

def get_reporte_tardanza(pin,str_date1,str_date2,db,only_activas=True):
	lista_reporte=[]
	cursor=db.cursor()
	select_quantity="""select DATE(hour),count(id) from marcacion
					where pin='%s' and DATE(Marcacion.hour)>='%s' and DATE(Marcacion.hour)<='%s'"""%(pin,str_date1,str_date2)
	if(only_activas):
		select_quantity+=" and valido=1"
	select_quantity+=" group by DATE(hour) order by DATE(hour)"
	cursor.execute(select_quantity)
	for row in cursor:
		day_reporte=[str(row[0]),row[1],0,0,0,0,True]
		total_marks=TOTAL_MARKS_LIMIT_FOR_DAY
		if(row[0].weekday()==5):
			total_marks=TOTAL_MARKS_SATURDAY
		if(row[1]==total_marks):
			complete_day_reporte(day_reporte,pin,day_reporte[0],only_activas,db,total_marks)
		else:
			day_reporte[1]=str(day_reporte[1])+" - Error"
			day_reporte[6]=False
			day_reporte[2]=None
			day_reporte[3]=None
			day_reporte[4]=None
		lista_reporte.append(day_reporte)
	return lista_reporte

def get_total_minutes(matrix):
	list_minuts=[0,0,0]
	if(len(matrix)):
		for row in matrix:
			if(row[6]):
				list_minuts[int(row[2]<0)]+=abs(row[2])
				list_minuts[int(row[3]<0)]+=abs(row[3])
				list_minuts[int(row[4]<0)]+=abs(row[4])
			list_minuts[2]+=row[5]
		return "Tarde: "+mins_to_str_time_ot(list_minuts[0])+" Temprano: "+mins_to_str_time_ot(list_minuts[1])+" Total: "+mins_to_str_time_ot(list_minuts[2])
	return None