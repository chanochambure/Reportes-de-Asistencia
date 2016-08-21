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
from models import horario
from controller import controller_horario

class horario_reporte_view(QDialog):
	def __init__(self,worker_to_set,parent=None):
		self.modify_mark_singleton=False
		self.ventana=None
		super(horario_reporte_view, self).__init__(parent)
		self.worker=worker_to_set
		#crear la ventana
		self.horario_reporte_create()
		#Dando tamaño a la pantalla
		screenGeometry = QApplication.desktop().availableGeometry()
		self.resize(screenGeometry.width()/2,screenGeometry.height()/2)
		self.setWindowTitle(REPORTES_HORARIO_TITLE)
		self.show()

	def horario_reporte_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(REPORTES_HORARIO_TITLE)
		button_back = QPushButton(BUTTON_BACK,self)
		self.insert = QTableWidget()

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		button_back.setFixedSize(BUTTON_SIZE_REPORTE_LUNCHTIME_VIEW_X,BUTTON_SIZE_REPORTE_LUNCHTIME_VIEW_Y)
		self.insert.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.insert.setRowCount(0);
		self.insert.setColumnCount(SIZE_COLUMNS_TABLE_HORARIO)
		self.insert.setHorizontalHeaderLabels(LISTA_TABLE_HORARIO)
		header = self.insert.horizontalHeader()
		header.setResizeMode(QHeaderView.Stretch)
		db=get_connection()
		lista=controller_horario.get_horarios(self.worker.pin,db)
		if(db and len(lista)):
			self.rows = len(lista)
			self.insert.setRowCount(self.rows)
			stringVert = []
			for index_hor in range(len(lista)):
				self.insert.setItem(index_hor,0, QTableWidgetItem(lista[index_hor].fechavalido))
				self.insert.setItem(index_hor,1, QTableWidgetItem(str(lista[index_hor].entrada)))
				self.insert.setItem(index_hor,2, QTableWidgetItem(str(lista[index_hor].salida)))
				stringVert.append(str(index_hor+1))
			stringVert.reverse()
			self.insert.setVerticalHeaderLabels(stringVert)
		db.close()

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)

		#GRID SIZE
		grid.setHorizontalSpacing(REPORTE_LUNCHTIME_X_GRID)
		grid.setVerticalSpacing(REPORTE_LUNCHTIME_Y_GRID)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_REPORTE_LUNCHTIME_TITLE,GRID_Y_POSITION_REPORTE_LUNCHTIME_TITLE)
		grid.addWidget(button_back,GRID_X_POSITION_BACK_REPORTE_LUNCHTIME,GRID_Y_POSITION_BACK_REPORTE_LUNCHTIME)
		grid.addWidget(self.insert,GRID_X_POSITION_REPORTE_LUNCHTIME_TABLE_1,GRID_Y_POSITION_REPORTE_LUNCHTIME_TABLE_1,
						GRID_X_POSITION_REPORTE_LUNCHTIME_TABLE_2,GRID_Y_POSITION_REPORTE_LUNCHTIME_TABLE_2)

		#LAYAOUT
		self.setLayout(grid)