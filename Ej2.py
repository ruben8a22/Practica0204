#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el
# programa debe mostrar un error.

numero1 = int(input("Introduce el primer numero:"))
numero2 = int(input("Introduce el segundo numero:"))

if numero2 == 0:
    print("El divisor no puede ser 0")
else:
    (print(numero1 / numero2))