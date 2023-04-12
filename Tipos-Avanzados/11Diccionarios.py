# Son conexiones de datos agrupados por llaves y valores.
# Estructura en orden { " ": , " ": }

punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto["z"])

# Aquí hay un error de indentación. La línea debe empezar en la columna 1.
print(punto)
# La clave "lala" no existe, por lo que el método devuelve None.
print(punto.get("lala"))

if "lala" in punto:
    print("encontré lala", punto["lala"])
else:
    print("lala no existe en el diccionario")

print(punto.get("x"))

print(punto.get("lala", 97))

# Para eliminar una llave incluyendo su valor
del punto["x"]
del (punto["y"])
print(punto)

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(valor)
