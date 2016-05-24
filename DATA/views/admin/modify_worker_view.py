#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from datetime import datetime

#Import de Modulos
BASE_DIR='../../'
sys.path.insert(0,BASE_DIR)
from constants import *
from models import trabajador
from controller import controller_trabajador

class modify_worker_view(QDialog):
	def __init__(self,parent=None):
		super(modify_worker_view, self).__init__(parent)
		#crear la ventana
		self.modify_worker_create()
		#Dando tamaño a la pantalla
		self.setWindowTitle(ADMIN_INSERT_WORKER_TITLE)
		self.show()

	def modify_worker_create(self):
		print "create"
