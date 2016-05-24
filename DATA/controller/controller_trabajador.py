#!/usr/bin/env python
# -*- coding: utf-8 -*-

def pin_is_invalid(str_pin,db):
	cursor=db.cursor()
	select_worker="select * from Trabajador where pin=%s"%(str_pin)
	cursor.execute(select_worker)
	rows = cursor.fetchall()
	return len(rows)>0