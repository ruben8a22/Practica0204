#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido
# (desde 1 hasta su edad).


edad = int(input("Introduce tu edad:\n"))
añosCumplidos = edad + 1
for num in range(1, añosCumplidos):
    print("Has cumplido", num, "años")