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

def date_to_str(year,month,day):
	return year+"-"+month+"-"+day

def time_to_str(hour,minute):
	return hour+":"+minute+":00"

def to_datetime(str_datetime,tipo):
	try:
		if(tipo):
			return_value=datetime.datetime.strptime(str(str_datetime),"%Y-%m-%d %H:%M:%S")
			return return_value
		else:
			return_value=datetime.datetime.strptime(str(str_datetime),"%d/%m/%Y %H:%M")
			return return_value
	except ValueError:
		return None

def to_date(str_date,tipo):
	try:
		if(tipo):
			return_value=datetime.datetime.strptime(str(str_date),"%Y-%m-%d").date()
			return return_value
		else:
			return_value=datetime.datetime.strptime(str(str_date),"%d/%m/%Y").date()
			return return_value
	except ValueError:
		return None

#UNICODE
def str_is_invalid(str_u):
	for char_u in unicode(str_u):
		if(char_u=="'" or char_u==";" or char_u=='"'):
			return True
	return False

#IS A NUMBER
def is_number(str_n):
	for char_n in str(str_n):
		if(ord(char_n)<48 or ord(char_n)>57):
			return False
	return True

#TEXT ADMIN
MAIN_TITLE							= "Reporte de Asistencias"
MAIN_VIEW_TITLE_ADMIN				= "Administrador:\nReportes de Asistencias"
BUTTON_INSERT_WORKER				= "Insertar Trabajador"
BUTTON_MARKS						= "Insertar Marcacion"
BUTTON_MARKS_FROM_FILE				= "Insertar Marcaciones desde un archivo"
BUTTON_MODIFY_WORKER				= "Modificar Trabajador"
BUTTON_CONTROL_MARKS				= "Control de Marcaciones"
BUTTON_EXIT							= "Salir"
ERROR_A_PROCESS_OPENED				= "Tiene ya una ventana abierta"
ADMIN_INSERT_WORKER_TITLE			= "Insertar Trabajador"
ADMIN_INSERT_WORKER_PIN				= "Numero de Identificacion"
ADMIN_INSERT_WORKER_NAME			= "Nombre"
ADMIN_INSERT_WORKER_FNAME			= "Apellido Paterno"
ADMIN_INSERT_WORKER_MNAME			= "Apellido Materno"
ADMIN_INSERT_INTRO_HOUR				= "Hora de Entrada"
ADMIN_INSERT_EXIT_HOUR				= "Hora de Salida"
ADMIN_MOD_WORKER_LUNCHDATE			= "Fecha de Cambio"
ADMIN_INSERT_LUNCHTIME_MINUTES		= "Tiempo para Refrigerio"
BUTTON_CREATE_WORKER				= "Insertar"
BUTTON_BACK							= "Atras"
CREATE_WORKER_EMPTY_CAMP			= "Existe algun Campo Vacio"
CREATE_WORKER_INVALID_CAMP			= "Existe caracteres no validos"
CREATE_WORKER_INVALID_PIN			= "El PIN solo puede tener caracteres numericos"
CREATE_WORKER_INVALID_LT_MINUTES	= "El tiempo para refrigerio solo puede tener caracteres numericos"
CREATE_WORKER_QUESTION				= "Esta seguro de crear a este nuevo Trabajador"
CREATE_WORKER_SUCCESS				= "Trabajador Creado"
CREATE_WORKER_BD_ERROR				= "Error con la Base de Datos"
CREATE_WORKER_ALREADY_HAS_BEEN_USED	= "El PIN ya esta siendo usando por otra persona"
SEARCH_WORKER_MODIFY_MESSAGE		= "Modificar"
SEARCH_WORKER_MARKS_MESSAGE			= "Insertar Marcacion"
SEARCH_WORKER_CONTROL_MESSAGE		= "Control"
SEARCH_WORKER_TITLE					= "Buscar Trabajador"
SEARCH_WORKER_VIEW_TITLE			= "Buscar Trabajador"
BUTTON_SEARCH_WORKER				= "Buscar"

SEARCH_TITLE_ROWS					= "Nombres;Apellido Paterno;Apellido Materno;Accion"
SPLIT_TABLE_WORKERS					= ";"
SEARCH_MARKS_TITLE_ROWS				= "Fecha - Hora;Activo;Accion"
SPLIT_TABLE_MARKS					= ";"

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
FIRST_DATE							= "01/01/01"
ADMIN_CONTROL_MARKS_TITLE			= "Control de Marcaciones"
BUTTON_SEARCH_MARK					= "Buscar Marcaciones"
ADMIN_CONTROL_MARKS_DATE1			= "Fecha Inicio"
ADMIN_CONTROL_MARKS_DATE2			= "Fecha Final"
CONTROL_MARK_SEARCH_MESSAGE			= "Modificar"
CONTROL_MARK_ACTIVO					= "Valido"
CONTROL_MARK_INACTIVO				= "No Valido"
MODIFY_MARK_OPENED					= "Tiene una ventana abierta de Marcacion"
ADMIN_MODIFY_MARK_TITLE				= "Modificar Marcacion"
BUTTON_MODIFY_MARKS					= "Modificar"
ADMIN_MODIFY_MARK_VALID				= "Valido"
CREATE_MARK_MODIFY_QUESTION			= "Esta seguro de modificar"
MOD_MARK_SUCCESS					= "Modificacion Hecha"
WORKER_WITH_MARK_OR_NO_MODIFICATION	= "El usuario tiene una marcacion en este dia con dicha hora o no hubo modificaciones"
ADMIN_CONTROL_MARKS_VALIDO			= "Mostrar No Validos"
CREATE_LUNCHTIME_INVALID_DATE		= "No puede crear un tiempo de refrigerio para un fecha que es anterior al ultimo refrigerio"

#NUMBERS ADMIN
GRID_X_MAIN_WINDOW_ADMIN				= 3
GRID_Y_MAIN_WINDOW_ADMIN				= 8
GRID_X_POSITION_TITLE					= 0
GRID_X_POSITION_INSERT_WORKER			= 2
GRID_X_POSITION_MODIFY_WORKER			= 3
GRID_X_POSITION_INSERT_MARKS			= 4
GRID_X_POSITION_INSERT_MARKS_FROM_FILE	= 5
GRID_X_POSITION_CONTROL_MARKS			= 6
GRID_X_POSITION_EXIT					= 7
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
ADMIN_MOD_WORKER_Y						= 6
GRID_X_POSITION_ACTIVE					= 6
GRID_X_POSITION_CREATE_MOD_WORK			= 7
GRID_Y_POSITION_CREATE_MOD_WORK			= 1
GRID_X_POSITION_BACK_MOD_WORK			= 7
GRID_Y_POSITION_BACK_MOD_WORK			= 0
GRID_X_POSITION_DATELUNCH				= 5
GRID_Y_POSITION_DAY_LUNCHDATE			= 3
GRID_Y_POSITION_MONTH_LUNCHDATE			= 4
GRID_Y_POSITION_YEAR_LUNCHDATE			= 5

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

BUTTON_SIZE_SEARCH_MARKS_VIEW_X			= 140
BUTTON_SIZE_SEARCH_MARKS_VIEW_Y			= 30
SIZE_COLUMNS_TABLE_MARKS				= 3
SEARCH_MARKS_X_GRID						= 12
SEARCH_MARKS_Y_GRID						= 5
GRID_X_POSITION_BACK_SEARCH_MARK		= 6
GRID_Y_POSITION_BACK_SEARCH_MARK		= 0
GRID_X_POSITION_CREATE_SEARCH_MARK		= 3
GRID_Y_POSITION_CREATE_SEARCH_MARK		= 4
GRID_X_POSITION_VALIDO					= 5
GRID_X_POSITION_DATEMARK				= 3
GRID_Y_POSITION_SEARCH_MARK_DATE		= 0
GRID_Y_POSITION_DAY_DATEMARK			= 1
GRID_Y_POSITION_MONTH_DATEMARK			= 2
GRID_Y_POSITION_YEAR_DATEMARK			= 3
GRID_X_POSITION_SEARCH_MARK_TITLE		= 0
GRID_Y_POSITION_SEARCH_MARK_TITLE		= 0
GRID_X_POSITION_SEARCH_MARK_TABLE_1		= 8
GRID_X_POSITION_SEARCH_MARK_TABLE_2		= 12
GRID_Y_POSITION_SEARCH_MARK_TABLE_1		= 0
GRID_Y_POSITION_SEARCH_MARK_TABLE_2		= 4

ADMIN_MOFIDY_MARKS_X					= 7
ADMIN_MOFIDY_MARKS_Y					= 4
GRID_X_POSITION_MODIFY_MARK				= 6
GRID_Y_POSITION_MODIFY_MARK				= 1
GRID_X_POSITION_BACK_MODIFY_MARK		= 6
GRID_Y_POSITION_BACK_MODIFY_MARK		= 0

#TEXT REPORTES
MAIN_VIEW_TITLE_REPORTES					= "Rerpotes de Asistencias"
BUTTON_REPORTES_LUCHTIME					= "Tiempos de Refrigerio"
REPORTES_LUNCHTIME_TITLE					= "Tiempos de Refrigerio"
SEARCH_SEE_REPORTES_LUNCHTIME_MESSAGE		= "Ver Refrigerios"
LISTA_TABLE_LUNCHTIME						= ["Fecha","Minutos"]

#NUMBERS REPORTES
GRID_X_MAIN_WINDOW_REPORTES					= 6
GRID_Y_MAIN_WINDOW_REPORTES					= 3
GRID_X_POSITION_TITLE_R						= 0
GRID_X_POSITION_EXIT_R						= 5
GRID_X_POSITION_REPORTE_LUNCHTIME_R			= 4
GRID_Y_POSITION_BUTTON_R					= 1

BUTTON_SIZE_REPORTE_LUNCHTIME_VIEW_X		= 150
BUTTON_SIZE_REPORTE_LUNCHTIME_VIEW_Y		= 50
SIZE_COLUMNS_TABLE_LUNCHTIME				= 2
REPORTE_LUNCHTIME_X_GRID					= 8
REPORTE_LUNCHTIME_Y_GRID					= 3
GRID_X_POSITION_REPORTE_LUNCHTIME_TITLE		= 1
GRID_Y_POSITION_REPORTE_LUNCHTIME_TITLE		= 0
GRID_X_POSITION_REPORTE_LUNCHTIME_TABLE_1	= 2
GRID_X_POSITION_REPORTE_LUNCHTIME_TABLE_2	= 5
GRID_Y_POSITION_REPORTE_LUNCHTIME_TABLE_1	= 0
GRID_Y_POSITION_REPORTE_LUNCHTIME_TABLE_2	= 4
GRID_X_POSITION_BACK_REPORTE_LUNCHTIME		= 7
GRID_Y_POSITION_BACK_REPORTE_LUNCHTIME		= 0