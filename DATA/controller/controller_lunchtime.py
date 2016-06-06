#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
import datetime
from PyQt4 import QtCore,QtGui

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from models import trabajador,mark,lunchtime
from constants import *

def get_lunchtime_minutes(idlt,db):
	if(db==None):
		return DEFAULT_LUNCHTIME
	cursor=db.cursor()
	select_lunchtime="select * from Lunchtime where id='%d'"%(idlt)
	cursor.execute(select_lunchtime)
	for lunch in cursor:
		return lunch[3]
	return DEFAULT_LUNCHTIME

def get_lunchtime_minutes_by_date_pin(str_date,pin,db):
	if(db==None):
		return DEFAULT_LUNCHTIME
	cursor=db.cursor()
	select_lunchtime="SELECT * FROM `lunchtime` WHERE pin='%s' and fechavalido<='%s' ORDER BY fechavalido DESC"%(pin,str_date)
	cursor.execute(select_lunchtime)
	for lunch in cursor:
		return lunch[3]
	return DEFAULT_LUNCHTIME

def get_lunchtime_date(idlt,db):
	if(db==None):
		return datetime.datetime.now().date()
	cursor=db.cursor()
	select_lunchtime="select * from Lunchtime where id='%d'"%(idlt)
	cursor.execute(select_lunchtime)
	for lunch in cursor:
		return to_date(str(lunch[2]),True)
	return datetime.datetime.now().date()

def get_lunchtime(idlt,db):
	if(db==None):
		return None
	cursor=db.cursor()
	select_lunchtime="select * from Lunchtime where id='%d'"%(idlt)
	cursor.execute(select_lunchtime)
	for lunch in cursor:
		return lunchtime.Lunchtime(lunch)
	return None

def get_lunchtimes(pin,db):
	if(db==None):
		return []
	cursor=db.cursor()
	select_lunchtime="select * from Lunchtime where pin='%s' ORDER BY fechavalido DESC"%(pin)
	cursor.execute(select_lunchtime)
	lunchtime_list = []
	for lunch in cursor:
		lunchtime_list.append(lunchtime.Lunchtime(lunch))
	return lunchtime_list
