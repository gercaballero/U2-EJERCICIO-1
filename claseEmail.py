import verificador

class Email:
    __id_cuenta=None
    __dominio=None
    __tipo_dom=None
    __password=None

    def __init__(self,id_cuenta='',dom='',tipodom='',passw=''):
        self.__id_cuenta=id_cuenta
        self.__dominio=dom
        self.__tipo_dom=tipodom
        self.__password=passw
    def mostrar(self):
        print ('ID: {}, DOMINIO: {}, TIPO DOM: {}, PASSWORD:{} \n'.format(self.__id_cuenta,self.__dominio, self.__tipo_dom, self.__password))
        
    def retornaMail(self):
        return ('{}@{}.{}'.format(self.__id_cuenta, self.__dominio, self.__tipo_dom))

    def getDominio(self):
        return str(self.__dominio)
    def getID(self):
        return str(self.__id_cuenta)

    def cambioPass(self):
        intento=0               #Se pone un contador de 3 intentos  
        while intento!=4:  
             actual=input("Ingrese su contraseña actual: ")
             if actual==self.__password:
                 nueva=input("Ingrese su contraseña nueva: ")
                 self.__password=nueva
                 print("CONTRASEÑA MODIFICADA\n")
                 break
             else:
                  print("CONTRASEÑA INCORRECTA\n")
                  intento=intento+1
                  print ("intentos restantes {}".format(4-intento))

    @classmethod
    def crearCuenta(cls, correo):
                separador1="@"
                separador2="."
                separado1=correo.split(separador1)
                separado2=separado1[1].split(separador2)
                return cls(separado1[0],separado2[0],separado2[1],separado1[0])
