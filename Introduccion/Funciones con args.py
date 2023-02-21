#se define la funcion
def suma(*args):
    #Inicializa variable en 0
    resultado=0
    #Se ejecuta ciclo For desde n hasta args
    for n in args:
        #la variable resultado toma valor de n
        resultado= resultado + n
    print("El resultado es: "+str(resultado))
    #al terminar el ciclo regresa el valor de resultado
    return resultado

suma(5,9)
