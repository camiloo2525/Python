# Map La función map () ejecuta una función especifica para cada elemento en un iterable 
# y el elemento se envía a la función como un parámetro.
"""
numeros = [1,2,3,4,5]
print (type(numeros))
print (numeros)
print (numeros[0])
"""
#Agregar un nuevo numero a la lista append

numeros = [1,2,3,4,5]
numeros_v2 = []
for i in numeros:
    numeros_v2.append(i*2)

numeros_v3 = list(map(lambda i: i *2, numeros))

print (numeros)
print(numeros_v2)
print(numeros_v3)

lista = [2,3,4,5]
lista2 = [6,7,8,9]

print(lista)
print(lista2)

resultado = list(map(lambda x , y : x + y , lista , lista2))
print(resultado)

# ejemplo de map

ingredientes = ('carne', 'maiz', 'aguacate')
ingredientes_2 = ('molida', 'tacos', 'guacamole')
menu = list(map(lambda a, b: a + ' es a ' + b, ingredientes, ingredientes_2))
print(menu)