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
		return None

#TIME
def get_time_str():
	return time.strftime('%Y-%m-%d %H:%M:%S')

#UNICODE
def str_is_invalid(str_u):
#	for char_u in unicode(str_u):
#		if(ord(char_u)>=128 or char_u=="'"):
#			return True
	return False

#IS A NUMBER
def is_number(str_n):
	for char_n in str(str_n):
		if(ord(char_n)<48 or ord(char_n)>57):
			return False
	return True

#TEXT
MAIN_TITLE							= "Reporte de Asistencias"
MAIN_VIEW_TITLE_ADMIN				= "Administrador:\nReportes de Asistencias"
BUTTON_INSERT_WORKER				= "Insertar Trabajador"
BUTTON_MARKS						= "Insertar Marcacion"
BUTTON_MARKS_FROM_FILE				= "Insertar Marcaciones desde un archivo"
BUTTON_MODIFY_WORKER				= "Modificar Trabajador"
BUTTON_EXIT							= "Salir"
ERROR_A_PROCESS_OPENED				= "Tiene ya una ventana abierta"
ADMIN_INSERT_WORKER_TITLE			= "Insertar Trabajador"
ADMIN_INSERT_WORKER_PIN				= "Numero de Identificacion"
ADMIN_INSERT_WORKER_NAME			= "Nombre"
ADMIN_INSERT_WORKER_FNAME			= "Apellido Paterno"
ADMIN_INSERT_WORKER_MNAME			= "Apellido Materno"
BUTTON_CREATE_WORKER				= "Insertar"
BUTTON_BACK							= "Atras"
CREATE_WORKER_EMPTY_CAMP			= "Existe algun Campo Vacio"
CREATE_WORKER_INVALID_CAMP			= "Existe caracteres no validos"
CREATE_WORKER_INVALID_PIN			= "El PIN solo puede tener caracteres numericos"
CREATE_WORKER_QUESTION				= "Esta seguro de crear a este nuevo Trabajador"
CREATE_WORKER_BD_ERROR				= "Error con la Base de Datos"
CREATE_WORKER_ALREADY_HAS_BEEN_USED	= "El PIN ya esta siendo usando por otra persona"
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
ADMIN_INSERT_WORKER_X					= 7
ADMIN_INSERT_WORKER_Y					= 2
BUTTON_SIZE_INSERT_WORKER_VIEW_X		= 300
BUTTON_SIZE_INSERT_WORKER_VIEW_Y		= 50
GRID_X_POSITION_CREATE_INSERT_WORK		= 6
GRID_Y_POSITION_CREATE_INSERT_WORK		= 1
GRID_X_POSITION_BACK_INSERT_WORK		= 6
GRID_Y_POSITION_BACK_INSERT_WORK		= 0
GRID_X_POSITION_PIN						= 2
GRID_X_POSITION_NAME					= 3
GRID_X_POSITION_FNAME					= 4
GRID_X_POSITION_MNAME					= 5
GRID_Y_POSITION_LABEL					= 0
GRID_Y_POSITION_TEXT					= 1
GRID_X_POSITION_INSERT_WORK_TITLE		= 0
GRID_Y_POSITION_INSERT_WORK_TITLE		= 0