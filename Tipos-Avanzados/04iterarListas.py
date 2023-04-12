mascotas = ["perro", "gato", "cerdo", "vaca"]


# Tuplas, se accede como un listado
for mascota in enumerate(mascotas):
    print(mascota)


mascotas = ["perro", "gato", "cerdo", "vaca"]

# Indices
primero, segundo = [1, 2]
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
