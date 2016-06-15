#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import datetime

#Import de Modulos
BASE_DIR='../../'
sys.path.insert(0,BASE_DIR)
from constants import *
from models import area
from views.admin import insert_type_view
from controller import controller_area,controller_tipo

class control_type_view(QDialog):
	def __init__(self,type_to_set,parent=None):
		self.type_singleton=False
		self.ventana=None
		super(control_type_view, self).__init__(parent)
		self.type_m=type_to_set
		self.relation_list=[]
		#crear la ventana
		self.control_type_create()
		#Dando tamaño a la pantalla
		screenGeometry = QApplication.desktop().availableGeometry()
		self.resize(screenGeometry.width()/2,2*screenGeometry.height()/3)
		self.setWindowTitle(ADMIN_CONTROL_AREA_TITLE)
		self.show()

	def control_type_create(self):
		#GRID
		grid = QGridLayout()

		#LAYAOUT
		self.setLayout(grid)

	def closeEvent(self, evnt):
		if(self.ventana):
			self.ventana.close()
