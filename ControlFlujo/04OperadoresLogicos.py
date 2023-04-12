# and, or, not

# and    x > 5       y > 10      los 2 True deben ser sino False.

# OR     X > 5       Y > 10      1 True ya hace que sea True.

# NOT    Niega el resultado de la operacion.


gas = True
encendido = True

if gas and encendido:
    print("Puedes avanzar")

#############################################################

gas = False
encendido = True

if gas or encendido:
    print("Puedes avanzar")

gas = True
encendido = True

if gas or encendido:
    print("Puedes avanzar")

gas = False
encendido = True

if gas or encendido:
    print("Puedes avanzar")

#############################################################

gas = False
encendido = True

if not gas or encendido:
    print("Puedes avanzar")

#############################################################

gas = True
encendido = True
edad = 18

if gas and (encendido or edad > 17):  # Primero siempre se evalua el ()
    print("Puedes avanzar")

gas = False
encendido = True
edad = 18

if not gas and (encendido or edad > 17):  # Primero siempre se evalua el ()
    print("Puedes avanzar")


#########################################################################################################

#                         OPERADOR DE CORTO CIRCUITO

gas = False
encendido = True
edad = 18

if not gas and encendido or edad > 17:  # Primero siempre se evalua el ()
    print("Puedes avanzar")
