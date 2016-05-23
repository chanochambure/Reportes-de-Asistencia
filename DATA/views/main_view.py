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

class main_view(QWidget):
	def __init__(self):
		super(main_view, self).__init__()
		self.main_view_create()
		screenGeometry = QApplication.desktop().availableGeometry()
		self.resize(screenGeometry.width()/3,screenGeometry.height()-100)
		self.setWindowTitle(MAIN_TITLE)
		self.show()

	def main_view_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(MAIN_VIEW_TITLE)
		button_insert_worker = QPushButton(BUTTON_INSERT_WORKER,self)
		button_insert_marks = QPushButton(BUTTON_MARKS,self)
		button_insert_marks_from_file = QPushButton(BUTTON_MARKS_FROM_FILE,self)
		button_modify_worker = QPushButton(BUTTON_MODIFY_WORKER,self)
		button_exit = QPushButton(BUTTON_EXIT,self)

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		button_insert_worker.setFixedSize(BUTTON_SIZE_MAIN_VIEW,button_insert_worker.height())
		button_insert_marks.setFixedSize(BUTTON_SIZE_MAIN_VIEW,button_insert_marks.height())
		button_insert_marks_from_file.setFixedSize(BUTTON_SIZE_MAIN_VIEW,button_insert_marks_from_file.height())
		button_modify_worker.setFixedSize(BUTTON_SIZE_MAIN_VIEW,button_modify_worker.height())
		button_exit.setFixedSize(BUTTON_SIZE_MAIN_VIEW,button_exit.height())

		#FUNCTION
		self.connect(button_insert_worker, SIGNAL("clicked()"),self.insert_worker)
		self.connect(button_insert_marks, SIGNAL("clicked()"),self.insert_marks)
		self.connect(button_insert_marks_from_file, SIGNAL("clicked()"),self.insert_marks_from_file)
		self.connect(button_modify_worker, SIGNAL("clicked()"),self.modify_worker)
		self.connect(button_exit, SIGNAL("clicked()"),self.close)

		#GRID SIZE
		grid.setHorizontalSpacing(GRID_X_MAIN_WINDOW)
		grid.setVerticalSpacing(GRID_Y_MAIN_WINDOW)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_TITLE,GRID_Y_POSITION_BUTTON)
		grid.addWidget(button_insert_worker,GRID_X_POSITION_INSERT_WORKER,GRID_Y_POSITION_BUTTON)
		grid.addWidget(button_insert_marks,GRID_X_POSITION_INSERT_MARKS,GRID_Y_POSITION_BUTTON)
		grid.addWidget(button_insert_marks_from_file,GRID_X_POSITION_INSERT_MARKS_FROM_FILE,GRID_Y_POSITION_BUTTON)
		grid.addWidget(button_modify_worker,GRID_X_POSITION_MODIFY_WORKER,GRID_Y_POSITION_BUTTON)
		grid.addWidget(button_exit,GRID_X_POSITION_EXIT,GRID_Y_POSITION_BUTTON)

		#LAYAOUT
		self.setLayout(grid)

	def insert_worker(self):
		print "insert_worker"
	def modify_worker(self):
		print "modify_worker"
	def insert_marks(self):
		print "marks"
	def insert_marks_from_file(self):
		print "marks_from_file"