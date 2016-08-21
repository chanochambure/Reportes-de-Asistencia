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
from models import trabajador, lunchtime, horario
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
		label_intro_hour = QLabel(ADMIN_INSERT_INTRO_HOUR)
		label_exit_hour = QLabel(ADMIN_INSERT_EXIT_HOUR)
		label_lunchtime = QLabel(ADMIN_INSERT_LUNCHTIME_MINUTES)
		self.text_pin = QLineEdit()
		self.text_name = QLineEdit()
		self.text_fname = QLineEdit()
		self.text_mname = QLineEdit()
		self.text_lunchtime = QLineEdit()
		self.text_intro_hour = QComboBox()
		self.text_intro_min = QComboBox()
		self.text_exit_hour = QComboBox()
		self.text_exit_min = QComboBox()
		button_create = QPushButton(BUTTON_CREATE_WORKER,self)
		button_back = QPushButton(BUTTON_BACK,self)

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		self.text_lunchtime.setText(str(DEFAULT_LUNCHTIME))
		button_create.setFixedSize(BUTTON_SIZE_INSERT_WORKER_VIEW_X,BUTTON_SIZE_INSERT_WORKER_VIEW_Y)
		button_back.setFixedSize(BUTTON_SIZE_INSERT_WORKER_VIEW_X,BUTTON_SIZE_INSERT_WORKER_VIEW_Y)
		for hour in range(0,24):
			str_hour=str(hour)
			if(hour<10):
				str_hour="0"+str_hour
			self.text_intro_hour.addItem(str_hour)
			self.text_exit_hour.addItem(str_hour)
		for min in range(0,60):
			str_min=str(min)
			if(min<10):
				str_min="0"+str_min
			self.text_intro_min.addItem(str_min)
			self.text_exit_min.addItem(str_min)
		self.text_intro_hour.setCurrentIndex(INTRO_HOUR_DEFAULT)
		self.text_intro_min.setCurrentIndex(INTRO_MIN_DEFAULT)
		self.text_exit_hour.setCurrentIndex(EXIT_HOUR_DEFAULT)
		self.text_exit_min.setCurrentIndex(EXIT_MIN_DEFAULT)

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)
		self.connect(button_create, SIGNAL("clicked()"),self.create_worker)

		#GRID SIZE
		grid.setHorizontalSpacing(ADMIN_INSERT_WORKER_X)
		grid.setVerticalSpacing(ADMIN_INSERT_WORKER_Y)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_INSERT_WORK_TITLE,GRID_Y_POSITION_INSERT_WORK_TITLE)
		grid.addWidget(label_pin,GRID_X_POSITION_PIN,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_name,GRID_X_POSITION_NAME,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_father_last_name,GRID_X_POSITION_FNAME,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_mother_last_name,GRID_X_POSITION_MNAME,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_intro_hour,GRID_X_POSITION_IHOUR,GRID_Y_POSITION_LABEL_HOUR)
		grid.addWidget(label_exit_hour,GRID_X_POSITION_EHOUR,GRID_Y_POSITION_LABEL_HOUR)
		grid.addWidget(label_lunchtime,GRID_X_POSITION_LUNCH,GRID_Y_POSITION_LABEL_HOUR)

		grid.addWidget(self.text_pin,GRID_X_POSITION_PIN,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_name,GRID_X_POSITION_NAME,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_fname,GRID_X_POSITION_FNAME,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_mname,GRID_X_POSITION_MNAME,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_lunchtime,GRID_X_POSITION_LUNCH-2,GRID_Y_POSITION_HOUR_INSERT,GRID_X_POSITION_LUNCH-1,GRID_Y_POSITION_HOUR_INSERT+1)

		grid.addWidget(self.text_intro_hour,GRID_X_POSITION_IHOUR,GRID_Y_POSITION_HOUR_INSERT)
		grid.addWidget(self.text_intro_min,GRID_X_POSITION_IHOUR,GRID_Y_POSITION_MIN_INSERT)
		grid.addWidget(self.text_exit_hour,GRID_X_POSITION_EHOUR,GRID_Y_POSITION_HOUR_INSERT)
		grid.addWidget(self.text_exit_min,GRID_X_POSITION_EHOUR,GRID_Y_POSITION_MIN_INSERT)

		grid.addWidget(button_create,GRID_X_POSITION_CREATE_INSERT_WORK,GRID_Y_POSITION_CREATE_INSERT_WORK)
		grid.addWidget(button_back,GRID_X_POSITION_BACK_INSERT_WORK,GRID_Y_POSITION_BACK_INSERT_WORK)

		#LAYAOUT
		self.setLayout(grid)

	def create_worker(self):
		pin = self.text_pin.text()
		name = self.text_name.text()
		fname = self.text_fname.text()
		mname = self.text_mname.text()
		intro_hour = self.text_intro_hour.currentText()
		intro_min = self.text_intro_min.currentText()
		exit_hour = self.text_exit_hour.currentText()
		exit_min = self.text_exit_min.currentText()
		lt_minutes = self.text_lunchtime.text()
		if(pin == '' or name == '' or fname=='' or mname=='' or lt_minutes==''):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_EMPTY_CAMP, QMessageBox.Ok)
		elif(str_is_invalid(pin) or str_is_invalid(name) or str_is_invalid(fname) or str_is_invalid(mname) or str_is_invalid(lt_minutes)):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_INVALID_CAMP, QMessageBox.Ok)
		elif(is_number(pin)==False):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_INVALID_PIN, QMessageBox.Ok)
		elif(len(pin)>PIN_LEN):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_INVALID_LEN, QMessageBox.Ok)
		elif(is_number(lt_minutes)==False):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_INVALID_LT_MINUTES, QMessageBox.Ok)
		else:
			reply=QMessageBox.question(self, 'Message',CREATE_WORKER_QUESTION,QMessageBox.Yes,QMessageBox.No)
			if reply == QMessageBox.Yes:
				db=get_connection()
				if(db):
					pin=str(pin).zfill(PIN_LEN)
					if(controller_trabajador.pin_exist(pin,db)):
						QMessageBox.warning(self, 'Error',CREATE_WORKER_ALREADY_HAS_BEEN_USED, QMessageBox.Ok)
					else:
						new_lunchtime = lunchtime.Lunchtime([0,pin,FIRST_DATE,int(lt_minutes)])
						new_lunchtime.insert(db.cursor())
						new_horario = horario.Horario([0,pin,FIRST_DATE,time_to_str(intro_hour,intro_min),time_to_str(exit_hour,exit_min)])
						new_horario.insert(db.cursor())
						new_worker = trabajador.Trabajador([pin,name,fname,mname,True,new_horario.id,new_lunchtime.id])
						new_worker.insert(db.cursor())
						db.commit()
						db.close()
						QMessageBox.question(self, 'Message',CREATE_WORKER_SUCCESS,QMessageBox.Ok)
						self.close()
