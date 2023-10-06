mi_diccionario = {}
print(type(mi_diccionario))

mi_diccionario = {
"avion": "vuela",
"nombre": "camilo",
"apellido": "salazar",
"edad": 22
}

print(mi_diccionario)
print(mi_diccionario.items())
print(mi_diccionario.keys())
print(mi_diccionario.values())


# cantidad de palabras del diccionario
print(len(mi_diccionario))

#saber la posicion de la variable y da su significado
print(mi_diccionario["edad"])
print(mi_diccionario["avion"])

# preguntar con el .get si esta en el diccionario
print(mi_diccionario.get("valor"))

print("avion" in mi_diccionario)
print("valor" in mi_diccionario)

# eliminar palabra diccionario
del mi_diccionario["avion"]
print(mi_diccionario)
