usuarios = [[2, "perro"], [1, "gato"], [4, "tortuga"], [5, "mono"]]

# Obtener solo el nombre
nombres = [usuario[1] for usuario in usuarios]
print(nombres)

# Filtrar
nombres_filtrados = [usuario for usuario in usuarios if usuario[0] > 2]
print(nombres_filtrados)

# Filtrar y transformar
nombres_filtrados_y_transformados = [usuario[1]
                                     for usuario in usuarios if usuario[0] > 2]
print(nombres_filtrados_y_transformados)

nombres_transformados = list(
    map(lambda usuario: usuario[1], nombres_filtrados_y_transformados))
print(nombres_transformados)
