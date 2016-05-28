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

def get_lunchtime_minutes(idlt,db):
	if(db==None):
		return DEFAULT_LUNCHTIME
	cursor=db.cursor()
	select_lunchtime="select * from Lunchtime where id='%d'"%(idlt)
	cursor.execute(select_lunchtime)
	for lunch in cursor:
		return lunch[3]
	return DEFAULT_LUNCHTIME

def get_lunchtime(idlt,db):
	if(db==None):
		return None
	cursor=db.cursor()
	select_lunchtime="select * from Lunchtime where id='%d'"%(idlt)
	cursor.execute(select_lunchtime)
	for lunch in cursor:
		return lunchtime.Lunchtime(lunch)
	return None
