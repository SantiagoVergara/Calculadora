# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
from Calculadora import Ui_Form

class Main(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
	def siete (self):
		self.ui.pantalla.setText("7")
	def ocho (self):
		self.ui.pantalla.setText("8")
	def nueve (self):
		self.ui.pantalla.setText("9")
	def cuatro (self):
		self.ui.pantalla.setText("4")
	def cinco (self):
		self.ui.pantalla.setText("5")
	def seis (self):
		self.ui.pantalla.setText("6")
	def uno (self):
		self.ui.pantalla.setText("1")
	def dos (self):
		self.ui.pantalla.setText("2")
	def tres (self):
		self.ui.pantalla.setText("3")
	def cero (self):
		self.ui.pantalla.setText("0")

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = Main()
	window.show()
	sys.exit(app.exec_())

#http://www.slideshare.net/alexander.uni.fiis/pyqt-qtdesigner
