#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de
# más abajo, de altura el número introducido.


numero = int(input("Introduce un número entero:\n"))

for t in range(numero):
    print("*" * (t + 1))