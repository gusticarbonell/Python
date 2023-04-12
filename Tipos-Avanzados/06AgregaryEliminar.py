mascotas = ["perro", "Lobo", "gato", "cerdo", "vaca"]

# Agregar elemtnos
mascotas.insert(1, "dog")
mascotas.append("foca")
print(mascotas)


# Eliminar elementos
mascotas.remove("cerdo")
mascotas.pop(4)
del mascotas[0]
mascotas.clear()  # Elimina todos los elementos
print(mascotas)
