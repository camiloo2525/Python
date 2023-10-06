# funcion reduce
# reduce() es una función incorporada de Python 2, que toma como argumento un conjunto de valores 
#(una lista, una tupla, o cualquier objeto iterable) y lo “reduce” a un único valor. 
# Cómo se obtiene ese único valor a partir de la colección pasada como argumento dependerá de la función aplicada.

import functools

lista = [1,2,3,4]

def acumulador (counter , item):
    print (" contador : " ,counter)
    print (" item: " ,item)
    return counter + item

resultado = functools.reduce(acumulador , lista)
print(" el resultado es: " ,resultado)

# functools.reduce: Esta función se utiliza para aplicar una función específica de manera acumulativa 
# a los elementos de un iterable, reduciéndolos a un solo valor. Antes de Python 3,
#  reduce estaba disponible como una función incorporada, pero en Python 3 se movió al módulo functools.