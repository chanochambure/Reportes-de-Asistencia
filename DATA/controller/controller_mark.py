#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
import datetime
from PyQt4 import QtCore,QtGui

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from models import *
from constants import *
from controller import controller_trabajador

def has_a_check(pin,str_datetime,db):
	cursor=db.cursor()
	select_marks="select * from Marcacion where pin='%s' and hour='%s'"%(pin,str_datetime)
	cursor.execute(select_marks)
	rows = cursor.fetchall()
	return len(rows)>0

def valid_date(str_datetime,tipo=True):
	actual=datetime.datetime.now()
	past=to_datetime(str_datetime,tipo)
	if(past):
		return past>actual
	return True

class class_insert_from_filepath(QtCore.QThread):
	finished 	= QtCore.pyqtSignal()
	data		= 0
	def __init__(self,path):
		self.file_path=path
		QtCore.QThread.__init__(self)

	def run(self):
		self.data=self.insert_from_filepath(self.file_path)
		self.finished.emit()
		self.fthread.terminate()

	def insert_from_filepath(self,filepath):
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
						datetime_data=to_datetime(str_datetime,False)
						str_datetime=str(datetime_data)
						if(has_a_check(str_pin,str_datetime,db)==False):
							new_mark = mark.Marcacion([0,str_pin,str_datetime])
							if(new_mark.insert(db.cursor())):
								cont+=1
				db.commit()
				db.close()
				return cont
			except IOError:
				return ERROR_FILE
		return -2