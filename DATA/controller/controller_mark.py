#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
import datetime
from PyQt4 import QtCore,QtGui

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from models import mark,trabajador,lunchtime
from constants import *
from controller import controller_trabajador

def has_a_check(pin,str_datetime,db,valid=True,id=-1):
	cursor=db.cursor()
	select_marks="select * from Marcacion where pin='%s' and hour='%s'"%(pin,str_datetime)
	if(valid):
		select_marks+=" and valido=1"
	cursor.execute(select_marks)
	rows = cursor.fetchall()
	if(id!=-1 and len(rows)>0):
		return rows[0][0]!=id
	return len(rows)>0

def valid_date(str_datetime,tipo=True):
	actual=datetime.datetime.now()
	past=to_datetime(str_datetime,tipo)
	if(past):
		return past>actual
	past=to_datetime_other(str_datetime)
	if(past):
		return past>actual
	return True

def get_marks(pin,str_datetime1,str_datetime2,db,validos=False):
	cursor=db.cursor()
	list_marks=[]
	select_marks="""SELECT * FROM Marcacion WHERE pin='%s' and 
					DATE(Marcacion.hour)>='%s' and DATE(Marcacion.hour)<='%s'"""%(pin,str_datetime1,str_datetime2)
	if(validos):
		select_marks+=" and valido=1"
	select_marks+=" ORDER BY hour"
	cursor.execute(select_marks)
	for row in cursor:
		list_marks.append(mark.Marcacion(row))
	return list_marks

def insert_from_filepath(filepath):
	if(filepath.length()==0):
		return ERROR_FILE
	db=get_connection()
	if(db):
		try:
			file = open(unicode(filepath),'r')
			cont=0
			file.readline()
			for line in file:
				listline=line.split(',')
				if(len(listline)!=COLUMNS_IN_FILE):
					return ERROR_FILE
				str_pin=listline[2]
				str_pin=str_pin[0:len(str_pin)-1]
				str_datetime=listline[1]
				if(controller_trabajador.pin_exist(str_pin,db,True) and valid_date(str_datetime,False)==False):
					datetime_data=to_datetime_other(str_datetime)
					if(datetime_data==None):
						datetime_data=to_datetime(str_datetime,False)
					if(datetime_data):
						str_datetime=str(datetime_data)
						if(has_a_check(str_pin,str_datetime,db)==False):
							new_mark = mark.Marcacion([0,str_pin,str_datetime,True])
							if(new_mark.insert(db.cursor())):
								cont+=1
			db.commit()
			db.close()
			return cont
		except IOError:
			return ERROR_FILE
	return -2