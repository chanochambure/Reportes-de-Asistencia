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
	def __init__(self,worker_to_mod,parent=None):
		super(modify_worker_view, self).__init__(parent)
		self.worker = worker_to_mod
		self.modify_worker_create()
		self.setWindowTitle(ADMIN_MODIFY_WORKER_TITLE)
		self.show()

	def modify_worker_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(ADMIN_MODIFY_WORKER_TITLE)
		label_pin = QLabel(ADMIN_INSERT_WORKER_PIN)
		label_name = QLabel(ADMIN_INSERT_WORKER_NAME)
		label_father_last_name = QLabel(ADMIN_INSERT_WORKER_FNAME)
		label_mother_last_name = QLabel(ADMIN_INSERT_WORKER_MNAME)
		label_active = QLabel(ADMIN_MOD_WORKER_ACTIVE)
		self.text_pin = QLineEdit()
		self.text_name = QLineEdit()
		self.text_fname = QLineEdit()
		self.text_mname = QLineEdit()
		self.text_active = QRadioButton()
		button_mod = QPushButton(BUTTON_MOD_WORKER,self)
		button_back = QPushButton(BUTTON_BACK,self)

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		button_mod.setFixedSize(BUTTON_SIZE_MOD_WORKER_VIEW_X,BUTTON_SIZE_MOD_WORKER_VIEW_Y)
		button_back.setFixedSize(BUTTON_SIZE_MOD_WORKER_VIEW_X,BUTTON_SIZE_MOD_WORKER_VIEW_Y)
		self.text_pin.setText(self.worker.pin)
		self.text_pin.setDisabled(True)
		self.text_name.setText(self.worker.name)
		self.text_fname.setText(self.worker.father_last_name)
		self.text_mname.setText(self.worker.mother_last_name)
		self.text_active.setChecked(bool(self.worker.activo))

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)
		self.connect(button_mod, SIGNAL("clicked()"),self.modify_worker_function)

		#GRID SIZE
		grid.setHorizontalSpacing(ADMIN_MOD_WORKER_X)
		grid.setVerticalSpacing(ADMIN_MOD_WORKER_Y)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_INSERT_WORK_TITLE,GRID_Y_POSITION_INSERT_WORK_TITLE)
		grid.addWidget(label_pin,GRID_X_POSITION_PIN,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_name,GRID_X_POSITION_NAME,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_father_last_name,GRID_X_POSITION_FNAME,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_mother_last_name,GRID_X_POSITION_MNAME,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_active,GRID_X_POSITION_ACTIVE,GRID_Y_POSITION_LABEL)
		grid.addWidget(self.text_pin,GRID_X_POSITION_PIN,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_name,GRID_X_POSITION_NAME,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_fname,GRID_X_POSITION_FNAME,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_mname,GRID_X_POSITION_MNAME,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_active,GRID_X_POSITION_ACTIVE,GRID_Y_POSITION_TEXT)
		grid.addWidget(button_mod,GRID_X_POSITION_CREATE_MOD_WORK,GRID_Y_POSITION_CREATE_MOD_WORK)
		grid.addWidget(button_back,GRID_X_POSITION_BACK_MOD_WORK,GRID_Y_POSITION_BACK_MOD_WORK)

		#LAYAOUT
		self.setLayout(grid)

	def modify_worker_function(self):
		name = self.text_name.text()
		fname = self.text_fname.text()
		mname = self.text_mname.text()
		activo = self.text_active.isChecked()
		if(name == '' or fname=='' or mname==''):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_EMPTY_CAMP, QMessageBox.Ok)
		elif(str_is_invalid(name) or str_is_invalid(fname) or str_is_invalid(mname)):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_INVALID_CAMP, QMessageBox.Ok)
		elif(name == self.worker.name and fname == self.worker.father_last_name and mname == self.worker.mother_last_name and activo == self.worker.activo):
			QMessageBox.warning(self, 'Error',MOD_WORKER_NO_CHANGES, QMessageBox.Ok)
		else:
			reply=QMessageBox.question(self, 'Message',MOD_WORKER_QUESTION,QMessageBox.Yes,QMessageBox.No)
			if reply == QMessageBox.Yes:
				db=get_connection()
				if(db):
					self.worker.name = name
					self.worker.father_last_name = fname
					self.worker.mother_last_name = mname
					self.worker.activo = activo
					if(self.worker.update(db.cursor())):
						db.commit()
						db.close()
						QMessageBox.question(self, 'Message',MOD_WORKER_SUCCESS,QMessageBox.Ok)
						self.close()
