# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui 
import sys 
from Calculadora import Ui_Form
import ConfigParser

class Main(QtGui.QMainWindow): 
	def __init__(self):
		QtGui.QMainWindow.__init__(self) 
		self.ui = Ui_Form() 
		self.ui.setupUi(self) 
		self.operacion=""
		self.PrimerNumero=0
		self.SegundoNumero=0
		self.Calculo=""

	def siete (self):
		CaracterIngresado = self.ui.pantalla.text()
		self.ui.pantalla.setText(CaracterIngresado+"7")
		self.Calculo+="7"
	def ocho (self):
		CaracterIngresado = self.ui.pantalla.text() 
		self.ui.pantalla.setText(CaracterIngresado+"8")
		self.Calculo+="8"
	def nueve (self):
		CaracterIngresado = self.ui.pantalla.text()
		self.ui.pantalla.setText(CaracterIngresado+"9")
		self.Calculo+="9"
	def cuatro (self):
		CaracterIngresado = self.ui.pantalla.text()
		self.ui.pantalla.setText(CaracterIngresado+"4")
		self.Calculo+="4"
	def cinco (self):
		CaracterIngresado = self.ui.pantalla.text()
		self.ui.pantalla.setText(CaracterIngresado+"5")
		self.Calculo+="5"
	def seis (self):
		CaracterIngresado = self.ui.pantalla.text()
		self.ui.pantalla.setText(CaracterIngresado+"6")
		self.Calculo+="6"
	def uno (self):
		CaracterIngresado = self.ui.pantalla.text()
		self.ui.pantalla.setText(CaracterIngresado+"1")
		self.Calculo+="1"
	def dos (self):
		CaracterIngresado = self.ui.pantalla.text()
		self.ui.pantalla.setText(CaracterIngresado+"2")
		self.Calculo+="2"
	def tres (self):
		CaracterIngresado = self.ui.pantalla.text()
		self.ui.pantalla.setText(CaracterIngresado+"3")
		self.Calculo+="3"	
	def cero (self):
		CaracterIngresado = self.ui.pantalla.text()
		self.ui.pantalla.setText(CaracterIngresado+"0")
		self.Calculo+="0"
	def dividir (self):
		if self.PrimerNumero==0:		
			CaracterIngresado = self.ui.pantalla.text()
			self.PrimerNumero=CaracterIngresado
		else:
			self.igual()
		self.ui.pantalla.setText("")
		self.operacion="/"
		self.Calculo+="/"
	def multiplicar (self):
		if self.PrimerNumero==0:		
			CaracterIngresado = self.ui.pantalla.text()
			self.PrimerNumero=CaracterIngresado
		else:
			self.igual()
		self.ui.pantalla.setText("")
		self.operacion="*"
		self.Calculo+="*"
	def restar (self):
		if self.PrimerNumero==0:		
			CaracterIngresado = self.ui.pantalla.text()
			self.PrimerNumero=CaracterIngresado
		else:
			self.igual()
		self.ui.pantalla.setText("")
		self.operacion="-"
		self.Calculo+="-"
	def sumar (self):
		if self.PrimerNumero==0:		
			CaracterIngresado = self.ui.pantalla.text()
			self.PrimerNumero=CaracterIngresado
		else:
			self.igual()
		self.ui.pantalla.setText("")
		self.operacion="+"
		self.Calculo+="+"
	def punto (self):
		CaracterIngresado = self.ui.pantalla.text()
		self.ui.pantalla.setText(CaracterIngresado+".")
		self.Calculo+="."
	def igual (self):
		print "igual"
		self.SegundoNumero=self.ui.pantalla.text()
		resultado=0
		if self.operacion=="/":
			print "entro"
			resultado=float(self.PrimerNumero) / float(self.SegundoNumero)
		elif self.operacion=="*":
			print "entro"
			resultado=float(self.PrimerNumero) * float(self.SegundoNumero)
		elif self.operacion=="-":
			print "entro"
			resultado=float(self.PrimerNumero) - float(self.SegundoNumero)
		elif self.operacion=="+":
			print "entro"
			resultado=float(self.PrimerNumero) + float(self.SegundoNumero)
		self.ui.pantalla.setText(str(resultado))
		CalcResult=str(resultado)
		self.Calculo+="="
		self.Calculo+=CalcResult
		self.PrimerNumero=self.ui.pantalla.text()
		self.SegundoNumero=0
	def AC (self):
		CaracterIngresado = self.ui.pantalla.text()
		self.operacion=""
		self.PrimerNumero=0
		self.SegundoNumero=0
		self.ui.pantalla.setText("")
		self.Calculo=""

	def guardar(self):
		Config = ConfigParser.ConfigParser()
		calculos=open("CalculosGuardados.ini","a")
		Config.add_section(str(self.Calculo))
		Config.set(str(self.Calculo),"Operacion",str(self.Calculo))
		Config.write(calculos)
		calculos.close()



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = Main()
	window.show()
	sys.exit(app.exec_())
