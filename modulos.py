# modulos en python
# En Python, un módulo es un archivo que contiene definiciones de funciones, variables y clases, 
# así como código ejecutable. Los módulos son una forma de organizar y reutilizar el código en programas
# más grandes al dividir el código en archivos más pequeños y lógicamente separados.
# Algunas características importantes de los módulos en Python son las siguientes:

# Reutilización de código: Los módulos permiten reutilizar código en diferentes partes de un programa o incluso
# en diferentes programas. Puedes importar un módulo en cualquier lugar donde necesites utilizar sus funciones o 
#variables.

# Organización: Los módulos ayudan a organizar el código en unidades lógicas y separadas. 
# Cada módulo puede contener un conjunto relacionado de funciones y clases.

# Evitar conflictos de nombres: Los módulos evitan conflictos de nombres al proporcionar un espacio de nombres
# separado para sus definiciones. Esto significa que dos módulos pueden tener funciones o variables 
# con el mismo nombre sin causar conflicto.

# Facilita la colaboración: En proyectos colaborativos, los módulos facilitan la división del trabajo en archivos
#separados, lo que permite que diferentes desarrolladores trabajen en diferentes partes del programa.

# Ruta donde estoy ubicado y donde se ejecuta
import sys
print (sys.path)

# re.findall(pattern, string)
# Esta función busca todas las ocurrencias del patrón en la cadena de texto 
# y devuelve una lista de todas las coincidencias encontradas.

import re
text = " Mi numero de telefono es 3225709750 , El codigo del pais es +57 , Mi numero de la suerte es 25  "
result = re.findall( ' [0-9]+ ' , text )
print (result)

# re.search (pattern , string)
# Esta función busca un patrón (pattern) dentro de una cadena de texto (string) 
# y devuelve un objeto match si encuentra una coincidencia. Si no se encuentra ninguna coincidencia, devuelve None.

import re
texto = "Python es un lenguaje de programación poderoso y versátil."
# Buscar la palabra "Python" en el texto
resultado = re.search(r"Python", texto)

if resultado:
    # el método group() es utilizado en el contexto de objetos que representan coincidencias encontradas
    #  por el módulo re (expresiones regulares) o por ciertas operaciones de búsqueda de patrones. 
    # Este método se utiliza para obtener el texto de la coincidencia encontrada.
    print("Se encontró una coincidencia:", resultado.group())
else:
    print("No se encontraron coincidencias.")

# importar tiempo actual

import time
tiempo_actual = time.time()
local = time.localtime()
resultado = time.asctime()
print(resultado)

import collections
numeros = [1,1,2,1,2,1,4,5,3,3,21]
contador = collections.Counter(numeros)
print(contador)
