# print (0/0)
# print (resultado)
print ("hola")

# assert para verificar si el codigo o nuestras funciones estan correctas
suma = lambda x, y : x+y
assert suma (5,5) == 10
print (suma(5,5))

print (" hola 2 ")

# crear una excepcion de no se permiten menores de edad
edad = 17
if edad < 18:
    raise Exception(" No se perimiten menores de edad ")