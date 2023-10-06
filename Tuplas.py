# tupla una lista ordenada de solo lectura y finita de elementos

numeros =(1,2,3,5)
strings = ("Camilo" , "Nicolas" , "Mario","Camilo")
print(numeros)
print(numeros[0])
print(numeros[-1])
print(type(numeros))

print(strings)
print(type(strings))

# CRUD
#numeros.append(10)
print(numeros)
#numeros[1]="change"

print(strings)
#Posicion del strings
print(strings.index("Camilo"))
#Cuenta cuantas veces esta repetida la palabra
print(strings.count("Camilo"))

# convertir la tupla en lista
mi_lista = list(strings)
print(mi_lista)
print(type(mi_lista))

mi_lista[1] = "Julia"
print(mi_lista)

mi_tupla=tuple(mi_lista)
print(mi_tupla)
