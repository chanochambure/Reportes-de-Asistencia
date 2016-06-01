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
from models import lunchtime
from controller import controller_lunchtime

class lunchtime_reporte_view(QDialog):
	def __init__(self,worker_to_set,parent=None):
		self.modify_mark_singleton=False
		self.ventana=None
		super(lunchtime_reporte_view, self).__init__(parent)
		self.worker=worker_to_set
		#crear la ventana
		self.lunchtime_reporte_create()
		#Dando tamaño a la pantalla
		screenGeometry = QApplication.desktop().availableGeometry()
		self.resize(screenGeometry.width()/2,screenGeometry.height()/2)
		self.setWindowTitle(REPORTES_LUNCHTIME_TITLE)
		self.show()

	def lunchtime_reporte_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(REPORTES_LUNCHTIME_TITLE)
		button_back = QPushButton(BUTTON_BACK,self)
		self.lunchtime_table = QTableWidget()

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		button_back.setFixedSize(BUTTON_SIZE_REPORTE_LUNCHTIME_VIEW_X,BUTTON_SIZE_REPORTE_LUNCHTIME_VIEW_Y)
		self.lunchtime_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.lunchtime_table.setRowCount(0);
		self.lunchtime_table.setColumnCount(SIZE_COLUMNS_TABLE_LUNCHTIME)
		self.lunchtime_table.setHorizontalHeaderLabels(LISTA_TABLE_LUNCHTIME)
		header = self.lunchtime_table.horizontalHeader()
		header.setResizeMode(QHeaderView.Stretch)
		db=get_connection()
		list_lunchtime=controller_lunchtime.get_lunchtimes(self.worker.pin,db)
		if(db and len(list_lunchtime)):
			self.rows = len(list_lunchtime)
			self.lunchtime_table.setRowCount(self.rows)
			stringVert = []
			for index_lunch in range(len(list_lunchtime)):
				self.lunchtime_table.setItem(index_lunch,0, QTableWidgetItem(list_lunchtime[index_lunch].fechavalido))
				self.lunchtime_table.setItem(index_lunch,1, QTableWidgetItem(str(list_lunchtime[index_lunch].minutos)))
				stringVert.append(str(index_lunch+1))
			stringVert.reverse()
			self.lunchtime_table.setVerticalHeaderLabels(stringVert)
		db.close()

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)

		#GRID SIZE
		grid.setHorizontalSpacing(REPORTE_LUNCHTIME_X_GRID)
		grid.setVerticalSpacing(REPORTE_LUNCHTIME_Y_GRID)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_REPORTE_LUNCHTIME_TITLE,GRID_Y_POSITION_REPORTE_LUNCHTIME_TITLE)
		grid.addWidget(button_back,GRID_X_POSITION_BACK_REPORTE_LUNCHTIME,GRID_Y_POSITION_BACK_REPORTE_LUNCHTIME)
		grid.addWidget(self.lunchtime_table,GRID_X_POSITION_REPORTE_LUNCHTIME_TABLE_1,GRID_Y_POSITION_REPORTE_LUNCHTIME_TABLE_1,
						GRID_X_POSITION_REPORTE_LUNCHTIME_TABLE_2,GRID_Y_POSITION_REPORTE_LUNCHTIME_TABLE_2)

		#LAYAOUT
		self.setLayout(grid)