numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# Tuplas crean nuevas listas y no se pueden modificar
punto = tuple([1, 2])
print(punto)

menosnumeros = numeros[:2]
print(menosnumeros)

primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

# Para modificar la lista de una tupla
listanumeros = list(numeros)
listanumeros[0] = "Samsung"
print(listanumeros)
