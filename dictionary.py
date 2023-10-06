diccionario = {}
for i in range (1,11):
    diccionario[i]= i*2
print(diccionario)

diccionario_2 ={i: i*2 for i in range (1,5)}
print(diccionario_2)

import random
paises = ["colombia" , "paraguay", "venezuela" , "guatemala"]
poblacion = {}
for pais in paises:
    poblacion[pais] = random.randint(1,100)
print(poblacion)

poblacion2={pais:random.randint(1,100)for pais in paises}

# union de dos listas
nombres = ["milo","camilo","santi"]
edad = [12,15,18]

print(list(zip(nombres, edad)))

nuevo_diccionario = {nombres: edad for (nombres , edad) in zip (nombres , edad)}
