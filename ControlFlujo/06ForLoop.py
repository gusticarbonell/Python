# Principalmente para poder listar cualquier elemento.

for numero in range(5):  # range, secuencia de numeros para el for[0,1,2,3,4]
    print(numero, numero * "Samsung ")


# Buscar un numero

buscar = input("Inserte su numero ")
for numero in range(5):  # range(5) es iterable como los strings.
    print(numero)
    if numero == int(buscar):
        print("encontrado ", buscar)
        break
else:
    print("No encontro el numero buscado")

for char in "ultimate python":
    print(char)
