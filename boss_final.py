from random import randint
tener_palo = False
ganar = "Has ganado el juego"

print("Bienvenido al juego de la mazmorra")
print("Tienes dos opciones 1-> Una puerta | 2-> Una trampilla del suelo")
puerta = int(input("Â¿Que escoges? "))
if puerta == 1:
    print("Te encuentras con un guardia, para intentar salvarte puede: 1-> Hacerte el dormido | 2-> Escapar corriendo")
    correr = int(input("Â¿Que escoges? "))
    if correr == 1:
        print("Por hacerte el dormido te ha matado")
        print("Has perdido")
        print("___________")
    else:
        print("Gracias a salir corriendo te has salvado")
        print(ganar)
        print("_"*len(ganar))
else:
    print("Te has encontrado un palo pesado, pero podria ser util en el futuro")
    palo = int(input("1-> Coges el palo | 2-> No coges el palo "))
    if palo == 1:
        print("Has recogido el palo")
        tener_palo = True
    else:
        print("Has dejado el palo donde estava")
        tener_palo = False

    print("Sigues el camino y te encuentras una rata gigante que te pregunta:")
    num = randint(1, 100)
    respuesta = int(input("Â¿Cuanto es 13x{} ".format(num)))
    if respuesta == 13*num:
        print("Por acertar has muerto porque a la rata no le gustan los listillos")
    else:
        print("Como a la rata no le gustan los listillos te has salvado, pero antes de que te vayas te pregunta si tienes un palo pesado")
        if tener_palo == True:
            print("Tu le contestas que si")
            print("Como tienes el palo te deja pasar y te salvas")
            print(ganar)
            print("_"*len(ganar))
        else:
            print("Tu le contestas que no")
            print("Por no tener el palo te mata")
            print("Has perdido")
            print("___________")