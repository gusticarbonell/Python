def hola(nombre, apellido):  # PARAMETROS
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Nicolas", "Schurman")  # ARGUMENTOS
hola("chanchito", "feliz")


# En el caso de parametros opcionales

def hola(nombre, apellido="Feliz"):  # PARAMETROS
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Nicolas", "Schurman")  # ARGUMENTOS
hola("chanchito")


# En el caso de argumentos nombrados
hola(apellido="Schurman", nombre="Wolfgang")
