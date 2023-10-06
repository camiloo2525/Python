# iterables nos permite controlar la forma en que se ejecutar un iterador,
# esto nos ayuda a no ocupar tanta memoria

# <aside> ⚠️ Si vamos mas alla del rango dado se va a generar un error con el StopIteration </aside>

for i in range (1,11):
    print(i)

# iterar de forma manual
mi_iterable = iter( range(1,11))
print (mi_iterable)
print(next(mi_iterable))
print(next(mi_iterable))
print(next(mi_iterable))
print(next(mi_iterable))
print(next(mi_iterable))
print(next(mi_iterable))
print(next(mi_iterable))
print(next(mi_iterable))
print(next(mi_iterable))
print(next(mi_iterable))

