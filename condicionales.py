# condicionales if y else

if True: 
    print("deberia ejecutarse")

if False:
    print("Nunca se ejecuta")


pet = input("Cuál es tu mascota favorita? ")

if pet == "perro":
    print("Los perros son lo mejor")
elif pet == "gato":
    print("Los gatos son lo mejor")
elif pet == "pez":
    print("No me gustan los peces")
else:
    print("Lo siento, no conozco esa mascota")


stock = input (" Digita el stock ")
stock = int(stock)
if stock >100 and stock <=1000:
    print(" El stock es correcto")
else:
    print(" El stock es incorecto")


condicion = 5 * 3

if condicion == 15:
    print(" se ejecuta la condicion del segundo if: " )

if condicion < 10:
    print ( " se ejecuta la tercer condicion ")


condicionales = 0

while condicionales < 30:
    print(condicionales)
    condicionales +=2
if condicionales == 30:
    print ( " si da la condicion")
else:
    print ( " no da la condicion ")
print ( " fin del programa :) ")

