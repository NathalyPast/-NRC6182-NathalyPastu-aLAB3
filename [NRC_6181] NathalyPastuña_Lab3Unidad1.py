#Agregamos el respectivo modulo
import datetime
#Clase cliente
class cliente():
    #Atributos
    def __init__(self, nombre, telefono):
        self.atributo1=nombre
        self.atributo2=telefono

def iniciarSeccion():
    nombre=input("Ingrese su nombre: ")
    telefono=input("Ingrese su telefono: ")
    print ("Su nombre es: ") +nombre ("con numero de telefono:")  +telefono 

#Clase tienda
class Tienda(): 
    #Atributos
    def __init__(self, nombre, telefono):
        self.atributo3=nombre
        self.atributo4=telefono 

#Clase administrador
class Administrador: 
    #Atributo
    def __init__(self, nombreTienda, ciudad, codigo ):
        self.atributo5=nombreTienda
        self.atributo6=ciudad
        self.atributo7=codigo

    def informacionTienda ():
        nombreTienda=input("Ingrese nombre de la tienda: ")
        ciudad=input("La ciudad es: ")
        codigo=input("Codigo emprsearial: ")
        print ("Nombre de la tienda es: ") +nombreTienda ("ubicado en: ") +ciudad ("codigo empresarial es: ") +codigo 
    

    #MENU PRINCIPAL

def menuPrincipal():
    while True:
        try:
            print("-------------MENU---------------") 
            print(" CLIENTE ---- PRESIONE (1)")
            print(" TIENDA ---- PRESIONE (2)")
            print(" ADMINISTRADOR ---- PRESIONE (3)") 
            opcionMenu= int(input("Ingrese una opcion: "))
            #op 1
            if opcionMenu==1:
                cliente()
                break 
               #op 2
            elif opcionMenu==2:
                Tienda()
                break   
               #op 3
            elif opcionMenu==3:
                Administrador()
                break   
            elif opcionMenu==4:
                print(" GRACIAS TENGA UN LINDO DIA")
                break 
            else:
                print("---------->Solo puede ingresar opciones dentro del rango del menu")
        except:
                print(" ---------- ")
