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
def mins_to_str_time(mins,minutos_de_trabajo):
	if(mins!=None and minutos_de_trabajo>0):
		horas=int(mins/60)
		real_mins=str(mins-horas*60)
		if(int(real_mins)<10):
			real_mins='0'+real_mins
		dias=int(mins/minutos_de_trabajo)
		diasd=int(horas/24)
		if(diasd>0):
			horas_t=int(minutos_de_trabajo/60)
			real_mins_t=str(minutos_de_trabajo-horas_t*60)
			if(int(real_mins_t)<10):
				real_mins_t='0'+real_mins_t
			str_tr=str(horas_t)+":"+real_mins_t+" h"
			return "Dias: "+str(dias)+" - Tiempo por Dia: "+str_tr+" - Tiempo Total: "+str(horas)+":"+real_mins+" h"
		return str(horas)+":"+real_mins+" h"
	return "Error - Faltan Marcaciones"

def mins_to_str_time_ot(mins,w_dat=False):
	if(mins!=None):
		nmins=(mins<0)
		mins=abs(mins)
		horas=int(mins/60)
		real_mins=str(mins-horas*60)
		if(int(real_mins)<10):
			real_mins='0'+real_mins
		dias=int((mins/60)/24)
		return_str=str(horas)+":"+real_mins+" h"
		if(w_dat):
			return_str="Dias: "+str(dias)+" - Tiempo Total: "+return_str
		if(nmins):
			return_str="Extra: "+return_str
		return return_str
	return "None"

def datetime_to_str(day,month,year,hour,minute):
	return year+"-"+month+"-"+day+" "+hour+":"+minute+":00"

def date_to_str(year,month,day):
	return year+"-"+month+"-"+day

def time_to_str(hour,minute):
	return hour+":"+minute+":00"

def time_get_hour(str_hour):
	return str(str_hour.split(":")[0])

def time_get_min(str_hour):
	return int(str_hour.split(":")[1])

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

def to_datetime_other(str_datetime):
	try:
		return_value=datetime.datetime.strptime(str(str_datetime),"%d/%m/%Y %I:%M:%S %p")
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
		if(char_u==unicode("'") or char_u==unicode(";") or char_u==unicode('"') or ord(char_u)>=128):
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
BUTTON_INSERT_AREA					= "Insertar Tipo"
BUTTON_CONTROL_AREAS				= "Control de Tipos"
BUTTON_EXIT							= "Salir"
ERROR_A_PROCESS_OPENED				= "Tiene ya una ventana abierta"
ADMIN_INSERT_WORKER_TITLE			= "Insertar Trabajador"
ADMIN_INSERT_AREA_TITLE				= "Insertar Tipo"
ADMIN_INSERT_WORKER_PIN				= "Numero de Identificacion"
ADMIN_INSERT_WORKER_NAME			= "Nombre"
ADMIN_INSERT_WORKER_FNAME			= "Apellido Paterno"
ADMIN_INSERT_WORKER_MNAME			= "Apellido Materno"
ADMIN_INSERT_INTRO_HOUR				= "Hora de Entrada"
ADMIN_INSERT_EXIT_HOUR				= "Hora de Salida"
ADMIN_MOD_WORKER_LUNCHDATE			= "Fecha Validez Refrigerio"
ADMIN_INSERT_LUNCHTIME_MINUTES		= "Tiempo para Refrigerio"
ADMIN_CONTROL_AREA_TITLE			= "Control de Tipos"
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
SEARCH_AREA_TITLE					= "Buscar Tipo"
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
CREATE_LUNCHTIME_LAST_MOD			= "\n Fecha Ultimo Refrigerio: "
BUTTON_INSERT_NEW_MARK				= "Crear Nueva Marcacion"
CREATE_AREA_EMPTY_CAMP				= "Existe un campo vacio"
CREATE_AREA_QUESTION				= "Esta seguro de crear un tipo con este nombre"
CREATE_AREA_INVALID_CAMP			= "El campo tiene un caracter no valido"
CREATE_AREA_SUCCESS					= "Tipo Insertada"
SEARCH_AREA_CONTROL_MESSAGE			= "Control de Tipo"
SEARCH_AREA_VIEW_TITLE				= "Buscar Tipo"
BUTTON_SEARCH_AREA					= "Buscar"
SEARCH_TITLE_AREA_ROWS				= ["Nombre","Accion"]
ADMIN_CONTROL_AREA_TYPE_TEXT		= "Areas"
ADMIN_CONTROL_REMOVE_AREA			= "Eliminar Tipo"
REMOVE_AREA_SUCCESS					= "Tipo Eliminada"
REMOVE_AREA_QUESTION				= "Desea eliminar el Tipo, esto eliminara todos las Areas y tambien las relaciones existentes entre trabajadores y areas"
ADMIN_CONTROL_AREA_INSERT_TYPE		= "Insertar Area"
ADMIN_INSERT_TYPE_TITLE				= "Insertar Area"
CREATE_TYPE_QUESTION				= "Esta seguro de asignar esta area con este nombre para el tipo de "
CREATE_TYPE_SUCCESS					= "Area Insertado"
CONTROL_AREA_LIST_HEADER_TABLE		= ["Nombre","Control","Eliminar"]
CONTROL_AREA_CONTROL_TYPE			= "Control"
CONTROL_AREA_REMOVE_TYPE			= "Remover"
REMOVE_TYPE_QUESTION				= "Esta seguro de eliminar esta area, esto eliminara todas las relaciones existentes entre trabajadores y areas"
REMOVE_TYPE_SUCCESS					= "Area Eliminado"
ADMIN_CONTROL_TYPE_TITLE			= "Control de Area"
ADMIN_CONTROL_AREA_RELATION_TEXT	= "Trabajadores"
ADMIN_CONTROL_AREA_INSERT_RELATION	= "Insertar Trabajador"
SEARCH_WORKER_SELECTION_MESSAGE		= "Seleccionar"
INSERT_RELATION_QUESTION_1			= "Desea establecerle a "
INSERT_RELATION_QUESTION_2			= " el area: "
CONTROL_TYPE_LIST_HEADER_TABLE		= ["Nombre","Apellido Paterno","Apellido Materno","Remover"]
INSERT_RELATION_SUCCESS				= "Trabajador Insertado"
INSERT_RELATION_ERROR				= "El trabajador seleccionado ya tiene esta area en este tipo"
CONTROL_TYPE_REMOVE_RELATION		= "Remover"
REMOVE_WORKER_QUESTION				= "Esta seguro de eliminar el area de este trabajador"
REMOVE_WORKER_SUCEESS				= "Relacion Removida"
CREATE_AREA_EXIST					= "El tipo ya existe"
CREATE_TYPE_EXIST					= "El area ya existe"
ADMIN_MOD_WORKER_HORARIODATE		= "Fecha Validez Horario"

#NUMBERS ADMIN
GRID_X_MAIN_WINDOW_ADMIN				= 3
GRID_Y_MAIN_WINDOW_ADMIN				= 10
GRID_X_POSITION_TITLE					= 0
GRID_X_POSITION_INSERT_WORKER			= 2
GRID_X_POSITION_MODIFY_WORKER			= 3
GRID_X_POSITION_INSERT_MARKS			= 4
GRID_X_POSITION_INSERT_MARKS_FROM_FILE	= 5
GRID_X_POSITION_CONTROL_MARKS			= 6
GRID_X_POSITION_INSERT_AREA				= 7
GRID_X_POSITION_CONTROL_AREAS			= 8
GRID_X_POSITION_EXIT					= 9
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

MORE_YEARS								= 25
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

ADMIN_INSERT_AREA_X						= 3
ADMIN_INSERT_AREA_Y						= 2
BUTTON_SIZE_INSERT_AREA_VIEW_X			= 150
BUTTON_SIZE_INSERT_AREA_VIEW_Y			= 40
GRID_X_POSITION_INSERT_AREA_TITLE		= 0
GRID_Y_POSITION_INSERT_AREA_TITLE		= 0
GRID_X_POSITION_NAME_INSERT_AREA		= 1
GRID_Y_POSITION_LABEL_INSERT_AREA		= 0
GRID_Y_POSITION_TEXT_INSERT_AREA		= 1
GRID_X_POSITION_CREATE_INSERT_AREA		= 2
GRID_Y_POSITION_CREATE_INSERT_AREA		= 1
GRID_X_POSITION_BACK_INSERT_AREA		= 2
GRID_Y_POSITION_BACK_INSERT_AREA		= 0

BUTTON_SIZE_SEARCH_AREA_VIEW_X			= 150
BUTTON_SIZE_SEARCH_AREA_VIEW_Y			= 40
SIZE_COLUMNS_TABLE_AREA					= 2
SEARCH_AREA_X_GRID						= 12
SEARCH_AREA_Y_GRID						= 5
GRID_X_POSITION_SEARCH_AREA_TITLE		= 0
GRID_Y_POSITION_SEARCH_AREA_TITLE		= 0

CONTROL_AREA_X_GRID						= 6
CONTROL_AREA_Y_GRID						= 6
GRID_X_POSITION_TITLE_CONTROL_AREA		= 0
GRID_Y_POSITION_TITLE_CONTROL_AREA		= 0
GRID_X_POSITION_TYPE_CONTROL_AREA		= 1
GRID_Y_POSITION_TYPE_CONTROL_AREA		= 0
GRID_X_POSITION_BUTTON_BACK_C_AREA		= 5
GRID_Y_POSITION_BUTTON_BACK_C_AREA		= 5
GRID_X_POSITION_BUTTON_REMO_C_AREA		= 0
GRID_Y_POSITION_BUTTON_REMO_C_AREA		= 5
GRID_X_POSITION_BUTTON_INS_T_C_AREA		= 2
GRID_Y_POSITION_BUTTON_INS_T_C_AREA		= 5
SIZE_COLUMNS_TABLE_TYPES_AREA			= 3
GRID_X_POSITION_TABLE_C_AREA			= 2
GRID_Y_POSITION_TABLE_C_AREA			= 0
GRID_X_SIZE_TABLE_C_AREA				= 4
GRID_Y_SIZE_TABLE_C_AREA				= 4

CONTROL_TYPE_X_GRID						= 6
CONTROL_TYPE_Y_GRID						= 5
GRID_X_POSITION_TITLE_CONTROL_TYPE		= 0
GRID_Y_POSITION_TITLE_CONTROL_TYPE		= 0
GRID_X_POSITION_RELATION_CONTROL_TYPE	= 1
GRID_Y_POSITION_RELATION_CONTROL_TYPE	= 0
GRID_X_POSITION_BUTTON_BACK_C_TYPE		= 4
GRID_Y_POSITION_BUTTON_BACK_C_TYPE		= 4
GRID_X_POSITION_BUTTON_INS_R_C_TYPE		= 2
GRID_Y_POSITION_BUTTON_INS_R_C_TYPE		= 4
SIZE_COLUMNS_TABLE_WORK_TYPE			= 4
GRID_X_POSITION_TABLE_C_TYPE			= 2
GRID_Y_POSITION_TABLE_C_TYPE			= 0
GRID_X_SIZE_TABLE_C_TYPE				= 4
GRID_Y_SIZE_TABLE_C_TYPE				= 4



#TEXT REPORTES
MAIN_VIEW_TITLE_REPORTES					= "Rerpotes de Asistencias"
BUTTON_REPORTES_LUCHTIME					= "Tiempos de Refrigerio"
BUTTON_REPORTES_TARDANZAS					= "Tardanzas"
BUTTON_REPORTES_HORAS						= "Horas Trabajadas"
BUTTON_REPORTES_HORAS_AREA					= "Lista - Horas Trabajadas"
REPORTES_LUNCHTIME_TITLE					= "Tiempos de Refrigerio"
REPORTES_TARDANZA_TITLE						= "Tardanzas"
REPORTES_HORAS_TITLE						= "Horas Trabajadas"
REPORTES_HORAS_AREA_TITLE					= "Lista - Horas Trabajadas"
SEARCH_SEE_REPORTES_LUNCHTIME_MESSAGE		= "Ver Refrigerios"
SEARCH_SEE_REPORTES_TARDANZA_MESSAGE		= "Ver Tardanzas"
SEARCH_SEE_REPORTES_HORAS_MESSAGE			= "Horas Trabajadas"
LISTA_TABLE_LUNCHTIME						= ["Fecha","Minutos"]
REPORTE_LABEL_NAME							= "Trabajador"
BUTTON_REPORTE								= "Generar Reporte"
REPORTE_TOTAL_HORAS_EMPTY					= "--"
REPORTE_LABEL_TOTAL_HORAS					= "Total Trabajado"
BUTTON_EXCEL								= "Exportar a Excel"
BUTTON_CONTROL_MARK							= "Abrir Control de Marcaciones"
REPORTE_HORAS_TITLE_ROWS					= ["Fecha","Horas:Minutos Trabajados","Ver"]
REPORTE_TARDANZA_TITLE_ROWS					= ["Fecha","Total Marcaciones","Tardanza Entrada","Tardanza Salida","Tardanza en Refrigerio","TOTAL","Ver"]
REPORTE_LABEL_TOTAL_MINUTOS_TARDE			= "Total Tarde"
CONTROL_MARK_OPENED							= "El Control de Marcaciones se encuentra Abierto"
NONE_TO_SAVE								= "Nada que Guardar"
SAVE_FILE_TITLE								= "Guardar Rerporte"
CREATE_EXCEL_SUCCESS						= "Reporte Guardado"
EXCEL_PROBLEM								= "No tiene permisos para editar el archivo, cierre todos los programas que esten usando el archivo"
MODIFICAR_REPORTE_MARKS						= "Ver"
REPO_AREA_NAME_R_H_A						= "Tipo"
REPO_TIPO_NAME_R_H_A						= "Area"
REPORTE_HORAS_AREA_HEADER					= ["Nombre Completo","Total Trabajado"]

#NUMBERS REPORTES
GRID_X_MAIN_WINDOW_REPORTES					= 7
GRID_Y_MAIN_WINDOW_REPORTES					= 3
GRID_X_POSITION_TITLE_R						= 0
GRID_X_POSITION_EXIT_R						= 6
GRID_X_POSITION_REPORTE_HORAS_A_R			= 5
GRID_X_POSITION_REPORTE_LUNCHTIME_R			= 4
GRID_X_POSITION_REPORTE_TARDANZA_R			= 3
GRID_X_POSITION_REPORTE_HORAS_R				= 2
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

REPORTE_HORAS_X_GRID						= 11
REPORTE_HORAS_Y_GRID						= 5
GRID_X_POSITION_TITLE_REP_HORAS				= 0
GRID_Y_POSITION_TITLE_REP_HORAS				= 0
GRID_X_POSITION_NAME_REP_HORAS				= 1
GRID_Y_POSITION_NAME_REP_HORAS				= 0
GRID_Y_POSITION_TEXT_N_REP_HORAS			= 1
GRID_X_POSITION_TOTAL_LABEL_REP_HORAS		= 2
GRID_Y_POSITION_TOTAL_LABEL_REP_HORAS		= 4
GRID_X_POSITION_TOTAL_REP_HORAS				= 3
GRID_Y_POSITION_TOTAL_REP_HORAS				= 4
GRID_X_POSITION_REPO_REP_HORAS				= 1
GRID_Y_POSITION_REPO_REP_HORAS				= 4
GRID_X_POSITION_EXCEL_REP_HORAS				= 10
GRID_Y_POSITION_EXCEL_REP_HORAS				= 2
GRID_X_POSITION_CMARK_REP_HORAS				= 10
GRID_Y_POSITION_CMARK_REP_HORAS				= 4
GRID_X_POSITION_BACK_REP_HORAS				= 10
GRID_Y_POSITION_BACK_REP_HORAS				= 0
GRID_X_POSITION_DATEMARK_REP_HORAS			= 2
GRID_Y_POSITION_LABEL_DATE					= 0
GRID_Y_POSITION_DAY_DATEMARK_REP_HORAS		= 1
GRID_Y_POSITION_MONTH_DATEMARK_REP_HORAS	= 2
GRID_Y_POSITION_YEAR_DATEMARK_REP_HORAS		= 3
REPORTES_HORAS_BUTTON_SIZE_X				= 350
REPORTES_HORAS_BUTTON_SIZE_Y				= 100

SIZE_COLUMNS_TABLE_REPORTE_HORAS			= 3
GRID_X_POSITION_REPORTE_HORAS_TABLE_1		= 4
GRID_X_POSITION_REPORTE_HORAS_TABLE_2		= 6
GRID_Y_POSITION_REPORTE_HORAS_TABLE_1		= 0
GRID_Y_POSITION_REPORTE_HORAS_TABLE_2		= 5
SIZE_COLUMNS_TABLE_REPORTE_TARDANZA			= 7

REPORTE_HORAS_AREA_X_GRID					= 10
REPORTE_HORAS_AREA_Y_GRID					= 6
GRID_X_POSITION_TITLE_R_HORAS_AREA			= 0
GRID_Y_POSITION_TITLE_R_HORAS_AREA			= 0
GRID_X_POSITION_BUTTON_BACK_R_H_A			= 9
GRID_Y_POSITION_BUTTON_BACK_R_H_A			= 1
GRID_X_POSITION_EXCEL_R_H_A					= 9
GRID_Y_POSITION_EXCEL_R_H_A					= 4
GRID_X_POSITION_REPO_R_H_A					= 2
GRID_Y_POSITION_REPO_R_H_A					= 5
GRID_X_POSITION_DATEMARK_R_H_A				= 2
GRID_Y_POSITION_DAY_DATEMARK_R_H_A			= 1
GRID_Y_POSITION_MONTH_DATEMARK_R_H_A		= 2
GRID_Y_POSITION_YEAR_DATEMARK_R_H_A			= 3
GRID_X_POSITION_CONFIG_R_H_A				= 1
GRID_Y_POSITION_R_H_A_LABEL_A				= 1
GRID_Y_POSITION_R_H_A_LABEL_T				= 3
GRID_Y_POSITION_R_H_A_BOX_A					= 2
GRID_Y_POSITION_R_H_A_BOX_T					= 4
GRID_X_POSITION_R_H_A_T						= 4
GRID_Y_POSITION_R_H_A_T						= 0
GRID_X_SIZE_R_H_A_T							= 5
GRID_Y_SIZE_R_H_A_T							= 6
SIZE_COLUMNS_TABLE_REPORTE_HORAS_AREA		= 2




#Importantes
VALUE_NOT_WORK								= "-"
TOTAL_MARKS_LIMIT_FOR_DAY					= 4
TOTAL_MARKS_SATURDAY						= 2
TOTAL_TIME_TARDANZA_LIMIT					= 5