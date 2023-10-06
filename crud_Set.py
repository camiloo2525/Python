conjunto_paises = {"Colombia","Venezuela","Ecuador"}

#Para saber cuantos elementos hay en el conjunto
size = len(conjunto_paises)
print(size)

#Para saber si un elemento esta dentro del conjunto 
print("Colombia" in conjunto_paises)
print("Peru" in conjunto_paises)

#Adicionar elementos al conjunto
conjunto_paises.add("Peru")
print(conjunto_paises)

#Actualizar elementos del conjunto
conjunto_paises.update({"Argentina","Chile"})
print(conjunto_paises)

#Eliminar elemento de un conjunto
conjunto_paises.remove("Peru")
print(conjunto_paises)

#Limpiar todo el conjunto
conjunto_paises.clear()
print(conjunto_paises)
print(len(conjunto_paises))
