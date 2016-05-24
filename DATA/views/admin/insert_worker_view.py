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

class insert_worker_view(QDialog):
	def __init__(self,parent=None):
		super(insert_worker_view, self).__init__(parent)
		#crear la ventana
		self.insert_worker_create()
		#Dando tamaño a la pantalla
		self.setWindowTitle(ADMIN_INSERT_WORKER_TITLE)
		self.show()

	def insert_worker_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(ADMIN_INSERT_WORKER_TITLE)
		label_pin = QLabel(ADMIN_INSERT_WORKER_PIN)
		label_name = QLabel(ADMIN_INSERT_WORKER_NAME)
		label_father_last_name = QLabel(ADMIN_INSERT_WORKER_FNAME)
		label_mother_last_name = QLabel(ADMIN_INSERT_WORKER_MNAME)
		self.text_pin = QLineEdit()
		self.text_name = QLineEdit()
		self.text_fname = QLineEdit()
		self.text_mname = QLineEdit()
		button_create = QPushButton(BUTTON_CREATE_WORKER,self)
		button_back = QPushButton(BUTTON_BACK,self)

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		button_create.setFixedSize(BUTTON_SIZE_INSERT_WORKER_VIEW_X,BUTTON_SIZE_INSERT_WORKER_VIEW_Y)
		button_back.setFixedSize(BUTTON_SIZE_INSERT_WORKER_VIEW_X,BUTTON_SIZE_INSERT_WORKER_VIEW_Y)

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)
		self.connect(button_create, SIGNAL("clicked()"),self.create_worker)

		#GRID SIZE
		grid.setHorizontalSpacing(GRID_X_MAIN_WINDOW_ADMIN)
		grid.setVerticalSpacing(GRID_Y_MAIN_WINDOW_ADMIN)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_INSERT_WORK_TITLE,GRID_Y_POSITION_INSERT_WORK_TITLE)
		grid.addWidget(label_pin,GRID_X_POSITION_PIN,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_name,GRID_X_POSITION_NAME,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_father_last_name,GRID_X_POSITION_FNAME,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_mother_last_name,GRID_X_POSITION_MNAME,GRID_Y_POSITION_LABEL)
		grid.addWidget(self.text_pin,GRID_X_POSITION_PIN,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_name,GRID_X_POSITION_NAME,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_fname,GRID_X_POSITION_FNAME,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_mname,GRID_X_POSITION_MNAME,GRID_Y_POSITION_TEXT)
		grid.addWidget(button_create,GRID_X_POSITION_CREATE_INSERT_WORK,GRID_Y_POSITION_CREATE_INSERT_WORK)
		grid.addWidget(button_back,GRID_X_POSITION_BACK_INSERT_WORK,GRID_Y_POSITION_BACK_INSERT_WORK)

		#LAYAOUT
		self.setLayout(grid)

	def create_worker(self):
		pin = self.text_pin.text()
		name = self.text_name.text()
		fname = self.text_fname.text()
		mname = self.text_mname.text()
		if(pin == '' or name == '' or fname=='' or mname==''):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_EMPTY_CAMP, QMessageBox.Ok)
		elif(str_is_invalid(pin) or str_is_invalid(name) or str_is_invalid(fname) or str_is_invalid(mname)):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_INVALID_CAMP, QMessageBox.Ok)
		elif(is_number(pin)==False):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_INVALID_PIN, QMessageBox.Ok)
		else:
			reply=QMessageBox.question(self, 'Message',CREATE_WORKER_QUESTION,QMessageBox.Yes,QMessageBox.No)
			if reply == QMessageBox.Yes:
				db=get_connection()
				if(db):
					new_worker = trabajador.Trabajador([pin,name,fname,mname,True])
					if(controller_trabajador.pin_is_invalid(pin,db)):
						QMessageBox.warning(self, 'Error',CREATE_WORKER_ALREADY_HAS_BEEN_USED, QMessageBox.Ok)
					elif(new_worker.insert(db.cursor())):
						db.commit()
						db.close()
						self.close()
