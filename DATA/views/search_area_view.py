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
from models import area
from controller import controller_area

class search_area_view(QDialog):
	def __init__(self,message,parent=None):
		self.selected = None
		self.message = message
		super(search_area_view, self).__init__(parent)
		self.search_area_create()
		screenGeometry = QApplication.desktop().availableGeometry()
		self.resize(2*screenGeometry.width()/5,4*screenGeometry.height()/5)
		self.setWindowTitle(SEARCH_AREA_TITLE)
		self.show()

	def search_area_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(SEARCH_AREA_VIEW_TITLE)
		label_name = QLabel(ADMIN_INSERT_WORKER_NAME)
		self.text_name = QLineEdit()
		button_search = QPushButton(BUTTON_SEARCH_AREA,self)
		button_back = QPushButton(BUTTON_BACK,self)
		self.area_Table = QTableWidget()

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		button_search.setFixedSize(BUTTON_SIZE_SEARCH_AREA_VIEW_X,BUTTON_SIZE_SEARCH_AREA_VIEW_Y)
		button_back.setFixedSize(BUTTON_SIZE_SEARCH_AREA_VIEW_X,BUTTON_SIZE_SEARCH_AREA_VIEW_Y)
		self.area_Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.rows = 0
		self.stringRow = ''
		self.area_Table.setColumnCount(SIZE_COLUMNS_TABLE_AREA)
		self.area_Table.setHorizontalHeaderLabels(SEARCH_TITLE_AREA_ROWS)
		self.area_Table.setRowCount(self.rows)
		header = self.area_Table.horizontalHeader()
		header.setResizeMode(QHeaderView.Stretch)
		self.area_Table.setVerticalHeaderLabels(QString(self.stringRow).split(";"))

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)
		self.connect(button_search, SIGNAL("clicked()"),self.search_area_function)

		#GRID SIZE
		grid.setHorizontalSpacing(SEARCH_AREA_X_GRID)
		grid.setVerticalSpacing(SEARCH_AREA_Y_GRID)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_SEARCH_AREA_TITLE,GRID_Y_POSITION_SEARCH_AREA_TITLE)
		grid.addWidget(label_name,GRID_X_POSITION_NAME_SEARCH,GRID_Y_POSITION_LABEL_SEARCH)
		grid.addWidget(self.text_name,GRID_X_POSITION_NAME_SEARCH,GRID_Y_POSITION_TEXT_SEARCH)
		grid.addWidget(button_search,GRID_X_POSITION_CREATE_SEARCH_WORK,GRID_Y_POSITION_CREATE_SEARCH_WORK)
		grid.addWidget(button_back,GRID_X_POSITION_BACK_SEARCH_WORK,GRID_Y_POSITION_BACK_SEARCH_WORK)
		grid.addWidget(self.area_Table,GRID_X_POSITION_SEARCH_WORK_TABLE_1,GRID_Y_POSITION_SEARCH_WORK_TABLE_1,
						GRID_X_POSITION_SEARCH_WORK_TABLE_2,GRID_Y_POSITION_SEARCH_WORK_TABLE_2)

		#LAYAOUT
		self.setLayout(grid)

	def search_area_function(self):
		self.selected = None
		name = self.text_name.text()
		if(str_is_invalid(name)):
			QMessageBox.warning(self, 'Error',CREATE_AREA_INVALID_CAMP, QMessageBox.Ok)
		else:
			db=get_connection()
			if(db):
				self.list_areas=controller_area.get_areas(db,name)
				self.insert_areas_table()

	def insert_areas_table(self):
		self.clear_areas_table()
		if(len(self.list_areas)):
			self.rows = len(self.list_areas)
			self.area_Table.setRowCount(self.rows)
			stringVert = []
			for index_area in range(len(self.list_areas)):
				#De esa forma actualizaremos
				self.area_Table.setItem(index_area,0,QTableWidgetItem(self.list_areas[index_area].name))
				self.btn_sell = QPushButton(self.message)
				self.btn_sell.clicked.connect(self.selection)
				self.area_Table.setCellWidget(index_area,1,self.btn_sell)
				stringVert.append(str(index_area+1))
			self.area_Table.setVerticalHeaderLabels(stringVert)

	def clear_areas_table(self):
		self.area_Table.clear();
		self.area_Table.setRowCount(0);
		self.area_Table.setColumnCount(SIZE_COLUMNS_TABLE_AREA)
		self.area_Table.setHorizontalHeaderLabels(SEARCH_TITLE_AREA_ROWS)

	def selection(self):
		index = self.area_Table.indexAt(qApp.focusWidget().pos())
		if index.isValid():
			self.selected=self.list_areas[index.row()]
			self.close()