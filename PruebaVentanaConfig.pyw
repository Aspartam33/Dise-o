from Calendario import Configuracion
import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QPushButton,QLabel)

class VentanaInicio(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(600,600)
        self.setWindowTitle("EjemplodeVentanaPrincipal")
        self.BotondeCreacion=QPushButton(self)
        self.BotondeCreacion.setText("Crear Nuevo Proyecto")
        self.BotondeCreacion.resize(300,20)
        self.VentanaEmergente=Configuracion()
        self.BotondeCreacion.clicked.connect(self.AbrirConfiguracion)
    def AbrirConfiguracion(self):
        self.VentanaEmergente.exec_()
        
app=QApplication(sys.argv)
ventana=VentanaInicio()
ventana.show()
app.exec_()