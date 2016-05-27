#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from datetime import datetime

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from constants import *
from models import trabajador
from controller import controller_trabajador

class search_worker_view(QDialog):
	def __init__(self,message,mode_to_s,parent=None):
		self.selected = None
		self.mode = mode_to_s
		self.message = message
		super(search_worker_view, self).__init__(parent)
		self.search_worker_create()
		screenGeometry = QApplication.desktop().availableGeometry()
		self.resize(2*screenGeometry.width()/5,4*screenGeometry.height()/5)
		self.setWindowTitle(SEARCH_WORKER_TITLE)
		self.show()

	def search_worker_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(SEARCH_WORKER_VIEW_TITLE)
		label_name = QLabel(ADMIN_INSERT_WORKER_NAME)
		label_father_last_name = QLabel(ADMIN_INSERT_WORKER_FNAME)
		label_mother_last_name = QLabel(ADMIN_INSERT_WORKER_MNAME)
		self.text_name = QLineEdit()
		self.text_fname = QLineEdit()
		self.text_mname = QLineEdit()
		button_search = QPushButton(BUTTON_SEARCH_WORKER,self)
		button_back = QPushButton(BUTTON_BACK,self)
		self.workers_table = QTableWidget()

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		button_search.setFixedSize(BUTTON_SIZE_SEARCH_WORKER_VIEW_X,BUTTON_SIZE_SEARCH_WORKER_VIEW_Y)
		button_back.setFixedSize(BUTTON_SIZE_SEARCH_WORKER_VIEW_X,BUTTON_SIZE_SEARCH_WORKER_VIEW_Y)
		self.workers_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.rows = 0
		self.stringRow = ''
		self.workers_table.setColumnCount(SIZE_COLUMNS_TABLE_WORKERS)
		self.workers_table.setHorizontalHeaderLabels(QString(SEARCH_TITLE_ROWS).split(SPLIT_TABLE_WORKERS))
		self.workers_table.setRowCount(self.rows)
		header = self.workers_table.horizontalHeader()
		header.setResizeMode(QHeaderView.Stretch)
		self.workers_table.setVerticalHeaderLabels(QString(self.stringRow).split(";"))

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)
		self.connect(button_search, SIGNAL("clicked()"),self.search_worker_function)

		#GRID SIZE
		grid.setHorizontalSpacing(SEARCH_WORKER_X_GRID)
		grid.setVerticalSpacing(SEARCH_WORKER_Y_GRID)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_SEARCH_WORK_TITLE,GRID_Y_POSITION_SEARCH_WORK_TITLE)
		grid.addWidget(label_name,GRID_X_POSITION_NAME_SEARCH,GRID_Y_POSITION_LABEL_SEARCH)
		grid.addWidget(label_father_last_name,GRID_X_POSITION_FNAME_SEARCH,GRID_Y_POSITION_LABEL_SEARCH)
		grid.addWidget(label_mother_last_name,GRID_X_POSITION_MNAME_SEARCH,GRID_Y_POSITION_LABEL_SEARCH)
		grid.addWidget(self.text_name,GRID_X_POSITION_NAME_SEARCH,GRID_Y_POSITION_TEXT_SEARCH)
		grid.addWidget(self.text_fname,GRID_X_POSITION_FNAME_SEARCH,GRID_Y_POSITION_TEXT_SEARCH)
		grid.addWidget(self.text_mname,GRID_X_POSITION_MNAME_SEARCH,GRID_Y_POSITION_TEXT_SEARCH)
		grid.addWidget(button_search,GRID_X_POSITION_CREATE_SEARCH_WORK,GRID_Y_POSITION_CREATE_SEARCH_WORK)
		grid.addWidget(button_back,GRID_X_POSITION_BACK_SEARCH_WORK,GRID_Y_POSITION_BACK_SEARCH_WORK)
		grid.addWidget(self.workers_table,GRID_X_POSITION_SEARCH_WORK_TABLE_1,GRID_Y_POSITION_SEARCH_WORK_TABLE_1,
						GRID_X_POSITION_SEARCH_WORK_TABLE_2,GRID_Y_POSITION_SEARCH_WORK_TABLE_2)

		#LAYAOUT
		self.setLayout(grid)

	def search_worker_function(self):
		self.selected = None
		name = self.text_name.text()
		fname = self.text_fname.text()
		mname = self.text_mname.text()
		if(str_is_invalid(name) or str_is_invalid(fname) or str_is_invalid(mname)):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_INVALID_CAMP, QMessageBox.Ok)
		else:
			db=get_connection()
			if(db):
				self.list_workers=controller_trabajador.get_workers(name,fname,mname,db,self.mode)
				self.insert_workers_table()

	def insert_workers_table(self):
		self.clear_workers_table()
		if(len(self.list_workers)):
			self.rows = len(self.list_workers)
			self.workers_table.setRowCount(self.rows)
			stringVert = []
			for index_worker in range(len(self.list_workers)):
				#De esa forma actualizaremos
				self.workers_table.setItem(index_worker,0, QTableWidgetItem(self.list_workers[index_worker].name))
				self.workers_table.setItem(index_worker,1, QTableWidgetItem(self.list_workers[index_worker].father_last_name))
				self.workers_table.setItem(index_worker,2, QTableWidgetItem(self.list_workers[index_worker].mother_last_name))
				self.btn_sell = QPushButton(self.message)
				self.btn_sell.clicked.connect(self.selection)
				self.workers_table.setCellWidget(index_worker,3,self.btn_sell)
				stringVert.append(str(index_worker+1))
			self.workers_table.setVerticalHeaderLabels(stringVert)

	def clear_workers_table(self):
		self.workers_table.clear();
		self.workers_table.setRowCount(0);
		self.workers_table.setColumnCount(SIZE_COLUMNS_TABLE_WORKERS)
		self.workers_table.setHorizontalHeaderLabels(QString(SEARCH_TITLE_ROWS).split(SPLIT_TABLE_WORKERS))

	def selection(self):
		index = self.workers_table.indexAt(qApp.focusWidget().pos())
		if index.isValid():
			self.selected=self.list_workers[index.row()]
			self.close()