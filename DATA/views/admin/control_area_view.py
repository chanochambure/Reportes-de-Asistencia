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
from views.admin import insert_type_view,control_type_view
from controller import controller_area,controller_tipo

class control_area_view(QDialog):
	def __init__(self,area_to_set,parent=None):
		self.type_singleton=False
		self.ventana=None
		super(control_area_view, self).__init__(parent)
		self.area=area_to_set
		self.type_list=[]
		db=get_connection()
		if(db):
			self.type_list=controller_tipo.get_tipos(db,self.area.id)
			db.close()
		#crear la ventana
		self.control_area_create()
		#Dando tamaño a la pantalla
		screenGeometry = QApplication.desktop().availableGeometry()
		self.resize(screenGeometry.width()/2,2*screenGeometry.height()/3)
		self.setWindowTitle(ADMIN_CONTROL_AREA_TITLE)
		self.show()

	def control_area_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(ADMIN_CONTROL_AREA_TITLE+": "+self.area.name)
		label_tipe_text = QLabel(ADMIN_CONTROL_AREA_TYPE_TEXT)

		button_back = QPushButton(BUTTON_BACK,self)
		button_remove = QPushButton(ADMIN_CONTROL_REMOVE_AREA,self)
		button_insert_type = QPushButton(ADMIN_CONTROL_AREA_INSERT_TYPE,self)

		self.table = QTableWidget()
		self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.stringRow = ''
		self.table.setColumnCount(SIZE_COLUMNS_TABLE_TYPES_AREA)
		self.table.setHorizontalHeaderLabels(CONTROL_AREA_LIST_HEADER_TABLE)
		self.table.setRowCount(0)
		header = self.table.horizontalHeader()
		header.setResizeMode(QHeaderView.Stretch)
		self.table.setVerticalHeaderLabels(QString(self.stringRow).split(";"))
		self.reinsert_table()

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)
		self.connect(button_remove, SIGNAL("clicked()"),self.remove_area)
		self.connect(button_insert_type, SIGNAL("clicked()"),self.insert_type)

		#GRID SIZE
		grid.setHorizontalSpacing(CONTROL_AREA_X_GRID)
		grid.setVerticalSpacing(CONTROL_AREA_Y_GRID)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_TITLE_CONTROL_AREA,GRID_Y_POSITION_TITLE_CONTROL_AREA)
		grid.addWidget(label_tipe_text,GRID_X_POSITION_TYPE_CONTROL_AREA,GRID_Y_POSITION_TYPE_CONTROL_AREA)
		grid.addWidget(button_back,GRID_X_POSITION_BUTTON_BACK_C_AREA,GRID_Y_POSITION_BUTTON_BACK_C_AREA)
		grid.addWidget(button_remove,GRID_X_POSITION_BUTTON_REMO_C_AREA,GRID_Y_POSITION_BUTTON_REMO_C_AREA)
		grid.addWidget(button_insert_type,GRID_X_POSITION_BUTTON_INS_T_C_AREA,GRID_Y_POSITION_BUTTON_INS_T_C_AREA)
		grid.addWidget(self.table,GRID_X_POSITION_TABLE_C_AREA,GRID_Y_POSITION_TABLE_C_AREA,
						GRID_X_SIZE_TABLE_C_AREA,GRID_Y_SIZE_TABLE_C_AREA)

		#LAYAOUT
		self.setLayout(grid)

	def insert_type(self):
		if(self.type_singleton):
			QMessageBox.warning(self, 'Error',ERROR_A_PROCESS_OPENED, QMessageBox.Ok)
		else:
			self.type_singleton=True
			self.ventana = insert_type_view.insert_type_view(self.area)
			self.ventana.exec_()
			db=get_connection()
			if(db):
				self.type_list=controller_tipo.get_tipos(db,self.area.id)
				db.close()
			self.reinsert_table()
			self.ventana=None
			self.type_singleton=False

	def reinsert_table(self):
		self.clear_table()
		if(len(self.type_list)):
			self.rows = len(self.type_list)
			self.table.setRowCount(self.rows)
			stringVert = []
			for index in range(len(self.type_list)):
				self.table.setItem(index,0, QTableWidgetItem(self.type_list[index].name))
				self.btn_sell = QPushButton(CONTROL_AREA_CONTROL_TYPE)
				self.btn_sell.clicked.connect(self.control_type)
				self.table.setCellWidget(index,1,self.btn_sell)
				self.btn_sell = QPushButton(CONTROL_AREA_REMOVE_TYPE)
				self.btn_sell.clicked.connect(self.remove_type)
				self.table.setCellWidget(index,2,self.btn_sell)
				stringVert.append(str(index+1))
			self.table.setVerticalHeaderLabels(stringVert)

	def remove_type(self):
		if(self.type_singleton):
			QMessageBox.warning(self, 'Error',ERROR_A_PROCESS_OPENED, QMessageBox.Ok)
		else:
			self.type_singleton=True
			reply=QMessageBox.question(self, 'Message',REMOVE_TYPE_QUESTION,QMessageBox.Yes,QMessageBox.No)
			if reply == QMessageBox.Yes:
				db=get_connection()
				if(db):
					index = self.table.indexAt(qApp.focusWidget().pos())
					if index.isValid():
						if(self.type_list[index.row()].remove(db.cursor())):
							db.commit()
							self.type_list=controller_tipo.get_tipos(db,self.area.id)
							db.close()
							self.reinsert_table()
							QMessageBox.question(self, 'Message',REMOVE_TYPE_SUCCESS,QMessageBox.Ok)
						else:
							db.close()
			self.type_singleton=False

	def control_type(self):
		if(self.type_singleton):
			QMessageBox.warning(self, 'Error',ERROR_A_PROCESS_OPENED, QMessageBox.Ok)
		else:
			self.type_singleton=True
			index = self.table.indexAt(qApp.focusWidget().pos())
			if index.isValid():
				self.ventana = control_type_view.control_type_view(self.type_list[index.row()])
				self.ventana.exec_()
				self.ventana=None
			self.type_singleton=False

	def clear_table(self):
		self.table.clear();
		self.table.setRowCount(0);
		self.table.setColumnCount(SIZE_COLUMNS_TABLE_TYPES_AREA)
		self.table.setHorizontalHeaderLabels(CONTROL_AREA_LIST_HEADER_TABLE)

	def remove_area(self):
		if(self.type_singleton):
			QMessageBox.warning(self, 'Error',ERROR_A_PROCESS_OPENED, QMessageBox.Ok)
		else:
			self.type_singleton=True
			reply=QMessageBox.question(self, 'Message',REMOVE_AREA_QUESTION,QMessageBox.Yes,QMessageBox.No)
			if reply == QMessageBox.Yes:
				db=get_connection()
				if(db):
					if(self.area.remove(db.cursor())):
						db.commit()
						db.close()
						QMessageBox.question(self, 'Message',REMOVE_AREA_SUCCESS,QMessageBox.Ok)
						self.close()
					else:
						db.close()
			self.type_singleton=False

	def closeEvent(self, evnt):
		if(self.ventana):
			self.ventana.close()
