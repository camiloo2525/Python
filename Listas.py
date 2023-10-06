# listas cualquier tipos de datos son con corchetes almacenan datos

numeros = [1,2,3,4,5]
print(numeros)
print(type(numeros))

tasks = ["Make a dishes", " play videogames"]
print(tasks)

types =[1, True, "Hola"]
print(types)

print(numeros[0])
# devuelve el numero de veces que el numero esta en la lista
print(numeros.count(5))
print(tasks[0])
text = "Hola"

tasks[0]="watch platzi courses"
print(tasks)

tasks[0] = "do the dishes"
print(tasks)

print(numeros[:3])
print(True in types)
print("Hola" in types)

# Crud crear, leer, actualizar y eliminar

numeros = [1,2,3,4,5]
print(numeros[1])

#Actualizar el ultimo numero de nuestra lista
numeros[-1]=10
print(numeros)

#Agregar un nuevo numero a la lista
numeros.append(700)
print(numeros)

#Insertar elementos
numeros.insert(0,"hola")
print(numeros)

numeros.insert(3,"change")
print(numeros)

#Fusionar lista
tareas =["todo1","todo2","todo3"]
nueva_lista= numeros + tareas
print(nueva_lista)

#Actualizar lista
index=nueva_lista.index("todo2")
nueva_lista[index] ="todo changed"
print(nueva_lista)

#Eliminar elementos de la lista
nueva_lista.remove("todo1")
print(nueva_lista)

#Eliminar ultimo elemento de la lista
nueva_lista.pop()
print(nueva_lista)

#Eliminar primer elemento de la lista
nueva_lista.pop(0)
print(nueva_lista)

#Poner la lista alreves
nueva_lista.reverse()
print(nueva_lista)

#Ordenar arreglos de numeros
numeros_a =[1,4,6,3]
numeros_a.sort()
print(numeros_a)

#Ordenar arreglos de strings
Strings = ["re","ab","qw"]
Strings.sort()
print(Strings)