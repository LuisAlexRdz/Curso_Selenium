#ingrear valor a variables de tipo string
print("Cual es tu nombre: ")
nom=input()
print("Cual es tu apellido paterno: ")
ap=input()
print("Cual es tu apellido materno: ")
am=input()

#ingresar valor a variables de tipo entero
print("Dame le valor de A: ")
a=int(input())
print("Dame el valor de B: ")
b=int(input())

suma= a + b

print("Tu nombre es: {} {} {} ".format(nom,ap,am))
print("La suma de {} + {} = {}".format(a,b,suma))
