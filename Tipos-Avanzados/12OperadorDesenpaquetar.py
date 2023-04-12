lista = (0, 1, 2, 3, 4)
# Aquí se imprimen los números 0, 1, 2, 3 y 4 directamente, no la variable "lista"
print(0, 1, 2, 3, 4)

# Desenpaquetamiento
print(*lista)  # Al agregar el asterisco antes de la variable, se desempaqueta la tupla y se imprimen sus elementos separados por comas

lista2 = [5, 6, 7]

# Aquí hacemos una lista combinando elementos de otras listas y elementos directos
combinada = ["inicio", *lista, "medio", *lista2, "final"]
print(combinada)


punto1 = {"x": 19, "b": "hola"}
punto2 = {"y": 20}

nuevopunto = {**punto1, "medio": "interrupcion", **punto2, "z": "chau"}
print(nuevopunto)
