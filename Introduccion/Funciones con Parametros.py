"""#Se definen las funciones
def saludar():
    print("Hola como estas")

def salir():
    print("Hasta luego")

#Funcion con parametros
def suma(a,b):
    resultado=a+b
    print("La suma es: "+str(resultado))

#Se mandan llamar las funciones
saludar()
suma(8,10)
salir()"""

#Se define la funcion
def datos(nom,ap,am):
    print("Tu nombre es: {} {} {}".format(nom,ap,am))
    
#Se manda llamar la funcion
datos("Alex","Rdz","Pdr")