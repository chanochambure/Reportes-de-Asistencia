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

#TEXT
MAIN_TITLE					= "Reporte de Asistencias"
MAIN_VIEW_TITLE_ADMIN		= "Administrador:\nReportes de Asistencias"
BUTTON_INSERT_WORKER		= "Insertar Trabajador"
BUTTON_MARKS				= "Insertar Marcacion"
BUTTON_MARKS_FROM_FILE		= "Insertar Marcaciones desde un archivo"
BUTTON_MODIFY_WORKER		= "Modificar Trabajador"
BUTTON_EXIT					= "Salir"
ERROR_A_PROCESS_OPENED		= "Tiene ya una ventana abierta"
ADMIN_INSERT_WORKER_TITLE	= "Insertar Trabajador"
BUTTON_CREATE_WORKER		= "Insertar"
BUTTON_BACK					= "Atras"
#NUMBERS
GRID_X_MAIN_WINDOW_ADMIN				= 3
GRID_Y_MAIN_WINDOW_ADMIN				= 7
GRID_X_POSITION_TITLE					= 0
GRID_X_POSITION_INSERT_WORKER			= 2
GRID_X_POSITION_MODIFY_WORKER			= 3
GRID_X_POSITION_INSERT_MARKS			= 4
GRID_X_POSITION_INSERT_MARKS_FROM_FILE	= 5
GRID_X_POSITION_EXIT					= 6
GRID_Y_POSITION_BUTTON					= 1
BUTTON_SIZE_MAIN_VIEW					= 250
FONT_TITLE_SIZE							= 18
ADMIN_INSERT_WORKER_X					= 8
ADMIN_INSERT_WORKER_Y					= 2
BUTTON_SIZE_INSERT_WORKER_VIEW			= 300
GRID_X_POSITION_CREATE_INSERT_WORK		= 7
GRID_Y_POSITION_CREATE_INSERT_WORK		= 1
GRID_X_POSITION_BACK_INSERT_WORK		= 7
GRID_Y_POSITION_BACK_INSERT_WORK		= 0
GRID_X_POSITION_INSERT_WORK_TITLE		= 0
GRID_Y_POSITION_INSERT_WORK_TITLE		= 0