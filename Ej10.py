#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la
# contraseña hasta que introduzca la contraseña correcta.

contraseña = input("Introduzca su contraseña: ")
while contraseña != "navarra123":
   print("La contraseña es incorrecta.")
   contraseña = input("Introduzca su contraseña: ")
print("La contraseña es correcta.")