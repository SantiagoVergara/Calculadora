# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculadora.ui'
#
# Created: Mon Feb  3 16:51:37 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(566, 274)
        self.siete = QtGui.QPushButton(Form)
        self.siete.setGeometry(QtCore.QRect(30, 80, 41, 31))
        self.siete.setObjectName(_fromUtf8("siete"))
        self.ocho = QtGui.QPushButton(Form)
        self.ocho.setGeometry(QtCore.QRect(90, 80, 41, 31))
        self.ocho.setObjectName(_fromUtf8("ocho"))
        self.cuatro = QtGui.QPushButton(Form)
        self.cuatro.setGeometry(QtCore.QRect(30, 120, 41, 31))
        self.cuatro.setObjectName(_fromUtf8("cuatro"))
        self.seis = QtGui.QPushButton(Form)
        self.seis.setGeometry(QtCore.QRect(150, 120, 41, 31))
        self.seis.setObjectName(_fromUtf8("seis"))
        self.tres = QtGui.QPushButton(Form)
        self.tres.setGeometry(QtCore.QRect(150, 160, 41, 31))
        self.tres.setObjectName(_fromUtf8("tres"))
        self.uno = QtGui.QPushButton(Form)
        self.uno.setGeometry(QtCore.QRect(30, 160, 41, 31))
        self.uno.setObjectName(_fromUtf8("uno"))
        self.nueve = QtGui.QPushButton(Form)
        self.nueve.setGeometry(QtCore.QRect(150, 80, 41, 31))
        self.nueve.setObjectName(_fromUtf8("nueve"))
        self.cinco = QtGui.QPushButton(Form)
        self.cinco.setGeometry(QtCore.QRect(90, 120, 41, 31))
        self.cinco.setObjectName(_fromUtf8("cinco"))
        self.dos = QtGui.QPushButton(Form)
        self.dos.setGeometry(QtCore.QRect(90, 160, 41, 31))
        self.dos.setObjectName(_fromUtf8("dos"))
        self.cero = QtGui.QPushButton(Form)
        self.cero.setGeometry(QtCore.QRect(30, 200, 41, 31))
        self.cero.setObjectName(_fromUtf8("cero"))
        self.dividir = QtGui.QPushButton(Form)
        self.dividir.setGeometry(QtCore.QRect(210, 80, 41, 31))
        self.dividir.setObjectName(_fromUtf8("dividir"))
        self.multiplicar = QtGui.QPushButton(Form)
        self.multiplicar.setGeometry(QtCore.QRect(210, 120, 41, 31))
        self.multiplicar.setObjectName(_fromUtf8("multiplicar"))
        self.restar = QtGui.QPushButton(Form)
        self.restar.setGeometry(QtCore.QRect(210, 160, 41, 31))
        self.restar.setObjectName(_fromUtf8("restar"))
        self.sumar = QtGui.QPushButton(Form)
        self.sumar.setGeometry(QtCore.QRect(210, 200, 41, 31))
        self.sumar.setObjectName(_fromUtf8("sumar"))
        self.igual = QtGui.QPushButton(Form)
        self.igual.setGeometry(QtCore.QRect(150, 200, 41, 31))
        self.igual.setObjectName(_fromUtf8("igual"))
        self.punto = QtGui.QPushButton(Form)
        self.punto.setGeometry(QtCore.QRect(90, 200, 41, 31))
        self.punto.setObjectName(_fromUtf8("punto"))
        self.pantalla = QtGui.QLineEdit(Form)
        self.pantalla.setEnabled(False)
        self.pantalla.setGeometry(QtCore.QRect(30, 30, 221, 31))
        self.pantalla.setObjectName(_fromUtf8("pantalla"))
        self.guardar = QtGui.QPushButton(Form)
        self.guardar.setGeometry(QtCore.QRect(90, 240, 98, 27))
        self.guardar.setObjectName(_fromUtf8("guardar"))
        self.Operaciones = QtGui.QTextEdit(Form)
        self.Operaciones.setGeometry(QtCore.QRect(310, 60, 241, 201))
        self.Operaciones.setMouseTracking(False)
        self.Operaciones.setObjectName(_fromUtf8("Operaciones"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 30, 171, 17))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.siete, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.siete)
        QtCore.QObject.connect(self.ocho, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.ocho)
        QtCore.QObject.connect(self.nueve, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.nueve)
        QtCore.QObject.connect(self.cuatro, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cuatro)
        QtCore.QObject.connect(self.cinco, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cinco)
        QtCore.QObject.connect(self.seis, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.seis)
        QtCore.QObject.connect(self.uno, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.uno)
        QtCore.QObject.connect(self.dos, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.dos)
        QtCore.QObject.connect(self.tres, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.tres)
        QtCore.QObject.connect(self.cero, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.cero)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.siete.setText(_translate("Form", "7", None))
        self.ocho.setText(_translate("Form", "8", None))
        self.cuatro.setText(_translate("Form", "4", None))
        self.seis.setText(_translate("Form", "6", None))
        self.tres.setText(_translate("Form", "3", None))
        self.uno.setText(_translate("Form", "1", None))
        self.nueve.setText(_translate("Form", "9", None))
        self.cinco.setText(_translate("Form", "5", None))
        self.dos.setText(_translate("Form", "2", None))
        self.cero.setText(_translate("Form", "0", None))
        self.dividir.setText(_translate("Form", "/", None))
        self.multiplicar.setText(_translate("Form", "*", None))
        self.restar.setText(_translate("Form", "-", None))
        self.sumar.setText(_translate("Form", "+", None))
        self.igual.setText(_translate("Form", "=", None))
        self.punto.setText(_translate("Form", ".", None))
        self.guardar.setText(_translate("Form", "Guardar", None))
        self.label.setText(_translate("Form", "Operaciones Guardadas:", None))

