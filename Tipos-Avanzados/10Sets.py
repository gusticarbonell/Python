# Un set es una colección de datos irrepetibles y desordenada

# De esta forma eliminamos los duplicados
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)

primer.add(5)
primer.remove(4)

# Unión de sets sin elementos duplicados " | " es una unión de sets
print(primer | segundo)

# Intersección
print(primer & segundo)

# Diferencia
print(primer - segundo)

# Diferencia simétrica
print(primer ^ segundo)

if 5 in segundo:
    print("diferencia simétrica")
