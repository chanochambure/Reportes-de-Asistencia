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
from models import area
from controller import controller_area

class insert_area_view(QDialog):
	def __init__(self,parent=None):
		super(insert_area_view, self).__init__(parent)
		#crear la ventana
		self.insert_area_create()
		#Dando tamaño a la pantalla
		self.setWindowTitle(ADMIN_INSERT_AREA_TITLE)
		self.show()

	def insert_area_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(ADMIN_INSERT_AREA_TITLE)
		label_name = QLabel(ADMIN_INSERT_WORKER_NAME)
		self.text_name = QLineEdit()
		button_create = QPushButton(BUTTON_CREATE_WORKER,self)
		button_back = QPushButton(BUTTON_BACK,self)

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		button_create.setFixedSize(BUTTON_SIZE_INSERT_AREA_VIEW_X,BUTTON_SIZE_INSERT_AREA_VIEW_Y)
		button_back.setFixedSize(BUTTON_SIZE_INSERT_AREA_VIEW_X,BUTTON_SIZE_INSERT_AREA_VIEW_Y)

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)
		self.connect(button_create, SIGNAL("clicked()"),self.create_area)

		#GRID SIZE
		grid.setHorizontalSpacing(ADMIN_INSERT_AREA_X)
		grid.setVerticalSpacing(ADMIN_INSERT_AREA_Y)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_INSERT_AREA_TITLE,GRID_Y_POSITION_INSERT_AREA_TITLE)
		grid.addWidget(label_name,GRID_X_POSITION_NAME_INSERT_AREA,GRID_Y_POSITION_LABEL_INSERT_AREA)

		grid.addWidget(self.text_name,GRID_X_POSITION_NAME_INSERT_AREA,GRID_Y_POSITION_TEXT_INSERT_AREA)

		grid.addWidget(button_create,GRID_X_POSITION_CREATE_INSERT_AREA,GRID_Y_POSITION_CREATE_INSERT_AREA)
		grid.addWidget(button_back,GRID_X_POSITION_BACK_INSERT_AREA,GRID_Y_POSITION_BACK_INSERT_AREA)

		#LAYAOUT
		self.setLayout(grid)

	def create_area(self):
		name = self.text_name.text()
		if(name == ''):
			QMessageBox.warning(self, 'Error',CREATE_AREA_EMPTY_CAMP, QMessageBox.Ok)
		elif(str_is_invalid(name)):
			QMessageBox.warning(self, 'Error',CREATE_AREA_INVALID_CAMP, QMessageBox.Ok)
		else:
			reply=QMessageBox.question(self, 'Message',CREATE_AREA_QUESTION,QMessageBox.Yes,QMessageBox.No)
			if reply == QMessageBox.Yes:
				db=get_connection()
				if(db):
					if(controller_area.exist_this_area(db,name)):
						db.close()
						QMessageBox.warning(self, 'Error',CREATE_AREA_EXIST, QMessageBox.Ok)
					else:
						new_area = area.Area([0,name])
						new_area.insert(db.cursor())
						db.commit()
						db.close()
						QMessageBox.question(self, 'Message',CREATE_AREA_SUCCESS,QMessageBox.Ok)
						self.close()
