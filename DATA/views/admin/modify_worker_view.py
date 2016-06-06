#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from datetime import datetime,date

#Import de Modulos
BASE_DIR='../../'
sys.path.insert(0,BASE_DIR)
from constants import *
from models import trabajador
from controller import controller_trabajador,controller_lunchtime

class modify_worker_view(QDialog):
	def __init__(self,worker_to_mod,parent=None):
		super(modify_worker_view, self).__init__(parent)
		self.worker = worker_to_mod
		self.modify_worker_create()
		self.setWindowTitle(ADMIN_MODIFY_WORKER_TITLE)
		self.show()

	def modify_worker_create(self):
		#GRID
		grid = QGridLayout()

		#WIDGETS
		label_title = QLabel(ADMIN_MODIFY_WORKER_TITLE)
		label_pin = QLabel(ADMIN_INSERT_WORKER_PIN)
		label_name = QLabel(ADMIN_INSERT_WORKER_NAME)
		label_father_last_name = QLabel(ADMIN_INSERT_WORKER_FNAME)
		label_mother_last_name = QLabel(ADMIN_INSERT_WORKER_MNAME)
		label_intro_hour = QLabel(ADMIN_INSERT_INTRO_HOUR)
		label_exit_hour = QLabel(ADMIN_INSERT_EXIT_HOUR)
		label_lunchtime = QLabel(ADMIN_INSERT_LUNCHTIME_MINUTES)
		label_lunchdate = QLabel(ADMIN_MOD_WORKER_LUNCHDATE)
		label_active = QLabel(ADMIN_MOD_WORKER_ACTIVE)
		self.text_pin = QLineEdit()
		self.text_name = QLineEdit()
		self.text_fname = QLineEdit()
		self.text_mname = QLineEdit()
		self.text_lunchtime = QLineEdit()
		self.text_intro_hour = QComboBox()
		self.text_intro_min = QComboBox()
		self.text_exit_hour = QComboBox()
		self.text_exit_min = QComboBox()
		self.text_active = QRadioButton()
		self.d_box = QComboBox()
		self.m_box = QComboBox()
		self.y_box = QComboBox()
		button_mod = QPushButton(BUTTON_MOD_WORKER,self)
		button_back = QPushButton(BUTTON_BACK,self)

		#Modificacion widgets
		font_title = QFont()
		font_title.setPointSize(FONT_TITLE_SIZE)
		label_title.setFont(font_title)
		button_mod.setFixedSize(BUTTON_SIZE_MOD_WORKER_VIEW_X,BUTTON_SIZE_MOD_WORKER_VIEW_Y)
		button_back.setFixedSize(BUTTON_SIZE_MOD_WORKER_VIEW_X,BUTTON_SIZE_MOD_WORKER_VIEW_Y)
		self.text_pin.setText(self.worker.pin)
		self.text_pin.setDisabled(True)
		self.text_name.setText(self.worker.name)
		self.text_fname.setText(self.worker.father_last_name)
		self.text_mname.setText(self.worker.mother_last_name)
		db=get_connection(False)
		self.text_lunchtime.setText(str(controller_lunchtime.get_lunchtime_minutes(self.worker.idlt,db)))
		self.text_active.setChecked(bool(self.worker.activo))
		if(db):
			db.close()
		for hour in range(0,24):
			str_hour=str(hour)
			if(hour<10):
				str_hour="0"+str_hour
			self.text_intro_hour.addItem(str_hour)
			self.text_exit_hour.addItem(str_hour)
		for min in range(0,60):
			str_min=str(min)
			if(min<10):
				str_min="0"+str_min
			self.text_intro_min.addItem(str_min)
			self.text_exit_min.addItem(str_min)
		intro_hour_list=self.worker.hora_entrada.split(":")
		exit_hour_list=self.worker.hora_salida.split(":")
		self.text_intro_hour.setCurrentIndex(int(intro_hour_list[0]))
		self.text_intro_min.setCurrentIndex(int(intro_hour_list[1]))
		self.text_exit_hour.setCurrentIndex(int(exit_hour_list[0]))
		self.text_exit_min.setCurrentIndex(int(exit_hour_list[1]))
		self.create_combo_box()

		#FUNCTION
		self.connect(button_back, SIGNAL("clicked()"),self.close)
		self.connect(button_mod, SIGNAL("clicked()"),self.modify_worker_function)
		self.connect(self.y_box, SIGNAL("currentIndexChanged(QString)"), self.day_combo_box)
		self.connect(self.m_box, SIGNAL("currentIndexChanged(QString)"), self.day_combo_box)

		#GRID SIZE
		grid.setHorizontalSpacing(ADMIN_MOD_WORKER_X)
		grid.setVerticalSpacing(ADMIN_MOD_WORKER_Y)

		#WIDGETS TO GRID
		grid.addWidget(label_title,GRID_X_POSITION_INSERT_WORK_TITLE,GRID_Y_POSITION_INSERT_WORK_TITLE)
		grid.addWidget(label_pin,GRID_X_POSITION_PIN,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_name,GRID_X_POSITION_NAME,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_father_last_name,GRID_X_POSITION_FNAME,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_mother_last_name,GRID_X_POSITION_MNAME,GRID_Y_POSITION_LABEL)
		grid.addWidget(label_intro_hour,GRID_X_POSITION_IHOUR,GRID_Y_POSITION_LABEL_HOUR)
		grid.addWidget(label_exit_hour,GRID_X_POSITION_EHOUR,GRID_Y_POSITION_LABEL_HOUR)
		grid.addWidget(label_lunchtime,GRID_X_POSITION_LUNCH+1,GRID_Y_POSITION_LABEL_HOUR)
		grid.addWidget(label_lunchdate,GRID_X_POSITION_DATELUNCH,GRID_Y_POSITION_LABEL_HOUR)
		grid.addWidget(label_active,GRID_X_POSITION_ACTIVE,GRID_Y_POSITION_LABEL)

		grid.addWidget(self.text_pin,GRID_X_POSITION_PIN,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_name,GRID_X_POSITION_NAME,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_fname,GRID_X_POSITION_FNAME,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_mname,GRID_X_POSITION_MNAME,GRID_Y_POSITION_TEXT)
		grid.addWidget(self.text_active,GRID_X_POSITION_ACTIVE,GRID_Y_POSITION_TEXT)
		grid.addWidget(button_mod,GRID_X_POSITION_CREATE_MOD_WORK,GRID_Y_POSITION_CREATE_MOD_WORK)
		grid.addWidget(button_back,GRID_X_POSITION_BACK_MOD_WORK,GRID_Y_POSITION_BACK_MOD_WORK)
		grid.addWidget(self.text_lunchtime,GRID_X_POSITION_LUNCH-1,GRID_Y_POSITION_HOUR_INSERT,GRID_X_POSITION_LUNCH,GRID_Y_POSITION_HOUR_INSERT+1)

		grid.addWidget(self.text_intro_hour,GRID_X_POSITION_IHOUR,GRID_Y_POSITION_HOUR_INSERT)
		grid.addWidget(self.text_intro_min,GRID_X_POSITION_IHOUR,GRID_Y_POSITION_MIN_INSERT)
		grid.addWidget(self.text_exit_hour,GRID_X_POSITION_EHOUR,GRID_Y_POSITION_HOUR_INSERT)
		grid.addWidget(self.text_exit_min,GRID_X_POSITION_EHOUR,GRID_Y_POSITION_MIN_INSERT)

		grid.addWidget(self.d_box,GRID_X_POSITION_DATELUNCH,GRID_Y_POSITION_DAY_LUNCHDATE)
		grid.addWidget(self.m_box,GRID_X_POSITION_DATELUNCH,GRID_Y_POSITION_MONTH_LUNCHDATE)
		grid.addWidget(self.y_box,GRID_X_POSITION_DATELUNCH,GRID_Y_POSITION_YEAR_LUNCHDATE)

		#LAYAOUT
		self.setLayout(grid)

	def modify_worker_function(self):
		db=get_connection()
		day=self.d_box.currentText()
		month=self.m_box.currentText()
		year=self.y_box.currentText()
		name = self.text_name.text()
		fname = self.text_fname.text()
		mname = self.text_mname.text()
		activo = self.text_active.isChecked()
		lt_minutes = self.text_lunchtime.text()
		intro_t=time_to_str(str(int(self.text_intro_hour.currentText())),self.text_intro_min.currentText())
		exit_t=time_to_str(str(int(self.text_exit_hour.currentText())),self.text_exit_min.currentText())
		if(name == '' or fname=='' or mname=='' or lt_minutes==''):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_EMPTY_CAMP, QMessageBox.Ok)
		elif(str_is_invalid(name) or str_is_invalid(fname) or str_is_invalid(mname) or str_is_invalid(lt_minutes)):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_INVALID_CAMP, QMessageBox.Ok)
		elif(is_number(lt_minutes)==False):
			QMessageBox.warning(self, 'Error',CREATE_WORKER_INVALID_LT_MINUTES, QMessageBox.Ok)
		elif(name == self.worker.name and fname == self.worker.father_last_name and mname == self.worker.mother_last_name
			and activo == self.worker.activo and intro_t==self.worker.hora_entrada and exit_t==self.worker.hora_salida
			and int(lt_minutes)==controller_lunchtime.get_lunchtime_minutes(self.worker.idlt,db)):
			QMessageBox.warning(self, 'Error',MOD_WORKER_NO_CHANGES, QMessageBox.Ok)
		else:
			lt_minutes=int(lt_minutes)
			reply=QMessageBox.question(self, 'Message',MOD_WORKER_QUESTION,QMessageBox.Yes,QMessageBox.No)
			if reply == QMessageBox.Yes:
				if(db):
					lname = self.worker.name
					lfname = self.worker.father_last_name
					lmname = self.worker.mother_last_name
					lactivo = self.worker.activo
					ltimeen = self.worker.hora_entrada
					ltimesa = self.worker.hora_salida
					self.worker.name = name
					self.worker.father_last_name = fname
					self.worker.mother_last_name = mname
					self.worker.activo = activo
					self.worker.hora_entrada = intro_t
					self.worker.hora_salida = exit_t
					inserted=True
					if(self.worker.update(db.cursor())):
						lunchtime_t=controller_lunchtime.get_lunchtime(self.worker.idlt,db)
						if(lunchtime_t):
							if(lunchtime_t.minutos!=lt_minutes):
								if(to_date(lunchtime_t.fechavalido,True)>=datetime.date(int(year),int(month),int(day))):
									QMessageBox.warning(self, 'Error',CREATE_LUNCHTIME_INVALID_DATE+CREATE_LUNCHTIME_LAST_MOD+lunchtime_t.fechavalido, QMessageBox.Ok)
									inserted=False
								else:
									lunchtime_t.fechavalido=date_to_str(year,month,day)
									if(lunchtime_t.insert_new_lunchtime(lt_minutes,db.cursor())):
										self.worker.update_new_lunchtime(lunchtime_t.id,db.cursor())
						if(inserted):
							db.commit()
							QMessageBox.question(self, 'Message',MOD_WORKER_SUCCESS,QMessageBox.Ok)
							self.close()
						else:
							self.worker.name = lname
							self.worker.father_last_name = lfname
							self.worker.mother_last_name = lmname
							self.worker.activo = lactivo
							self.worker.hora_entrada = ltimeen
							self.worker.hora_salida = ltimesa
		if(db):
			db.close()

	def create_combo_box(self):
		db=get_connection()
		actual_date=controller_lunchtime.get_lunchtime_date(self.worker.idlt,db)
		if(db):
			db.close()
		act_year=datetime.datetime.now().year
		year_list=range(act_year - MORE_YEARS,act_year + 1)
		year_list.reverse()
		for year in year_list:
			self.y_box.addItem(str(year))
		self.y_box.setCurrentIndex(act_year-actual_date.year)
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
