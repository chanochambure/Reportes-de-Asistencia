#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import de Librerias
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#Import de Modulos
BASE_DIR='DATA'
sys.path.insert(0,BASE_DIR)
from constants import *
from views import main_view

def main():
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon('icon.png'))
	window = main_view.main_view()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
