#Unir dos conjuntos
Conjunto_A = {"Colombia","Venezuela","Ecuador","Chile"}
Conjunto_B = {"Peru","Chile"}

Conjunto_Resultado = Conjunto_A.union(Conjunto_B)
print(Conjunto_Resultado)
print(Conjunto_A | Conjunto_B )

#Interseccion conjunto

Conjunto_Resultado=Conjunto_A.intersection(Conjunto_B)
print(Conjunto_Resultado)
print(Conjunto_A & Conjunto_B)

#Diferencia conjunto Resta del conjunto A-B quitando el elmento de B en A

Conjunto_Resultado=Conjunto_A.difference(Conjunto_B)
print(Conjunto_Resultado)
print(Conjunto_A-Conjunto_B)

#Diferencia simetrica sin tener en cuenta los elementos repetidos de los dos conjuntos
Conjunto_Resultado = Conjunto_A.symmetric_difference(Conjunto_B)
print(Conjunto_Resultado)
print(Conjunto_A ^ Conjunto_B)


