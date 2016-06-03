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
from models import mark
from views import modify_mark_view
from views.admin import insert_marks_view
from controller import controller_mark

class control_single_mark_view(QDialog):
	def __init__(self,worker_to_set,date_to_set,parent=None):
		self.modify_mark_singleton=False
		self.ventana=None
		super(control_single_mark_view, self).__init__(parent)
		self.worker=worker_to_set
		self.date_d=date_to_set
		#crear la ventana
		self.control_marks_create()
		#Dando tamaño a la pantalla
		self.setWindowTitle(ADMIN_CONTROL_MARKS_TITLE)
		self.show()

	def control_marks_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(ADMIN_CONTROL_MARKS_TITLE)
		label_date1 = QLabel(ADMIN_CONTROL_MARKS_DATE1)
		label_valido = QLabel(ADMIN_CONTROL_MARKS_VALIDO)
		self.text_valido = QRadioButton()
		button_search = QPushButton(BUTTON_SEARCH_MARK,self)
		button_insert = QPushButton(BUTTON_INSERT_NEW_MARK,self)
		button_back = QPushButton(BUTTON_BACK,self)
		label_pin = QLabel(ADMIN_NAME_INSERT_MARK)
		self.text_name = QLineEdit()
		self.marks_table = QTableWidget()
		self.d_box1 = QComboBox()
		self.m_box1 = QComboBox()
		self.y_box1 = QComboBox()

		#Modificacion widgets
		self.text_valido.setChecked(True)
		self.text_name.setText(self.worker.pin+" - "+self.worker.name+" "+self.worker.father_last_name+" "+self.worker.mother_last_name)
		self.text_name.setDisabled(True)
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		button_search.setFixedSize(BUTTON_SIZE_SEARCH_MARKS_VIEW_X,BUTTON_SIZE_SEARCH_MARKS_VIEW_Y)
		button_insert.setFixedSize(BUTTON_SIZE_SEARCH_MARKS_VIEW_X,BUTTON_SIZE_SEARCH_MARKS_VIEW_Y)
		button_back.setFixedSize(BUTTON_SIZE_SEARCH_MARKS_VIEW_X,BUTTON_SIZE_SEARCH_MARKS_VIEW_Y)
		self.marks_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.rows = 0
		self.stringRow = ''
		self.marks_table.setColumnCount(SIZE_COLUMNS_TABLE_MARKS)
		self.marks_table.setHorizontalHeaderLabels(QString(SEARCH_MARKS_TITLE_ROWS).split(SPLIT_TABLE_MARKS))
		self.marks_table.setRowCount(self.rows)
		header = self.marks_table.horizontalHeader()
		header.setResizeMode(QHeaderView.Stretch)
		self.marks_table.setVerticalHeaderLabels(QString(self.stringRow).split(";"))
		self.create_combo_box()

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)
		self.connect(button_search, SIGNAL("clicked()"),self.search_marks_function)
		self.connect(button_insert, SIGNAL("clicked()"),self.new_marks_function)
		self.connect(self.y_box1, SIGNAL("currentIndexChanged(QString)"), self.day_combo_box1)
		self.connect(self.m_box1, SIGNAL("currentIndexChanged(QString)"), self.day_combo_box1)

		#GRID SIZE
		grid.setHorizontalSpacing(SEARCH_MARKS_X_GRID)
		grid.setVerticalSpacing(SEARCH_MARKS_Y_GRID)

		#WIDGETS TO GRID
		grid.addWidget(label_valido,GRID_X_POSITION_VALIDO,GRID_Y_POSITION_LABEL)
		grid.addWidget(self.text_valido,GRID_X_POSITION_VALIDO,1)
		grid.addWidget(label_title,GRID_X_POSITION_SEARCH_MARK_TITLE,GRID_Y_POSITION_SEARCH_MARK_TITLE)
		grid.addWidget(label_date1,GRID_X_POSITION_DATEMARK,GRID_Y_POSITION_SEARCH_MARK_DATE)
		grid.addWidget(button_search,GRID_X_POSITION_CREATE_SEARCH_MARK,GRID_Y_POSITION_CREATE_SEARCH_MARK)
		grid.addWidget(button_insert,GRID_X_POSITION_CREATE_SEARCH_MARK+2,GRID_Y_POSITION_CREATE_SEARCH_MARK)
		grid.addWidget(button_back,GRID_X_POSITION_BACK_SEARCH_MARK,GRID_Y_POSITION_BACK_SEARCH_MARK)
		grid.addWidget(self.marks_table,GRID_X_POSITION_SEARCH_MARK_TABLE_1,GRID_Y_POSITION_SEARCH_MARK_TABLE_1,
						GRID_X_POSITION_SEARCH_MARK_TABLE_2,GRID_Y_POSITION_SEARCH_MARK_TABLE_1)

		grid.addWidget(self.d_box1,GRID_X_POSITION_DATEMARK,GRID_Y_POSITION_DAY_DATEMARK)
		grid.addWidget(self.m_box1,GRID_X_POSITION_DATEMARK,GRID_Y_POSITION_MONTH_DATEMARK)
		grid.addWidget(self.y_box1,GRID_X_POSITION_DATEMARK,GRID_Y_POSITION_YEAR_DATEMARK)

		grid.addWidget(label_pin,GRID_X_POSITION_PIN,GRID_Y_POSITION_LABEL)
		grid.addWidget(self.text_name,GRID_X_POSITION_PIN,GRID_Y_POSITION_TEXT,1,GRID_Y_POSITION_TEXT+3)

		#LAYAOUT
		self.setLayout(grid)

	def search_marks_function(self):
		if(self.modify_mark_singleton):
			QMessageBox.warning(self, 'Error',MODIFY_MARK_OPENED, QMessageBox.Ok)
		else:
			day1=self.d_box1.currentText()
			month1=self.m_box1.currentText()
			year1=self.y_box1.currentText()
			datestr1=date_to_str(year1,month1,day1)
			db=get_connection()
			if(db):
				self.list_marks=controller_mark.get_marks_day(self.worker.pin,datestr1,db,not self.text_valido.isChecked())
				self.insert_marks_table()

	def insert_marks_table(self):
		self.clear_marks_table()
		if(len(self.list_marks)):
			self.rows = len(self.list_marks)
			self.marks_table.setRowCount(self.rows)
			stringVert = []
			for index_mark in range(len(self.list_marks)):
				self.marks_table.setItem(index_mark,0, QTableWidgetItem(self.list_marks[index_mark].hora))
				if(self.list_marks[index_mark].valido):
					self.marks_table.setItem(index_mark,1, QTableWidgetItem(CONTROL_MARK_ACTIVO))
				else:
					self.marks_table.setItem(index_mark,1, QTableWidgetItem(CONTROL_MARK_INACTIVO))
				self.btn_sell = QPushButton(CONTROL_MARK_SEARCH_MESSAGE)
				self.btn_sell.clicked.connect(self.modification_mark)
				self.marks_table.setCellWidget(index_mark,2,self.btn_sell)
				stringVert.append(str(index_mark+1))
			self.marks_table.setVerticalHeaderLabels(stringVert)

	def clear_marks_table(self):
		self.marks_table.clear();
		self.marks_table.setRowCount(0);
		self.marks_table.setColumnCount(SIZE_COLUMNS_TABLE_MARKS)
		self.marks_table.setHorizontalHeaderLabels(QString(SEARCH_MARKS_TITLE_ROWS).split(SPLIT_TABLE_MARKS))

	def modification_mark(self):
		index = self.marks_table.indexAt(qApp.focusWidget().pos())
		if index.isValid():
			if(self.modify_mark_singleton):
				QMessageBox.warning(self, 'Error',MODIFY_MARK_OPENED, QMessageBox.Ok)
			else:
				self.modify_mark_singleton=True
				self.ventana=modify_mark_view.modify_mark_view(self.list_marks,index.row())
				self.ventana.exec_()
				self.ventana=None
				self.insert_marks_table()
				self.modify_mark_singleton=False

	def create_combo_box(self):
		actual_date=datetime.datetime.now()
		year_list=range(actual_date.year - MORE_YEARS,actual_date.year + 1)
		year_list.reverse()
		actual_date=to_date(self.date_d,True)
		for year in year_list:
			self.y_box1.addItem(str(year))
		self.y_box1.setCurrentIndex(actual_date.year-year_list[0])
		for month in range(1,13):
			str_month=str(month)
			if(month<10):
				str_month="0"+str_month
			self.m_box1.addItem(str_month)
		self.m_box1.setCurrentIndex(actual_date.month - 1)
		self.max_day1=0
		if(actual_date.month==2):
			self.max_day1=int(actual_date.year%4==0)+28
		elif(actual_date.month==1 or actual_date.month==3 or actual_date.month==5 or actual_date.month==7 or actual_date.month==8 or actual_date.month==10 or actual_date.month==12):
			self.max_day1=31
		else:
			self.max_day1=30
		for day in range(1,self.max_day1+1):
			str_day=str(day)
			if(day<10):
				str_day="0"+str_day
			self.d_box1.addItem(str_day)
		self.d_box1.setCurrentIndex(actual_date.day - 1)

	def day_combo_box1(self):
		current_day = int(self.d_box1.currentText())
		current_month = int(self.m_box1.currentText())
		current_year = int(self.y_box1.currentText())
		new_day=0
		if(current_month==2):
			new_day=int(current_year%4==0)+28
		elif(current_month==1 or current_month==3 or current_month==5 or current_month==7 or current_month==8 or current_month==10 or current_month==12):
			new_day=31
		else:
			new_day=30
		if(self.max_day1!=new_day):
			self.max_day1=new_day
			self.d_box1.clear()
			for day in range(1,self.max_day1+1):
				str_day=str(day)
				if(day<10):
					str_day="0"+str_day
				self.d_box1.addItem(str_day)
			if(current_day<=self.max_day1):
				self.d_box1.setCurrentIndex(current_day - 1)
			else:
				self.d_box1.setCurrentIndex(0)

	def closeEvent(self, evnt):
		if(self.ventana):
			self.ventana.close()

	def new_marks_function(self):
		if(self.modify_mark_singleton):
			QMessageBox.warning(self, 'Error',MODIFY_MARK_OPENED, QMessageBox.Ok)
		else:
			self.modify_mark_singleton=True
			self.ventana = insert_marks_view.insert_marks_view(self.worker,self.date_d)
			self.ventana.exec_()
			self.ventana=None
			self.modify_mark_singleton=False
