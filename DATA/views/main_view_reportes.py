#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#Import de Modulos
BASE_DIR='../'
sys.path.insert(0,BASE_DIR)
from constants import *
from views.reportes import lunchtime_reporte_view,tardanza_reporte_view,horas_reporte_view
from views import search_worker_view

class main_view_reportes(QWidget):
	def __init__(self):
		self.ventana_rh=None
		self.ventana_rt=None
		self.ventana_rl=None
		super(main_view_reportes, self).__init__()
		self.main_view_create()
		screenGeometry = QApplication.desktop().availableGeometry()
		self.resize(screenGeometry.width()/4,screenGeometry.height()/2)
		self.setWindowTitle(MAIN_TITLE)
		self.show()
		self.singleton_widget_rh=False
		self.singleton_widget_rt=False
		self.singleton_widget_rl=False

	def main_view_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(MAIN_VIEW_TITLE_REPORTES)
		button_reporte_horas = QPushButton(BUTTON_REPORTES_HORAS,self)
		button_reporte_tardanzas = QPushButton(BUTTON_REPORTES_TARDANZAS,self)
		button_reporte_lunchtime = QPushButton(BUTTON_REPORTES_LUCHTIME,self)
		button_exit = QPushButton(BUTTON_EXIT,self)

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		button_exit.setFixedSize(BUTTON_SIZE_MAIN_VIEW,button_exit.height())
		button_reporte_lunchtime.setFixedSize(BUTTON_SIZE_MAIN_VIEW,button_reporte_lunchtime.height())
		button_reporte_tardanzas.setFixedSize(BUTTON_SIZE_MAIN_VIEW,button_reporte_tardanzas.height())
		button_reporte_horas.setFixedSize(BUTTON_SIZE_MAIN_VIEW,button_reporte_horas.height())

		#FUNCTION
		self.connect(button_exit, SIGNAL("clicked()"),self.close)
		self.connect(button_reporte_lunchtime, SIGNAL("clicked()"),self.reporte_lunchtime)
		self.connect(button_reporte_tardanzas, SIGNAL("clicked()"),self.reporte_tardanzas)
		self.connect(button_reporte_horas, SIGNAL("clicked()"),self.reporte_horas)

		#GRID SIZE
		grid.setHorizontalSpacing(GRID_X_MAIN_WINDOW_REPORTES)
		grid.setVerticalSpacing(GRID_Y_MAIN_WINDOW_REPORTES)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_TITLE_R,GRID_Y_POSITION_BUTTON_R)
		grid.addWidget(button_exit,GRID_X_POSITION_EXIT_R,GRID_Y_POSITION_BUTTON_R)
		grid.addWidget(button_reporte_lunchtime,GRID_X_POSITION_REPORTE_LUNCHTIME_R,GRID_Y_POSITION_BUTTON)
		grid.addWidget(button_reporte_tardanzas,GRID_X_POSITION_REPORTE_TARDANZA_R,GRID_Y_POSITION_BUTTON)
		grid.addWidget(button_reporte_horas,GRID_X_POSITION_REPORTE_HORAS_R,GRID_Y_POSITION_BUTTON)

		#LAYAOUT
		self.setLayout(grid)

	def reporte_horas(self):
		if(self.singleton_widget_rh):
			QMessageBox.warning(self, 'Error',ERROR_A_PROCESS_OPENED, QMessageBox.Ok)
		else:
			self.singleton_widget_rh=True
			self.ventana_rh = search_worker_view.search_worker_view(SEARCH_SEE_REPORTES_HORAS_MESSAGE,True)
			self.ventana_rh.exec_()
			if(self.ventana_rh.selected):
				worker = self.ventana_rh.selected
				self.ventana_rh = horas_reporte_view.horas_reporte_view(worker)
				self.ventana_rh.exec_()
			self.ventana_rh=None
			self.singleton_widget_rh=False

	def reporte_tardanzas(self):
		if(self.singleton_widget_rt):
			QMessageBox.warning(self, 'Error',ERROR_A_PROCESS_OPENED, QMessageBox.Ok)
		else:
			self.singleton_widget_rt=True
			self.ventana_rt = search_worker_view.search_worker_view(SEARCH_SEE_REPORTES_TARDANZA_MESSAGE,True)
			self.ventana_rt.exec_()
			if(self.ventana_rt.selected):
				worker = self.ventana_rt.selected
				self.ventana_rt = tardanza_reporte_view.tardanza_reporte_view(worker)
				self.ventana_rt.exec_()
			self.ventana_rt=None
			self.singleton_widget_rt=False

	def reporte_lunchtime(self):
		if(self.singleton_widget_rl):
			QMessageBox.warning(self, 'Error',ERROR_A_PROCESS_OPENED, QMessageBox.Ok)
		else:
			self.singleton_widget_rl=True
			self.ventana_rl = search_worker_view.search_worker_view(SEARCH_SEE_REPORTES_LUNCHTIME_MESSAGE,False)
			self.ventana_rl.exec_()
			if(self.ventana_rl.selected):
				worker = self.ventana_rl.selected
				self.ventana_rl = lunchtime_reporte_view.lunchtime_reporte_view(worker)
				self.ventana_rl.exec_()
			self.ventana_rl=None
			self.singleton_widget_rl=False

	def closeEvent(self, evnt):
		if(self.ventana_rh):
			self.ventana_rh.close()
		if(self.ventana_rt):
			self.ventana_rt.close()
		if(self.ventana_rl):
			self.ventana_rl.close()
