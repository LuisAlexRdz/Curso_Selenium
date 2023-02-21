#While sirve hasta que algo pase o se cumpla

inicio=1
fin=10

while (inicio<=fin):
    inicio= inicio +1
    if (inicio==5):
        continue
    print("Esto se repite: " + str(inicio))