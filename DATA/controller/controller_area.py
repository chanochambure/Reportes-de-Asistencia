#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from models import trabajador,mark,lunchtime,area
from constants import *

def get_areas(db,str_name):
	cursor=db.cursor()
	list_areas=[]
	select_areas="""select * from Area where
					name LIKE '%s'"""%("%"+str_name+"%")
	select_areas+=" ORDER BY name"
	cursor.execute(select_areas)
	for row in cursor:
		list_areas.append(area.Area(row))
	return list_areas