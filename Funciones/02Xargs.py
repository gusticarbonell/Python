def suma(*numeros):
    resultados = 0
    for numero in numeros:
        resultados += numero
    print(resultados)


suma(2, 5, 1)
suma(1, 6, 2, 2)
suma(5, 4, 3, 33, 10, 5)
