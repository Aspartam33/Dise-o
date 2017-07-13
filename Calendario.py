import sys
from PyQt5.QtWidgets import (QDialog,QDateEdit,QTextEdit,QDialogButtonBox,QCalendarWidget,QApplication)
from PyQt5.uic import loadUi

class Configuracion(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        loadUi("Configuracion.ui",self)
        FechaI=self.CalendarioFechaI.selectedDate()
        self.CalendarioFechaF.setSelectedDate(FechaI.addDays(1))
        self.FechaIcaja.setDate(self.CalendarioFechaI.selectedDate())
        self.FechaFcaja.setDate(FechaI.addDays(1))