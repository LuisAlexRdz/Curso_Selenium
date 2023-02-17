
texto = "Hola Bienvenido a Python"
#imprime el valor de la variable
print(texto)
#imprime solo el tercer digito
print(texto[3])
#Imprime un rango de digitos
print(texto[5:15])
#imprime del digito seleccionado hasta el final del enunciado
print(texto[5:])
#imrime desde el ultimo digito hasta el valor seleccionado
print(texto[-6:])

"""Imprime valores de casdena con .format"""

nom="Alejandro"
ap="Rodriguez"
am="Pedroza"

print("Tu nombre es {} tu apellido paterno es {} tu apellido materno es {}".format(nom,ap,am))