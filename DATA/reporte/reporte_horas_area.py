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
from reporte import reporte_horas

def get_reporte_hora_interface(db,worker,str_date1,str_date2):
	reporte_matrix=reporte_horas.get_reporte_horas(worker.pin,str_date1,str_date2,db)
	minutos=reporte_horas.get_total_minutes(reporte_matrix)
	time_to_work=8*60
	return_value=[{},""]
	if(minutos>-1):
		time_lunch=controller_lunchtime.get_lunchtime_minutes(worker.idlt,db)
		time_to_work=controller_trabajador.get_time_work(worker.hora_entrada,worker.hora_salida,time_lunch)
		return_value[1]=(mins_to_str_time(minutos,time_to_work))
	else:
		return_value[1]=REPORTE_TOTAL_HORAS_EMPTY
	for index_report in range(len(reporte_matrix)):
		return_value[0][reporte_matrix[index_report][0]]=mins_to_str_time(reporte_matrix[index_report][1],time_to_work)
	return return_value

def get_all_pins(db,id_area,id_tipo):
	list_pins=[]
	sql_sentence="select pin from RelacionTrabajadorTipo"
	if(id_area>0):
		if(id_tipo>0):
			sql_sentence+=" where id_tipo='%d'"%(id_tipo)
		else:
			area_tipos=controller_tipo.get_r_tipos(db,id_area)
			sql_sentence+=" where id_tipo in ("
			cont=0
			len_list=len(area_tipos)-1
			for tipo in area_tipos:
				sql_sentence+="'%d'"%(tipo.id)
				if(cont<len_list):
					sql_sentence+=", "
				cont+=1
			sql_sentence+=")"
	cursor=db.cursor()
	sql_sentence+=" group by pin"
	cursor.execute(sql_sentence)
	for row in cursor:
		list_pins.append(row[0])
	return list_pins

def get_reporte_horas_area(db,id_area,id_tipo,str_date1,str_date2):
	matriz=[]
	list_relations=get_all_pins(db,id_area,id_tipo)
	for pin in list_relations:
		worker=controller_trabajador.get_worker(pin,db,False)
		worker_fullname=worker.name+" "+worker.father_last_name+" "+worker.mother_last_name
		reporte_hora=get_reporte_hora_interface(db,worker,str_date1,str_date2)
		matriz.append([worker_fullname,reporte_hora[1],reporte_hora[0]])
	return matriz
