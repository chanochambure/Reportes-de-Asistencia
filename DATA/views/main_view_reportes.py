#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from constants import *
from views.admin import insert_worker_view,insert_marks_view,modify_worker_view
from views import search_worker_view
from controller import controller_mark

class main_view_reportes(QWidget):
	def __init__(self):
		self.ventana=None
		super(main_view_reportes, self).__init__()
		self.main_view_create()
		screenGeometry = QApplication.desktop().availableGeometry()
		self.resize(screenGeometry.width()/4,screenGeometry.height()/2)
		self.setWindowTitle(MAIN_TITLE)
		self.show()
		self.singleton_widget=False

	def main_view_create(self):
		print "create"

	def closeEvent(self, evnt):
		if(self.ventana):
			self.ventana.close()
