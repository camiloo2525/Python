
print (" hello world ")
print (" hola mundo ")

# variable con numero
numero = 23
numeros = 2023

# variable con string
palabra = "juan"
nombre_juan = " camilo "

# salto de linea
salto = " Este es un mensaje \n con salto de linea " 
print(salto)

# salto de tabulacion
salto2 = " \t Este es un mensaje  con tabulacion " 
print(salto2)

# salto escapado
salto3 = " \t Este es un mensaje \n escapado " 
print(salto3)

# cuenta las letras que almacena la variable
print(len(palabra))

#almacenano valores con variables
print (" el primer nombre de camilo es: " , palabra)
print (" su edad es :" , numero)

# numeros
numero1 = 25
numero2 = 34
numero3 = 67
palabraNombre= ( " camilo ")

#suma

suma = numero1 + numero2 + numero3
print(" El resultado de la sumas es: " , suma)

# resta

resta = numero1 - numero2 - numero3
print( " El resultado de la resta es: " , resta)

# multiplicacion

multiplicacion = numero1 * numero2 * numero3
print( "El resultado de la multiplicacion es: " ,multiplicacion)

# division 

division = numero1 / numero2 / numero3
print ( " El resultado de la division es: " ,division)

# exponenciacion

exponenciacion = (2 ** 5)
print ( " El resultado de la exponenciacion es: " ,exponenciacion)

# residuo de division

residuo_division = (25 % 5)
print ( " El residuo de la division es: " ,residuo_division)

# que tipo de dato es la variable

print (type(suma))
print (type(palabra))

# input para preguntar

pregunta = input (" Cuantos años tienes")
print (" Su edad es: " , pregunta)

pregunta2 = input (" Digite el numero de cedula: " )
print (" Su numero de cedula es: " , pregunta2)

# frases
palabra1 = " juan "
palabra2 = " camilo "
palabra3 = " salazar "
palabra4 = " hernandez "

frase = f" Hola mi primer nombre es: {palabra1} , mi segundo nombre es: {palabra2} , mi primer apellido es: {palabra3} , mi segundo apellido es: {palabra4}"
print(" La frase es: " ,frase)

# condicionales

a = 25

a = int(input(" Que numero empieza por dos y termina en 5"))
if a == 25:
    print(" Si Es 25 ")
else:
    print ( " No es el numero correcto ")

b = "hola"

b=str(input(" Con que palabra se saluda a una persona:"))
if b == "hola":
    print (" Si Es la palabra hola ")
else:
    print (" No es la palabra correcta para saludar a una persona ")


c = int(input(" Cual es la edad de camilo: "))
if c == 23:
    print (" Su edad es 23")
else:
    print (" su edad no es 23")

# booleanos

es_feo = True
print(es_feo)

es_lindo = False
print(es_lindo)

es_lindo = not es_lindo
print(es_lindo)

es_alto = True
print(es_alto)

es_alto= str(input(" ¿El es alto? : "))
if es_alto == "alto":
    print(" El es una persona alta ")
else:
    print(" El no es una persona alta ")

# comparativos

#mayor
print (1>2)
print (2>1)

#mayor igual
print (1>=2)
print (2>=1)

#igual
print (2==2)

#menor
print (1<2)
print (3<2)

#menor igual
print (1<=2)
print (3<=2)

#diferencia
print (1!=2)
print (2!=2)

# operador and significa Y

print ("And")
print ("True and True =>", True and True )
print ("True and False =>", True and False )
print ("False and True =>", False and True )
print ("False and False =>", False and False )

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

stock = input("Ingrese el numero de stock =>")
stock = int(stock)
print (stock>=100 and stock <=1000)

# operador Or significa o

print ("OR")
print ("True or True =>", True or True )
print ("True or False =>", True or False )
print ("False or True =>", False or True )
print ("False or False =>", False or False )

role = input(" ¿ digite el rol =>")
print (role =="admin" or role == "seller" )

# input para hacer operaciones

numero10=0
numero20=0
numero30=0

print (" Digite el numero 1 ")
numero10 = int(input())

print (" Digite el numero 2 ")
numero20 = int(input())

print (" Digite el numero 3 ")
numero30 = int(input())

operacion = numero10 + numero20 + numero30

print( " El resultado de la operacion es: " ,operacion)

# ciclo while

# numeros del 1 al 25

numero = 0
while numero<25:
    numero+=1
    print(numero)

# ciclo for

# numeros hasta el 20

for elemento in range(20):
    print(elemento)

#Numeros del 1 al 20
for elementos in range(1,21):
    print(elementos)


# listas cualquier tipos de datos almacenan datos se usa con corchetes 
# son ordenadas y mutables permiten duplicados

nombres_estudiantes = ["juan","camilo","paola","isabel"]
print (" Los estudiantes son: " ,nombres_estudiantes)
# sabaer la posicion del array
print(nombres_estudiantes[0])
print(nombres_estudiantes[1])
print(nombres_estudiantes[2])
print(nombres_estudiantes[3])

mezcla = ["hola",1,"todos",2]
print (mezcla)

# tuplas se inician con parentesis son ordenadas la diferencia con la lista es que 
# no puede ser modificada directamente, ordenados y inmutables , permite duplicados

tupla = ("azul",1)
print(tupla)
print(tupla[0])

# arrays permite almacenar datos en un mismo conjunto , se abre en corchetes

matriz = [1,2,3]
print(matriz)
print(matriz[0])

matriz_2 = [[0,1,2],[3,4,5],[6,7,8],[9,"w","a"]]
print(matriz_2)
print(matriz_2[2])

# Los sets o conjuntos en Python son una estructura de datos usada para almacenar 
# elementos de una manera similar a las listas, pero con ciertas diferencias.
# no son ordenados, puede contener diferentes datos , son inmutables, sin repetir datos

set_paises = {"colombia" , "mexico" , "bolivia"}
print(set_paises)

set_numeros = {1,2,3,4,5}
print(set_numeros)

set_tipos = {1,"hola",False,25.25}
print(set_tipos)

# diccionarios coleccion de elementos forma clave valor se encierra en llaves
#  son ordenados , cualquier tipo de dato , y son mutables , sin repetir datos

mi_diccionario = {
"avion": "vuela",
"nombre": "camilo",
"apellido": "salazar",
"edad": 22
}
print(mi_diccionario)

# declarar variables en una misma linea de codigo
nombre , apellido , edad = " juan " , " salazar " , 23

# manera de hacer un texto con format buenas practicas
print ( " Mi nombre es: {} {} y mi edad es {} ".format(nombre,apellido,edad))
print ( " Mi nombre es: %s %s y mi edad es %s " %(nombre,apellido,edad))

# condicionale con while 

condicionales = 0

while condicionales < 30:
    print(condicionales)
    condicionales +=2
if condicionales == 30:
    print ( " si da la condicion")
else:
    print ( " no da la condicion ")

print ( " fin del programa ")

# funciones

# funcion sin retorno

def my_function (val1 ,val2): # nombrar funcion \ se asigna parametros
    print (val1 + val2) # imprimo los dos parametros
my_function(4,4) # imprimo la funcion

# funcion con reetorno

def retonar (num1 , num2): #: retornar nombre funcion\ (num1,num2): parametros que se le da a la funcion
    return num1 * num2 # return retorna los valores de los parametros
product = retonar(5,5) # creo variable product\ nombre de la funcion y valores a los parametros
# ahora product toma los valores de los parametros
print(product) # imprimir funcion

# funciones lambdas

sumas = lambda o , u : o + u
print(sumas(5,7))

multiplicaciones = lambda a , b , c : a * b * c
print(multiplicaciones(5,5,5))

constantes = lambda : 10
print(constantes())

# funciones con orden superior

# upper convierte de minuscula a mayuscula
# lower convierte de mayuscula a minuscula

def gritar(text):
	return text.upper()
	
def silencio(text):
	return text.lower()
	
def saludo(func):
	# almacenar la función en una variable
	conversacion = func("Hi, I am created by a function \
	passed as an argument.")
	print(conversacion)
	
saludo(gritar)
saludo(silencio)

# otro ejemplo

def suma (x,y):
	return x+y

def resta (a,b):
	return a-b

def resultado(func):
	operacion = func(7,5)
	print(operacion)

resultado(suma)
resultado(resta) 

# funciones con lambdas
sumando = lambda u , o : u + o
multiplicacion = lambda u , o , c : u * o * c
constante = lambda : 10

print(sumando(5,7))
print(multiplicacion(5,5,5))
print(constante())

# Map La función map () ejecuta una función especifica para cada elemento en un iterable 
# y el elemento se envía a la función como un parámetro.

lista = [2,3,4,5]
lista2 = [6,7,8,9]

print(lista)
print(lista2)

resultado = list(map(lambda x , y : x + y , lista , lista2))
print(resultado)

def multiplicacion (numbers):
    return list(map(lambda x: x *2, numbers))
numbers = [1,2,3,4]
result = multiplicacion(numbers)
print(result)

# ejemplo
ingredientes = ('carne', 'maiz', 'aguacate')
ingredientes_2 = ('molida', 'tacos', 'guacamole')
menu = list(map(lambda a, b: a + ' es a ' + b, ingredientes, ingredientes_2))
print(menu)

# filter 
# devuelve un valor que esta siendo iterado de la cual su resultado será el valor que se esta buscando en el filter

def filter_by_length(words):
   # Escribe tu solución 👇
   return list(filter(lambda words: len (words)>=4 , words))

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)

# funcion reduce
# reduce() es una función incorporada de Python 2, que toma como argumento un conjunto de valores 
#(una lista, una tupla, o cualquier objeto iterable) y lo “reduce” a un único valor. 
# Cómo se obtiene ese único valor a partir de la colección pasada como argumento dependerá de la función aplicada.

# functools.reduce: Esta función se utiliza para aplicar una función específica de manera acumulativa 
# a los elementos de un iterable, reduciéndolos a un solo valor. Antes de Python 3,
#  reduce estaba disponible como una función incorporada, pero en Python 3 se movió al módulo functools.

import functools

lista = [1,2,3,4]

def acumulador (counter , item):
    print (" contador : " ,counter)
    print (" item: " ,item)
    return counter + item

resultado = functools.reduce(acumulador , lista)
print(" el resultado es: " ,resultado)

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