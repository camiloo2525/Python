# funciones

def texto():
    print("hola" *2)
texto()

def texto2():
    print(" hola mi nombre es juan camilo salazar hernandez ")
texto2()

def texto3(text):
    print(text)
texto3(" juan camilo salazar hernandez ")

def nombre_funcion():
    print( " hola esto es una funcion  " )

nombre_funcion()

def suma():
    a = 5
    b = 5
    c = a + b
    print(" el resultado de la suma es: " , c)

suma()

def lista():
    lista =[" camilo " , " paola " , " baby " ]
    print(" la lista es: " ,lista)

lista()

def multi(numero1 , numero2):
    print(numero1 + numero2)
multi(5, 7)

def retorno( valor1 , valor2):
    return valor1 + valor2
resultado = retorno(10 ,5)
print(resultado)

# valores definidos
def nombres (nombre,apellido):
    print ( " hola como te llamas: " ,nombre , " y su apellido es: " ,apellido)
nombres("camilo" , "salazar")

# valores sin definir
"""
def Nombre ( nombre= "" , apellido= "" ):
    print ( " hola como te llamas: " , nombre , " y su apellido es: " , apellido)
    return input()
respuesta = Nombre ()
print (respuesta)
"""

def suman( numeroo, numeroos , numeross):
    print (numeroo + numeroos + numeross)
suman ( 25, 56, 57)

def suma_rango ():
    suma = 0
    for x in range ( 1, 10 ):
      suma +=x
    print(suma)
suma_rango()

def rango (min , max):
    print (min,max)
    su = 0
    for i in range (min , max):
     su +=i
    return su
result = rango(1,25)
print (result)

def dos_valores (valores1, valores2 ):
    return valores1 + valores2
origen = dos_valores(10,5)
print(origen)


def fun (frase):
    return frase
palabra = fun ("camilo")
print ( " El nombre de el es: " ,palabra)

# funcion calcular area de un triangulo

def triangulo (base , altura):
    area = base * altura / 2
    return area
base = int(input(" ingrese la base: "))
altura = int(input(" ingrese la altua: "))
print ( " el area del triangulo es: " ,triangulo (base,altura))

# funcion compara dos numeros y dice cual es mayor

def mayor_valor (va1, va2):
    if va1 > va2:
        mayor = va1
    else:
        mayor = va2
    return mayor

v1 = int(input(" ingrese el primer valor"))
v2 = int(input(" ingrese el segundo valor"))
print (" el mayor valor es: " ,mayor_valor(v1,v2))


def suma3 (x,y):
    print (x + y)
suma3(5,5)

def suma4 (a,b):
    return  a + b
producto = suma4 (4 , 5 )
print(producto)

"""
¿entonces return nos devuelve un valor a la variable que hemos llamado?
Exacto, has entendido bien. La declaración return en una función de Python se utiliza para devolver un valor 
calculado de vuelta al lugar desde donde se llamó la función. Puedes pensar en ello como una forma de "entregar" 
el resultado de la función a la parte del programa que la invocó.

Cuando llamas a una función que contiene una declaración return, el valor especificado después de return es
 evaluado y devuelto a la llamada de la función. Puedes asignar este valor devuelto a una variable si deseas 
 utilizarlo en tu programa.

Aquí tienes un ejemplo:
"""

def suma(c, d):
    resultado2 = c + d
    return resultado2
resultado2 = suma(3, 5)  # La función devuelve 8
print(resultado2)  # Imprime 8

def imprimir_info(nombre, edad):
    print(f"Nombre: {nombre}, Edad: {edad}")

imprimir_info(edad=30, nombre="Juan")

def info (nombres,edades):
    return nombres , edades
informacion = info ("camilo" , 23)
print(informacion)


def volumen (altura , ancho , profundidad):
    return altura * ancho * profundidad
resultado_volumen = volumen(5,5,5)
print(resultado_volumen)

def volumen2 (altura1=1 , ancho1=1 , profundidad1=1):
    return altura1 * ancho1 * profundidad1, ancho1, "hola"
resultado_volumen2, altura1 , text = volumen2(altura1=10)
print(resultado_volumen2)
print(altura1)
print(text)



