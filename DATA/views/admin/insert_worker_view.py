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

class insert_worker_view(QDialog):
	def __init__(self,parent=None):
		super(insert_worker_view, self).__init__(parent)
		#crear la ventana
		self.insert_worker_create()
		#Dando tamaño a la pantalla
		size=self.size()
		desktopSize=QDesktopWidget().screenGeometry()
		top=(3*desktopSize.height()/4)
		left=(desktopSize.width()/2)
		self.resize(left, top)
		self.setWindowTitle(ADMIN_INSERT_WORKER_TITLE)
		self.show()

	def insert_worker_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(ADMIN_INSERT_WORKER_TITLE)
		button_create = QPushButton(BUTTON_CREATE_WORKER,self)
		button_back = QPushButton(BUTTON_BACK,self)

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		button_create.setFixedSize(BUTTON_SIZE_INSERT_WORKER_VIEW,button_create.height())
		button_back.setFixedSize(BUTTON_SIZE_INSERT_WORKER_VIEW,button_back.height())

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)
		self.connect(button_create, SIGNAL("clicked()"),self.create_worker)

		#GRID SIZE
		grid.setHorizontalSpacing(GRID_X_MAIN_WINDOW_ADMIN)
		grid.setVerticalSpacing(GRID_Y_MAIN_WINDOW_ADMIN)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_INSERT_WORK_TITLE,GRID_Y_POSITION_INSERT_WORK_TITLE)
		grid.addWidget(button_create,GRID_X_POSITION_CREATE_INSERT_WORK,GRID_Y_POSITION_CREATE_INSERT_WORK)
		grid.addWidget(button_back,GRID_X_POSITION_BACK_INSERT_WORK,GRID_Y_POSITION_BACK_INSERT_WORK)

		#LAYAOUT
		self.setLayout(grid)

	def create_worker(self):
		print "create"