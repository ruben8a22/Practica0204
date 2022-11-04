#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for num1 in range(1,11):
    for num2 in range(1,11):
        resultado = num1 * num2
        print(num1,'x', num2, '=', resultado)