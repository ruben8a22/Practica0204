#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for numero1 in range(1, 11):
    for numero2 in range(1, 11):
        resultado = numero1 * numero2
        print(numero1, 'x', numero2, '=', resultado)