
def incrementar(x):
    return x + 1

incrementar2 = lambda x : x+1

resultado = incrementar(10)
print (resultado)

resultado = incrementar2(20)
print(resultado)


"""
Las funciones lambda o anónimas son un tipo de funciones en Python que típicamente se definen en una línea
 y cuyo código a ejecutar suele ser pequeño.
"""

full_name = lambda name , last_name: f"su nombre es {name.title()} {last_name.title()}"
text = full_name ("camilo" , "salazar")
print(text)

# funcion sin lambdas
def suma (a,b):
    return a+b
resultado = suma (5,5)
print (resultado)

def palabra (nombre,apellido):
    return nombre + apellido
frase = palabra (" camilo " , " salazar ")
print (frase)

# funciones con lambdas
sumando = lambda u , o : u + o
multiplicacion = lambda u , o , c : u * o * c
constante = lambda : 10

print(sumando(5,7))
print(multiplicacion(5,5,5))
print(constante())

# lista con tuplas nombre - años - tiempo del credito
# la funcion sort se utiliza poara ordenar los elementos de una lista
# key = Este argumento permite especificar una función de clave que se aplicará a cada elemento antes de ordenar. 
# La función de clave debe devolver un valor que se utilizará para determinar el orden

personas = [(" juan" , 82 , 5 ) , (" camilo " , 23 , 2) , (" paola " , 24 , 3)]

print(" desordenada" ,personas)

personas.sort()
print ( " ordenana por nombre " , personas)

personas.sort(key=lambda persona: persona[1])
print(" ordenada por edad", personas)

personas.sort(key=lambda persona : persona [1] + persona[2])
print (" ordenada edad + credito " ,personas)


fruits = ["apple", "banana", "orange", "grape"]
fruits.sort()  # Ordenar en orden ascendente (alfabético)
print(fruits)  # Salida: ['apple', 'banana', 'grape', 'orange']

numbers = [10, 5, 8, 2, 7]
numbers.sort(reverse=True)  # Ordenar en orden descendente
print(numbers)  # Salida: [10, 8, 7, 5, 2]

words = ["dog", "elephant", "cat", "rhinoceros"]
words.sort(key=len)  # Ordenar por longitud de palabras
print(words)  # Salida: ['cat', 'dog', 'elephant', 'rhinoceros']

# Si prefieres crear una nueva lista ordenada sin modificar la original, puedes utilizar la función sorted() en su lugar:
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Salida: [1, 1, 2, 3, 4, 5, 9]
print(numbers)  # La lista original no se modifica
