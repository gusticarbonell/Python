animal = " CHANCHITO ESTA FELIZ "
print(animal.lower())

animal = "CHANCHITO ESTA FELIZ"
print(animal.capitalize())

animal = " CHANCHITO ESTA FELIZ "
print(animal.title())

animal1 = " chanchito esta feliz "
print(animal1.upper())

animal2 = "chanchito esta feliz"
print(animal2.strip())

animal2 = " chanchito esta feliz "
print(animal2.strip().capitalize())

print(animal)
print(animal.lstrip())
print(animal.rstrip())
animal2 = "chanchito esta feliz"


print(animal.find("FE"))
print(animal.find("ch"))  # -1 ES QUE NO LO ENCUENTRA
print(animal.replace("CH", "j"))
# find devuelve el indice de donde se encuentra e in devuelve el booleano
print("CH" in animal)
# negacion del in, busca si no se encuentra en el string
print("CH" not in animal)
