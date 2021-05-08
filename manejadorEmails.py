import csv
from claseEmail import Email
import verificador

class manejaEmails:
    def __init__(self):
        self.__lista=[]

    def agregarMail(self, unEmail):
        self.__lista.append(unEmail)
    
    def testEmail(self):
        archivo=open('archivo.csv')
        reader=csv.reader(archivo)
        for fila in reader:
            if verificador.verificar(fila[0]):
                mail=Email.crearCuenta(fila[0])     #Crea objetos de la clase Email solo con un string del mail
                self.agregarMail(mail)              #Agrega los objetos a la lista
        archivo.close()

    def contador(self, dominio=''):
        contador=0              
        for i in self.__lista:
            if i.getDominio()==dominio:
                 contador=contador+1        #Cuenta si se cumple que el dominio es igual al ingresado
        print("LA CANTIDAD DE VECES QUE APARECE ESE DOMINIO ES DE {} VECES".format(contador))

