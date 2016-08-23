#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
import datetime
from PyQt4 import QtCore,QtGui

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from models import trabajador,mark,lunchtime,horario
from constants import *

def get_horario_date(idh,db):
	if(db==None):
		return datetime.datetime.now().date()
	cursor=db.cursor()
	select="select * from Horario where id='%d'"%(idh)
	cursor.execute(select)
	for hor in cursor:
		return to_date(str(hor[2]),True)
	return datetime.datetime.now().date()

def get_horario(idh,db):
	if(db==None):
		return None
	cursor=db.cursor()
	select="select * from Horario where id='%d'"%(idh)
	cursor.execute(select)
	for hor in cursor:
		return horario.Horario(hor)
	return None

def get_horarios(pin,db):
	if(db==None):
		return []
	cursor=db.cursor()
	select="select * from Horario where pin='%s' ORDER BY fechavalido DESC"%(pin)
	cursor.execute(select)
	horario_list = []
	for hor in cursor:
		horario_list.append(horario.Horario(hor))
	return horario_list

def get_horario_by_date_pin(str_date,pin,db):
	cursor=db.cursor()
	select="select * from Horario WHERE pin='%s' and fechavalido<='%s' ORDER BY fechavalido DESC"%(pin,str_date)
	cursor.execute(select)
	for hor in cursor:
		return horario.Horario(hor)
	return None