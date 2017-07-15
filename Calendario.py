import sys
import pickle
from PyQt5.QtWidgets import (QDialog,QDateEdit,QTextEdit,QDialogButtonBox,QCalendarWidget,QApplication,QMessageBox,QInputDialog,QListView,QErrorMessage)
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QStyle
from PyQt5.uic import loadUi
from PyQt5.QtGui import QStandardItemModel,QStandardItem

class Configuracion(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        loadUi("Configuracion.ui",self)
        FechaI=self.CalendarioFechaI.selectedDate()
        FechaF=FechaI.addDays(1)
        self.CalendarioFechaI.setToolTip('Ingresa la <b> Fecha</b> de inicio de tu proyecto')
        self.CalendarioFechaF.setToolTip('Ingresa la <b> Fecha</b> de cierre de tu proyecto')
        icono1='SP_ArrowRight'
        icono2='SP_DialogCancelButton'
        self.Agregar.setIcon(self.style().standardIcon(getattr(QStyle,icono1)))
        self.Eliminar.setIcon(self.style().standardIcon(getattr(QStyle,icono2)))
        self.Agregar.setToolTip('Haz click aqui para <b>agregar</b> un objetivo nuevo')
        self.Eliminar.setToolTip('Haz click aqui para <b>eliminar</b> uno o más objetivos seleccionados')
        self.Objetivos.setToolTip('Aqui se encuentran los objetivos iniciales del proyecto, haz click en uno o en mas objetivos y en eliminar para eliminarlos')
        self.error=QErrorMessage(self)
        self.valido=True
        self.Agregar.clicked.connect(self.AgregarItems)
        self.Eliminar.clicked.connect(self.EliminarItems)
        self.caja=QStandardItemModel(self.Objetivos)
        self.objetivos=[]
        self.Objetivos.setModel(self.caja)
        self.Objetivos.show()
        self.CalendarioFechaF.setSelectedDate(FechaF)
        self.FechaIcaja.setText(FechaI.toString())
        self.FechaFcaja.setText(FechaF.toString())
        self.CalendarioFechaI.clicked[QDate].connect(self.ActualizarFechaI)
        self.CalendarioFechaF.clicked[QDate].connect(self.ActualizarFechaF)
        self.NombreProyecto.setToolTip('Ingresa el nombre de tu proyecto')
        self.Terminar.accepted.connect(self.terminado)
    def ActualizarFechaI(self, date):
        self.FechaIcaja.setText(date.toString())
        fecha=date.addDays(1)
        self.FechaFcaja.setText(fecha.toString())
    def ActualizarFechaF(self,date):
        if date.__le__(self.CalendarioFechaI.selectedDate()) or date.__eq__(self.CalendarioFechaI.selectedDate()):
            self.error.showMessage('La fecha ingresada no es valida por favor seleccione otra')
            self.valido=False
        else:
            self.FechaFcaja.setText(date.toString())
            self.valido=True
    def AgregarItems(self):
        texto,ok=QInputDialog.getText(self,'Ingresar objetivo','Ingresa el objetivo')
        if ok:
           item=QStandardItem(texto)
           self.caja.appendRow(item)
           self.objetivos.append(texto)
    def EliminarItems(self):
        seleccionados=self.Objetivos.selectedIndexes()
        for i in seleccionados:
            self.caja.takeRow(i.row())
    def terminado(self):
        formato='dd/MM/yyyy'
        Fecha1,Fecha2=self.CalendarioFechaI.selectedDate(),self.CalendarioFechaF.selectedDate()
        datos={'Nombre del Proyecto':self.NombreProyecto.toPlainText(),'Fecha Inicio':Fecha1.toString(formato),'Fecha Fin':Fecha2.toString(formato),'Objetivos':self.objetivos}
        serializar=open(datos['Nombre del Proyecto']+'.pickle',"wb")
        print(datos)
        pickle.dump(datos,serializar)
        


