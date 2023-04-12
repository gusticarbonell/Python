# Codigo de creacion de calculadora automatica.

n1 = input("Ingrese su primer numero ")
n2 = input("Ingrese su segundo numero ")

n1 = int(n1)
n2 = int(n2)


suma = n1 + n2

resta = n1 - n2

multiplicacion = n1 * n2

division = n1 / n2

potencia = n1 ** n2

mensaje = f""" Para los numeros {n1}, {n2},

el resultado de la suma es {suma}.

el resultado de la resta es {resta}.

el resultado de la multiplicacion es {multiplicacion}.

el resultado de la division es {division}.

el resultado de la potencia es {potencia}.
"""

print(mensaje)
