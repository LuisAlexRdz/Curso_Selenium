#declara variables
a=10
b=6
c=11

#operadores matematicos y relacionales
print("Son iguales: "+ str(a==b))
print("Es a menor que b: "+ str(a<=b))
print("Es a mayor que b: "+ str(a>=b))
print("Son diferentes: "+ str(a!=b))

#Operadores logicos
#comparacion Y
print("si A e menor que B y A es menor que C: "+str(a<b and a<c))

#Comparacion Ó
print("si A e menor que B ó A es menor que C: "+str(a<b or a<c))