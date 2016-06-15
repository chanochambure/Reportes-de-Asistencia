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

cursor.execute("""CREATE TABLE Area
				(
				id int PRIMARY KEY AUTO_INCREMENT,
				name varchar(30)
				)""")

db.commit()
db.close()
