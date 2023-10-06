# Leer un txt

texto = open ("./text.txt")
#print (texto.read())

# leer linea especificas una a una

# print(texto.readline())
# print(texto.readline())
# print(texto.readline())

for linea in texto:
    print(linea)
texto.close()

with open ("./text.txt") as texto:
 for linea in texto:
    print(linea)



