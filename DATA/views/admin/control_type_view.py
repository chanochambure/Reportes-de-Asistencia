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
from models import relation_trabajador_tipo
from views.admin import insert_type_view
from views import search_worker_view
from controller import controller_area,controller_tipo,controller_relation_tipo,controller_trabajador

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
		self.setWindowTitle(ADMIN_CONTROL_TYPE_TITLE)
		self.show()

	def control_type_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(ADMIN_CONTROL_TYPE_TITLE+": "+self.type_m.name)
		label_relation_text = QLabel(ADMIN_CONTROL_AREA_RELATION_TEXT)

		button_back = QPushButton(BUTTON_BACK,self)
		button_insert_relation = QPushButton(ADMIN_CONTROL_AREA_INSERT_RELATION,self)

		self.table = QTableWidget()
		self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.stringRow = ''
		self.table.setColumnCount(SIZE_COLUMNS_TABLE_WORK_TYPE)
		self.table.setHorizontalHeaderLabels(CONTROL_TYPE_LIST_HEADER_TABLE)
		self.table.setRowCount(0)
		header = self.table.horizontalHeader()
		header.setResizeMode(QHeaderView.Stretch)
		self.table.setVerticalHeaderLabels(QString(self.stringRow).split(";"))
		self.reinsert_table()

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		label_relation_text.setFont(font_title)

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)
		self.connect(button_insert_relation, SIGNAL("clicked()"),self.insert_relation)

		#GRID SIZE
		grid.setHorizontalSpacing(CONTROL_TYPE_X_GRID)
		grid.setVerticalSpacing(CONTROL_TYPE_Y_GRID)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_TITLE_CONTROL_TYPE,GRID_Y_POSITION_TITLE_CONTROL_TYPE)
		grid.addWidget(label_relation_text,GRID_X_POSITION_RELATION_CONTROL_TYPE,GRID_Y_POSITION_RELATION_CONTROL_TYPE)
		grid.addWidget(button_back,GRID_X_POSITION_BUTTON_BACK_C_TYPE,GRID_Y_POSITION_BUTTON_BACK_C_TYPE)
		grid.addWidget(button_insert_relation,GRID_X_POSITION_BUTTON_INS_R_C_TYPE,GRID_Y_POSITION_BUTTON_INS_R_C_TYPE)
		grid.addWidget(self.table,GRID_X_POSITION_TABLE_C_TYPE,GRID_Y_POSITION_TABLE_C_TYPE,
						GRID_X_SIZE_TABLE_C_TYPE,GRID_Y_SIZE_TABLE_C_TYPE)

		#LAYAOUT
		self.setLayout(grid)

	def insert_relation(self):
		if(self.type_singleton):
			QMessageBox.warning(self, 'Error',ERROR_A_PROCESS_OPENED, QMessageBox.Ok)
		else:
			self.type_singleton=True
			self.ventana = search_worker_view.search_worker_view(SEARCH_WORKER_SELECTION_MESSAGE,False)
			self.ventana.exec_()
			if(self.ventana.selected):
				worker = self.ventana.selected
				worker_name= worker.name+" "+worker.father_last_name+" "+worker.mother_last_name
				reply=QMessageBox.question(self, 'Message',INSERT_RELATION_QUESTION_1+worker_name+INSERT_RELATION_QUESTION_2+self.type_m.name,QMessageBox.Yes,QMessageBox.No)
				if reply == QMessageBox.Yes:
					db=get_connection()
					if(db):
						if(controller_relation_tipo.relation_exist(db,self.type_m.id,worker.pin)):
							db.close()
							QMessageBox.question(self, 'Error',INSERT_RELATION_ERROR,QMessageBox.Ok)
						else:
							new_relation=relation_trabajador_tipo.RelacionTrabajadorTipo([self.type_m.id,worker.pin])
							new_relation.insert(db.cursor())
							db.commit()
							db.close()
							self.reinsert_table()
							QMessageBox.question(self, 'Message',INSERT_RELATION_SUCCESS,QMessageBox.Ok)
			self.ventana=None
			self.type_singleton=False

	def reinsert_table(self):
		self.clear_table()
		if(len(self.relation_list)):
			self.rows = len(self.relation_list)
			self.table.setRowCount(self.rows)
			stringVert = []
			db=get_connection()
			if(db):
				for index in range(len(self.relation_list)):
					worker=controller_trabajador.get_worker(self.relation_list[index].pin,db,False)
					self.table.setItem(index,0, QTableWidgetItem(worker.name))
					self.table.setItem(index,1, QTableWidgetItem(worker.father_last_name))
					self.table.setItem(index,2, QTableWidgetItem(worker.mother_last_name))
					self.btn_sell = QPushButton(CONTROL_TYPE_REMOVE_RELATION)
					self.btn_sell.clicked.connect(self.remove_worker)
					self.table.setCellWidget(index,3,self.btn_sell)
					stringVert.append(str(index+1))
				self.table.setVerticalHeaderLabels(stringVert)
			db.close()

	def clear_table(self):
		db=get_connection()
		if(db):
			self.relation_list=controller_relation_tipo.get_relations_tipos(db,self.type_m.id)
			db.close()
		self.table.clear();
		self.table.setRowCount(0);
		self.table.setColumnCount(SIZE_COLUMNS_TABLE_WORK_TYPE)
		self.table.setHorizontalHeaderLabels(CONTROL_TYPE_LIST_HEADER_TABLE)

	def remove_worker(self):
		if(self.type_singleton):
			QMessageBox.warning(self, 'Error',ERROR_A_PROCESS_OPENED, QMessageBox.Ok)
		else:
			self.type_singleton=True
			reply=QMessageBox.question(self, 'Message',REMOVE_WORKER_QUESTION,QMessageBox.Yes,QMessageBox.No)
			if reply == QMessageBox.Yes:
				db=get_connection()
				if(db):
					index = self.table.indexAt(qApp.focusWidget().pos())
					if index.isValid():
						if(self.relation_list[index.row()].remove(db.cursor())):
							db.commit()
							db.close()
							self.reinsert_table()
							QMessageBox.question(self, 'Message',REMOVE_WORKER_SUCEESS,QMessageBox.Ok)
						else:
							db.close()
			self.type_singleton=False

	def closeEvent(self, evnt):
		if(self.ventana):
			self.ventana.close()
