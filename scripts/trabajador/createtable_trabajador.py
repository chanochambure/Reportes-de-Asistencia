#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
from PyQt4 import QtGui

#Import de Modulos
BASE_DIR='../../DATA'
sys.path.insert(0,BASE_DIR)
from constants import *

db=get_connection()
cursor=db.cursor()

cursor.execute("""CREATE TABLE Trabajador
				(
				pin varchar(15) PRIMARY KEY,
				name varchar(30),
				father_last_name varchar(30),
				mother_last_name varchar(30),
				activo boolean
				)""")

db.commit()
db.close()
