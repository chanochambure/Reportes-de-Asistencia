#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import sys
import datetime
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import BDconf

def get_connection(showError=True):
	try:
		return MySQLdb.connect(BDconf.DATABASE_HOST,BDconf.DATABASE_USER,BDconf.DATABASE_PASSWORD,BDconf.DATABASE_NAME)
	except MySQLdb.Error as err:
		if(showError):
			QMessageBox.warning(None, 'Error',"Error al Conectar con la Base De Datos", QMessageBox.Ok)
		return None

#TIME
def datetime_to_str(day,month,year,hour,minute):
	return year+"-"+month+"-"+day+" "+hour+":"+minute+":00"

def get_actual_date():
	return time.strftime("%Y-%m-%d")

def time_to_str(hour,minute):
	return hour+":"+minute+":00"

def to_datetime(str_datetime,tipo):
	try:
		if(tipo):
			return_value=datetime.datetime.strptime(str_datetime,"%Y-%m-%d %H:%M:%S")
			return return_value
		else:
			return_value=datetime.datetime.strptime(str_datetime,"%d/%m/%Y %H:%M")
			return return_value
	except ValueError:
		return None

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
ADMIN_INSERT_INTRO_HOUR				= "Hora de Entrada"
ADMIN_INSERT_EXIT_HOUR				= "Hora de Salida"
ADMIN_INSERT_LUNCHTIME_MINUTES		= "Tiempo de Refrigerio"
BUTTON_CREATE_WORKER				= "Insertar"
BUTTON_BACK							= "Atras"
CREATE_WORKER_EMPTY_CAMP			= "Existe algun Campo Vacio"
CREATE_WORKER_INVALID_CAMP			= "Existe caracteres no validos"
CREATE_WORKER_INVALID_PIN			= "El PIN solo puede tener caracteres numericos"
CREATE_WORKER_INVALID_LT_MINUTES	= "El tiempo de refrigerio solo puede tener caracteres numericos"
CREATE_WORKER_QUESTION				= "Esta seguro de crear a este nuevo Trabajador"
CREATE_WORKER_SUCCESS				= "Trabajador Creado"
CREATE_WORKER_BD_ERROR				= "Error con la Base de Datos"
CREATE_WORKER_ALREADY_HAS_BEEN_USED	= "El PIN ya esta siendo usando por otra persona"
SEARCH_WORKER_MODIFY_MESSAGE		= "Modificar"
SEARCH_WORKER_MARKS_MESSAGE			= "Insertar Marcacion"
SEARCH_WORKER_TITLE					= "Buscar Trabajador"
SEARCH_WORKER_VIEW_TITLE			= "Buscar Trabajador"
BUTTON_SEARCH_WORKER				= "Buscar"
SEARCH_TITLE_ROWS					= "Nombres;Apellido Paterno;Apellido Materno;Accion"
SPLIT_TABLE_WORKERS					= ";"
ADMIN_MODIFY_WORKER_TITLE			= "Modificar Trabajador"
ADMIN_MOD_WORKER_ACTIVE				= "Activo"
BUTTON_MOD_WORKER					= "Modificar"
MOD_WORKER_NO_CHANGES				= "No ha hecho ningun cambio"
MOD_WORKER_QUESTION					= "Esta seguro de modificar con nuevos datos al Trabajador"
MOD_WORKER_SUCCESS					= "Trabajador Modificado"
ADMIN_INSERT_MARKS_TITLE			= "Insertar Marcacion"
BUTTON_INSERT_MARKS					= "Insertar"
ADMIN_INSERT_MARK_DATE				= "Fecha DD/MM/YY"
ADMIN_INSERT_MARK_TIME				= "Hora HH/MM"
ADMIN_NAME_INSERT_MARK				= "Trabajador"
CREATE_MARK_QUESTION				= "Esta seguro de crear una nueva Marcacion"
CREATE_MARK_SUCCESS					= "Marcacion Insertada"
WORKER_HAVE_ALREADY_THIS_MARK		= "El Trabajador ya tiene una Marcacion muy cercana de dicho dia a dicha hora"
MARK_NO_EXIST_YET					= "No se puede guardar una Marcacion de un dia con una hora que aun no ha pasado"
TITLE_FILE_DIALOG					= "Abrir Archivo"
DATA_TYPE_FILE_DIALOG				= "CSV data files (*.csv)"
DATA_INSERTED_FROM_FILE				= "Marcaciones Insertados desde el Archivo: "
ERROR_WITH_THE_FILE					= "Hubo un error al leer el archivo, puede estar corrompido"
FIRST_DATE								= "01/01/01"

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
ADMIN_INSERT_WORKER_Y					= 5
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
GRID_X_POSITION_IHOUR					= 2
GRID_X_POSITION_EHOUR					= 3
GRID_X_POSITION_LUNCH					= 5
GRID_Y_POSITION_LABEL					= 0
GRID_Y_POSITION_TEXT					= 1
GRID_Y_POSITION_LABEL_HOUR				= 2
GRID_Y_POSITION_HOUR_INSERT				= 3
GRID_Y_POSITION_MIN_INSERT				= 4
GRID_X_POSITION_INSERT_WORK_TITLE		= 0
GRID_Y_POSITION_INSERT_WORK_TITLE		= 0

SEARCH_WORKER_X_GRID					= 12
SEARCH_WORKER_Y_GRID					= 2
GRID_X_POSITION_SEARCH_WORK_TITLE		= 0
GRID_Y_POSITION_SEARCH_WORK_TITLE		= 0
GRID_X_POSITION_NAME_SEARCH				= 2
GRID_X_POSITION_FNAME_SEARCH			= 3
GRID_X_POSITION_MNAME_SEARCH			= 4
GRID_Y_POSITION_LABEL_SEARCH			= 0
GRID_Y_POSITION_TEXT_SEARCH				= 1
GRID_X_POSITION_CREATE_SEARCH_WORK		= 5
GRID_Y_POSITION_CREATE_SEARCH_WORK		= 1
GRID_X_POSITION_BACK_SEARCH_WORK		= 5
GRID_Y_POSITION_BACK_SEARCH_WORK		= 0
GRID_X_POSITION_SEARCH_WORK_TABLE_1		= 6
GRID_X_POSITION_SEARCH_WORK_TABLE_2		= 12
GRID_Y_POSITION_SEARCH_WORK_TABLE_1		= 0
GRID_Y_POSITION_SEARCH_WORK_TABLE_2		= 2
BUTTON_SIZE_SEARCH_WORKER_VIEW_X		= 200
BUTTON_SIZE_SEARCH_WORKER_VIEW_Y		= 50
SIZE_COLUMNS_TABLE_WORKERS				= 4

BUTTON_SIZE_MOD_WORKER_VIEW_X			= 150
BUTTON_SIZE_MOD_WORKER_VIEW_Y			= 50
ADMIN_MOD_WORKER_X						= 8
ADMIN_MOD_WORKER_Y						= 5
GRID_X_POSITION_ACTIVE					= 6
GRID_X_POSITION_CREATE_MOD_WORK			= 7
GRID_Y_POSITION_CREATE_MOD_WORK			= 1
GRID_X_POSITION_BACK_MOD_WORK			= 7
GRID_Y_POSITION_BACK_MOD_WORK			= 0

BUTTON_SIZE_INSERT_MARKS_VIEW_X			= 150
BUTTON_SIZE_INSERT_MARKS_VIEW_Y			= 50
ADMIN_INSERT_MARKS_X					= 6
ADMIN_INSERT_MARKS_Y					= 4
GRID_Y_POSITION_TEXT_MARKS_NAME			= 2
GRID_X_POSITION_INSERT_MARK				= 5
GRID_Y_POSITION_INSERT_MARK				= 3
GRID_X_POSITION_BACK_MARK				= 5
GRID_Y_POSITION_BACK_MARK				= 0
GRID_X_POSITION_DATE					= 3
GRID_Y_POSITION_DAY_DATE				= 1
GRID_Y_POSITION_MONTH_DATE				= 2
GRID_Y_POSITION_YEAR_DATE				= 3
GRID_X_POSITION_TIME					= 4
GRID_Y_POSITION_HOUR_TIME				= 1
GRID_Y_POSITION_MIN_TIME				= 2

MORE_YEARS								= 15
COLUMNS_IN_FILE							= 3
ERROR_FILE								= -1

INTRO_HOUR_DEFAULT						= 8
INTRO_MIN_DEFAULT						= 0
EXIT_HOUR_DEFAULT						= 17
EXIT_MIN_DEFAULT						= 0
DEFAULT_LUNCHTIME						= 60