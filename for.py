# range numero de iteracciones


#Numeros hasta el 20
for elemento in range(20):
    print(elemento)

#Numeros del 1 al 20
for elementos in range(1,21):
    print(elementos)

sum = 0
for x in range ( 1, 10 ):
    sum +=x
    print(sum)

#recorrido de la lista
mi_lista = [1,5,15,25,35]
for i in mi_lista:
    print(i)

#recorrido de la tupla
mi_tupla = ("Camilo","Paola","Paula")
for j in mi_tupla:
    print(j)

Producto = {
    "Nombre": "Pantalon",
    "Precio": 100000,
    "Stock": 90
}

for key in Producto:
    print(key,Producto[key])
for key, value in Producto.items():
    print(key,value)

personas =[
    {
        "name" : "Nicolas",
        "Edad" : 34
    },

     {
        "name" : "jader",
        "Edad" : 46
    },

     {
        "name" : "paula",
        "Edad" : 44
    }
]

for persona in personas:
    print(persona)

#solo numeros positivos
my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# Escribe tu solución 👇
for numero in my_list:
  if not numero<0:
    new_list.append(numero)

print(new_list)


lista = [3,6,9,11,15,25]

for element in lista:
    print(element)

tupla = (2,3,4,5,6,7,8)
for o in tupla:
    print(o)

conjuntos = { "colombia " , " venezuela " , " ecuador "}
for paises in conjuntos:
    print(paises)

diccionarios = {
    " primer_nombre " : " juan ",
    " segundo_nombre " : " camilo ",
    " primer_apellido " : " salazar ",
    " segundo_apellido " : " hernandez ",
    " edad " : 23,
}

for diccionario in list(diccionarios.values()):
 print(diccionario)

for elemento in diccionarios:
    print(elemento)
    if elemento == "edad":
        continue
    print(" ejecutar ")
else:
    print(" finalizado ")

print (" ejecucion ")