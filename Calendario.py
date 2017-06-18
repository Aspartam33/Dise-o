import calendar
#Para el uso del modulo de calendario se necesita el formato aaaa/mm/dd en un string ingresado por el usuario(en la interface)
class Calendario:
    #Dada la funcion weekday del modulo calendar se requiere de transformar el numero entero de 0 a 6 a un string para especificar exactamente el día que cae el inicio
    # y el final de proyecto según lo ingrese el usuario
    dias={0:'Lunes',1:'Martes',2:'Miercoles',3:'Jueves',4:'Viernes',5:'Sabado',6:'Domingo'}
    def __init__(self,FechaIniIngre,FechaFinIngre):
        #Se toman los primeros parametros para realizar el calculo del día que cae el inicio y final según las fechas ingresadas por el usuario.
        self.InicioP=dias[calendar.weekday(int(FechaIniIngre.split('/')[0]),int(FechaIniIngre.split('/')[1]),int(FechaIniIngre.split('/').[2]))]+' '+FechaIniIngre
        self.FinP=dias[calendar.weekday(int(FechaFinIngre.split('/')[0]),int(FechaFinIngre.split('/')[1]),int(FechaFinIngre.split('/').[2]))]+' '+FechaFinIngre
    #Una vez realizado nuestro formateo de la fecha de inicio y proyecto y almacenado en el objeto Calendario procedemos a crear el calendario del proyecto
    # En este caso será en texto simple pero puede ser usado para creación grafica.
    def CalendarioTexto(self):






