a= 25
b= 30
c= 15

if (a<b):
    print("El mayor es: "+ str(b))
else:
    print("El mayor es b: "+ str(a))

nombre= "Juan"

if  (nombre=='Juan'):
    print("Tu nombre es :"+ nombre)

if (a<=b):
    print("{} es menor o igual que {}".format(a,b))

if (a>b and a>c):
    print("El mayor es: "+str(a))
elif (b>a and b>c):
    print("El mayor es: " + str(b))

if (a<b or a>c):
    print("{} es menor que {} ó es mayor que {}".format(a,b,c))