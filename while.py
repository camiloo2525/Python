# while ciclos significa mientras

counter = 0

while counter<10:
    counter +=1
    print(counter)


counter = 0

#Break instruccion forzada de rompér un ciclo

while counter < 20:
    counter+=1
    if counter==15:
        print(" se detiene ")
        break
    print(counter)


#Numeros del 1 al 20

counter=0
while counter<20:
    counter+=1
    print(counter)

#solo nos ejecuta del 15 al 20

counter=0
while counter<20:
    counter+=1
    if counter <15:
        continue
    print(counter)










