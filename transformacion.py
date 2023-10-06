nombre = "camilo"
print(nombre)
print(type(nombre))

nombre = 12
print(nombre)
print(type(nombre))

print (" hola " + " todos ")

# transformacion entero a string con str
edad = 22
print (" Mi edad es: " + str(edad))
# si poner F (formato no nesecitamos str para convertir variables)
print ( f" mi edad es: {edad}")

# transformacion string a int
edad = input(" escribe tu edad : ")
print(type(edad))
edad = int(edad)
edad +=10
print(f" tu edad en 10 años sera: {edad}")
