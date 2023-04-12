numeros = [2, 4, 1, 45, 74, 22, 87, 34, 222, 564, 234, 12, 234, 56]

# Lista Ordenada, utiliza la lista creada
numeros.sort()
print(numeros)

# Lista ordenada, nueva lista
sorted(numeros, reverse=False)
print(numeros)

# Lista ordenada invertida
numeros.sort(reverse=True)
print(numeros)


usuarios = [[2, "perro"], [1, "gato"], [4, "tortuga"], [5, "mono"]]

usuarios.sort()
print(usuarios)

usuarios2 = [[2, "perro"], [1, "gato"], [4, "tortuga"], [5, "mono"]]


def ordena(elemento):
    return elemento[1]


usuarios2.sort(key=ordena)
print(usuarios2)

usuarios2.sort(key=lambda el: el[1], reverse=True)
print(usuarios2)
