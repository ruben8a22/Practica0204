#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo que tenga
# tantas líneas como el número introducido, como el triángulo de más abajo.

numero = int(input("Introduce un número entero:\n"))

for t in range(1,numero + 1,2):
    for tr in range(t,0, - 2):
        print(tr, end=" ")
    print("")