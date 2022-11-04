#Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.


frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
numeroVeces = 0
for n in frase:
   if n == letra:
       numeroVeces = numeroVeces + 1
print("El numero de veces que aparece es ", numeroVeces)
