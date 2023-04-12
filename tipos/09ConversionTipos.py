# x siempre es tipo string, se debe transformar a int (integer).
# str() siempre transforma el dato a string
# float() siempre transorma en un numero con , ej: 1,14 3,24
# bool() siempre transofmra a boolean lo evalua en True o False (Falsy strings vacios 0, None)

x = input("Ingrese una cadena: ")

# Imprimimos los valores booleanos de varias expresiones
print(bool(""))     # imprime False
print(bool("0"))    # imprime True
print(bool(None))   # imprime False
print(bool(" "))    # imprime True
print(bool(0))      # imprime False
