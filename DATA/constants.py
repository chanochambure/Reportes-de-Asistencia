#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import time
import datetime
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import BDconf

def get_connection():
	try:
		return MySQLdb.connect(BDconf.DATABASE_HOST,BDconf.DATABASE_USER,BDconf.DATABASE_PASSWORD,BDconf.DATABASE_NAME)
	except MySQLdb.Error as err:
		QMessageBox.warning(None, 'Error',"Error al Conectar con la Base De Datos", QMessageBox.Ok)
		exit()

#TIME
def get_time_str():
	return time.strftime('%Y-%m-%d %H:%M:%S')

#UNICODE
def str_is_invalid(str_u):
	for char_u in unicode(str_u):
		if(ord(char_u)>=128 or char_u=="'"):
			return True
	return False
