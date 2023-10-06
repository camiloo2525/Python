persona = {

"nombre": "camilo",
"apellido": "salazar",
"programacion": ["python" , "javascript"],
"edad": 22
}
print(persona)

#Actualizar los nombres y edades con strings y numeros

persona["nombre"] = "juan"
persona["edad"] -= 2
print(persona)

#agregar mas elementos

persona["programacion"].append("Go")
print (persona)

#del delete sirve para eliminar registros

del persona ["apellido"]
persona.pop("age")

print(persona)

#items nos agrupa la tupla
print("items")
print(persona.items())

#devuelve solo las llaves
print("keys")
print(persona.keys())

#devuelve los valores
print("values")
print(persona.values())

#1.Agregar un nuevo elemento al diccionario con la llave "twitter" y el valor "@nicobytes".
#2.Actualizar el valor del elemento con la llave "name" con el valor "Felipe".
#3.Eliminar el elemento del diccionario con la llave "age".
#4.Imprimir una lista con las llaves del diccionario.
#5.Imprimir una lista con los valores del 

person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

# Escribe tu solución 👇
person["twitter"] = "@nicobytes"
person["name"]= "Felipe"
del person["age"]
print(list(person.keys()))
print(list(person.values()))
print(person)