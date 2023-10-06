items = [
    {
        " producto " : " camisa " ,
        " precio " : 80000 ,
    },

    {
        " producto " : " pantalon " ,
        " precio " : 110000
    },

    {
        " producto " : " zapatos " ,
        " precio " : 200000
    }

]
print(type(items))

productos = list ( map ( lambda item: item [" producto " ] , items ) )
print(productos)

precios = list ( map ( lambda item: item [" precio " ] , items ) )
print(precios)

def impuesto (item):
    nuevo_item = item.copy()
    nuevo_item[ " impuesto " ] = nuevo_item [ " precio " ] * .19
    return nuevo_item

nuevos_itemss = list(map( impuesto , items ))

print (nuevos_itemss)
print (items)


# utilizamos map con dos numeros

def multiplicacion (numbers):
    return list(map(lambda x: x *2, numbers))
numbers = [1,2,3,4]
result = multiplicacion(numbers)
print(result)

def multiplicaciones (numero):
    return list(map(lambda x: x *2, numero))
numero = [-1,-1,-3,-4]
resultados = multiplicaciones(numero)
print(resultados)

def filter_by_length(words):
   # Escribe tu solución 👇
   return list(filter(lambda words: len (words)>=4 , words))

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)

numeros = [1,2,3,4,5]
nuevos_numeros = list(filter( lambda x: x % 2 == 0 , numeros))
print (numeros)
print (nuevos_numeros)