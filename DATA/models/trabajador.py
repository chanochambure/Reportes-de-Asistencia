#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Trabajador():
	pin 				= ""
	name				= ""
	father_last_name	= ""
	mother_last_name	= ""
	activo				= 1
	def  __init__(self, row_trabajador):
		self.pin	 			= row_trabajador[0]
		self.name		 		= row_trabajador[1]
		self.father_last_name 	= row_trabajador[2]
		self.mother_last_name 	= row_trabajador[3]
		self.activo 			= row_trabajador[4]