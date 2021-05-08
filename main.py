from claseEmail import Email          #Se importa la clase mail
import verificador                     #Se importa el verificador de expresiones regulares
from manejadorEmails import manejaEmails  #Se importa el majeador de mails para leer el archivo

def test():     #TEST DE EMAILS
    #EJEMPLOS DE EMAILS
    email1='informatica.fcefn@gmail.com'
    email2='wicc2019@unsj-cuim.edu'
    email3='informatica.gmail.com'
    email4='german@gmail'
    email5='POO@.com'
    lista=[]
    lista.extend([email1,email2,email3,email4,email5])
    for i in lista:
        if verificador.verificar(i):
            cuenta=Email.crearCuenta(i)
            print('---CUENTA DE {} CREADA---'.format(cuenta.getID()))
            cuenta.mostrar()
        else:
            print('NO SE PUEDE CREAR CUENTA {} \n'.format(i))

if __name__=='__main__':
    t=str(input('DESEA PROBAR EL TEST (S/N) : '))
    if t.lower()=='s':
        test() 
    print('-----PUNTO 1-----\n')
    cuenta1=Email('caballerogermangc','gmail','com','123german321') #Se crea una instancia de la clase Mail
    nombrecuenta1=input("INGRESE SU NOMBRE: ")
    print ('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombrecuenta1.upper(), cuenta1.retornaMail() ))
    print('-----PUNTO 2-----\n')
    print('~CAMBIO DE CONTRASEÑA~\n')
    cuenta1.cambioPass()
    cuenta1.mostrar()
    print('\n-----PUNTO 3-----\n')
    cuenta2=Email.crearCuenta('informatica.fcefn@gmail.com')
    cuenta2.mostrar()
    print('\n-----PUNTO 4-----\n')
    me=manejaEmails()               #Invoca al manejador de mails para cargar el archivo
    me.testEmail()                  #Carga la lista con objetos de la clase EMAIL
    domi=input("INGRESE EL DOMINIO QUE DESEA BUSCAR EN EL ARCHIVO: ")
    me.contador(domi)
