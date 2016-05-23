#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Trabajador():
	pin 				= 0
	name				= ""
	father_last_name	= ""
	mother_last_name	= ""
	def  __init__(self, row_trabajador):
		self.pin	 			= row_trabajador[0]
		self.name		 		= row_trabajador[1]
		self.father_last_name 	= row_trabajador[2]
		self.mother_last_name 	= row_trabajador[3]