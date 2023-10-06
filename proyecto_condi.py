import random

options= ("Piedra" , "Papel" , "Tijera")

computer_wins=0
user_wins=0

rondas = 1

while True:
    print("*"*10)
    print("RONDA",rondas)
    print("*"*10)
    print("Computador gano:" , computer_wins)
    print("usuario gano:" , user_wins)

    user_option = input (" Piedra , Papel o Tijera =")

    rondas +=1

    if not user_option in options:
        print("Esa opcion no es valida")
        continue

    computer_option = random.choice(options)

    print("User option:", user_option)
    print("Computer option:" , computer_option)

    if user_option == computer_option:
        print("Empate!")
    elif user_option == "Piedra":
        if computer_option=="Tijera":
            print("Piedra gana a Tijera")
            print("User gano!")
            user_wins +=1

        else:
            print("Papel gana a Piedra")
            print("Computer gano!")
            computer_wins+=1

    elif user_option == "Papel":
        if computer_option == "Piedra":
            print("Papel gana a Piedra")
            print("Use gano")
            user_wins +=1

        else:
            print("Tijera gana a papel")
            print("Computer gano!")
            computer_wins+=1

    elif user_option == "Tijera":
        if computer_option == "Papel":
            print("Tijera gana a papel")
            print("Usuario gano")
            user_wins +=1

        else:
            print("Piedra gana a Tijera")
            print("Computer gano!")
            computer_wins+=1

    if computer_wins==2:
        print("El ganador es la computadora")
        break

    if user_wins==2:
        print("El ganador es el Usuario")
        break

    


    