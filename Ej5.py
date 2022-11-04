#Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin, de acuerdo al sexo y el nombre.
# Gryffindor está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y
# Slytheryn por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
# que le corresponde.

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
sexo = input("Introduce tu sexo:")
nombre = input("Introduce tu nombre:")

for i in alfabeto:
    if sexo == "h" and nombre[0] > alfabeto[12]:
        print("Eres de la casa Gryffindor")
        break
    if sexo == "m" and nombre[0] < alfabeto[12]:
        print("Eres de la casa Gryffindor")
        break
    else:
        print("Eres de la casa Slytheryn")
        break
