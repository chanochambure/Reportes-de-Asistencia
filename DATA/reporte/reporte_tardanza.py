#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
import datetime

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from models import mark,trabajador,lunchtime
from constants import *
from controller import *

def get_reporte_tardanza(pin,str_date1,str_date2,db,only_activas=True):
	lista_reporte=[]
	return lista_reporte

def get_total_minutes(matrix):
	return -1