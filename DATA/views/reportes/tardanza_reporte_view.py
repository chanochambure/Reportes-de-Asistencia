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
from models import mark,lunchtime,trabajador
from controller import *

class tardanza_reporte_view(QDialog):
	def __init__(self,worker_to_set,parent=None):
		self.modify_mark_singleton=False
		self.ventana=None
		super(tardanza_reporte_view, self).__init__(parent)
		self.worker=worker_to_set
		self.tardanza_reporte_create()
		screenGeometry = QApplication.desktop().availableGeometry()
		self.resize(screenGeometry.width(), screenGeometry.height())
		self.showMaximized()
		self.setWindowTitle(REPORTES_TARDANZA_TITLE)
		self.show()

	def tardanza_reporte_create(self):
		print "hey"