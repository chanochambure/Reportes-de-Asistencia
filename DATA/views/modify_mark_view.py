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
from models import mark
from controller import controller_mark

class modify_mark_view(QDialog):
	def __init__(self,mlist,mark_to_mod,parent=None):
		super(modify_mark_view, self).__init__(parent)
		self.mark_list = mlist
		self.mark_index = mark_to_mod
		self.modify_mark_create()
		self.setWindowTitle(ADMIN_MODIFY_MARK_TITLE)
		self.show()

	def modify_mark_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(ADMIN_MODIFY_MARK_TITLE)
		label_date = QLabel(ADMIN_INSERT_MARK_DATE)
		label_time = QLabel(ADMIN_INSERT_MARK_TIME)
		label_valido = QLabel(ADMIN_MODIFY_MARK_VALID)
		label_tipo = QLabel(ADMIN_INSERT_MARK_TYPE)
		self.d_box = QComboBox()
		self.m_box = QComboBox()
		self.y_box = QComboBox()
		self.text_hour = QComboBox()
		self.text_min = QComboBox()
		self.text_valido = QRadioButton()
		self.text_tipo = QComboBox()
		button_insert = QPushButton(BUTTON_MODIFY_MARKS,self)
		button_back = QPushButton(BUTTON_BACK,self)

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		button_insert.setFixedSize(BUTTON_SIZE_INSERT_MARKS_VIEW_X,BUTTON_SIZE_INSERT_MARKS_VIEW_Y)
		button_back.setFixedSize(BUTTON_SIZE_INSERT_MARKS_VIEW_X,BUTTON_SIZE_INSERT_MARKS_VIEW_Y)
		self.text_valido.setChecked(bool(self.mark_list[self.mark_index].valido))
		self.create_combo_box()

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)
		self.connect(button_insert, SIGNAL("clicked()"),self.modify_marks_function)
		self.connect(self.y_box, SIGNAL("currentIndexChanged(QString)"), self.day_combo_box)
		self.connect(self.m_box, SIGNAL("currentIndexChanged(QString)"), self.day_combo_box)

		#GRID SIZE
		grid.setHorizontalSpacing(ADMIN_MOFIDY_MARKS_X)
		grid.setVerticalSpacing(ADMIN_MOFIDY_MARKS_Y)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_INSERT_WORK_TITLE,GRID_Y_POSITION_INSERT_WORK_TITLE)
		grid.addWidget(label_date,GRID_X_POSITION_DATE,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_time,GRID_X_POSITION_TIME,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_valido,GRID_X_POSITION_TIME+1,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_tipo,GRID_X_POSITION_TIME+2,GRID_Y_POSITION_LABEL)
		grid.addWidget(self.d_box,GRID_X_POSITION_DATE,GRID_Y_POSITION_DAY_DATE)
		grid.addWidget(self.m_box,GRID_X_POSITION_DATE,GRID_Y_POSITION_MONTH_DATE)
		grid.addWidget(self.y_box,GRID_X_POSITION_DATE,GRID_Y_POSITION_YEAR_DATE)
		grid.addWidget(self.text_hour,GRID_X_POSITION_TIME,GRID_Y_POSITION_HOUR_TIME)
		grid.addWidget(self.text_min,GRID_X_POSITION_TIME,GRID_Y_POSITION_MIN_TIME)
		grid.addWidget(self.text_valido,GRID_X_POSITION_TIME+1,1)
		grid.addWidget(self.text_tipo,GRID_X_POSITION_TIME+2,1)
		grid.addWidget(button_insert,GRID_X_POSITION_MODIFY_MARK,GRID_Y_POSITION_MODIFY_MARK)
		grid.addWidget(button_back,GRID_X_POSITION_BACK_MODIFY_MARK,GRID_Y_POSITION_BACK_MODIFY_MARK)

		#LAYAOUT
		self.setLayout(grid)

	def modify_marks_function(self):
		day=self.d_box.currentText()
		month=self.m_box.currentText()
		year=self.y_box.currentText()
		hour=self.text_hour.currentText()
		min=self.text_min.currentText()
		tvalido = self.text_valido.isChecked()
		ttipo=bool(self.text_tipo.currentIndex())
		str_datetime=datetime_to_str(day,month,year,hour,min)
		reply=QMessageBox.question(self, 'Message',CREATE_MARK_MODIFY_QUESTION,QMessageBox.Yes,QMessageBox.No)
		if reply == QMessageBox.Yes:
			db=get_connection()
			if(db):
				if(controller_mark.has_a_check(self.mark_list[self.mark_index].pin,str_datetime,db,False,self.mark_list[self.mark_index].id)):
					QMessageBox.warning(self, 'Error',WORKER_HAVE_ALREADY_THIS_MARK, QMessageBox.Ok)
				elif(controller_mark.valid_date(str_datetime)):
					QMessageBox.warning(self, 'Error',MARK_NO_EXIST_YET, QMessageBox.Ok)
				elif(self.mark_list[self.mark_index].update(db.cursor())):
					self.mark_list[self.mark_index].hora = str_datetime
					self.mark_list[self.mark_index].valido = tvalido
					self.mark_list[self.mark_index].tipo = ttipo
					db.commit()
					db.close()
					QMessageBox.question(self, 'Message',MOD_MARK_SUCCESS,QMessageBox.Ok)
					self.close()

	def create_combo_box(self):
		self.text_tipo.addItem(MARK_TYPE_INTRO_NAME)
		self.text_tipo.addItem(MARK_TYPE_EXIT_NAME)
		self.text_tipo.setCurrentIndex(int(self.mark_list[self.mark_index].tipo))
		actual_date=to_datetime(self.mark_list[self.mark_index].hora,True)
		for hour in range(0,24):
			str_hour=str(hour)
			if(hour<10):
				str_hour="0"+str_hour
			self.text_hour.addItem(str_hour)
		self.text_hour.setCurrentIndex(actual_date.hour)
		for min in range(0,60):
			str_min=str(min)
			if(min<10):
				str_min="0"+str_min
			self.text_min.addItem(str_min)
		self.text_min.setCurrentIndex(actual_date.minute)
		year_list=range(actual_date.year - MORE_YEARS,actual_date.year + 1)
		year_list.reverse()
		for year in year_list:
			self.y_box.addItem(str(year))
		for month in range(1,13):
			str_month=str(month)
			if(month<10):
				str_month="0"+str_month
			self.m_box.addItem(str_month)
		self.m_box.setCurrentIndex(actual_date.month - 1)
		self.max_day=0
		if(actual_date.month==2):
			self.max_day=int(actual_date.year%4==0)+28
		elif(actual_date.month==1 or actual_date.month==3 or actual_date.month==5 or actual_date.month==7 or actual_date.month==8 or actual_date.month==10 or actual_date.month==12):
			self.max_day=31
		else:
			self.max_day=30
		for day in range(1,self.max_day+1):
			str_day=str(day)
			if(day<10):
				str_day="0"+str_day
			self.d_box.addItem(str_day)
		self.d_box.setCurrentIndex(actual_date.day - 1)

	def day_combo_box(self):
		current_day = int(self.d_box.currentText())
		current_month = int(self.m_box.currentText())
		current_year = int(self.y_box.currentText())
		new_day=0
		if(current_month==2):
			new_day=int(current_year%4==0)+28
		elif(current_month==1 or current_month==3 or current_month==5 or current_month==7 or current_month==8 or current_month==10 or current_month==12):
			new_day=31
		else:
			new_day=30
		if(self.max_day!=new_day):
			self.max_day=new_day
			self.d_box.clear()
			for day in range(1,self.max_day+1):
				str_day=str(day)
				if(day<10):
					str_day="0"+str_day
				self.d_box.addItem(str_day)
			if(current_day<=self.max_day):
				self.d_box.setCurrentIndex(current_day - 1)
			else:
				self.d_box.setCurrentIndex(0)
