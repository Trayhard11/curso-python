from random import randint
import time, os
VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90
vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE
TAMAÑO_BARRA = 20
daño_placaje = 10
daño_pistola_agua = 12
daño_burbuja = 9
daño_onda_trueno = 10
daño_bola_voltio = 11
continuar_user = True

print("Benvenido al combate pokemon, tu vas a jugar con squirtle")

while vida_squirtle>0 and vida_pikachu>0:
    print("")
    print("Las barras de vidas acuales son:")

    barra_vida_pikachu = int(vida_pikachu * TAMAÑO_BARRA / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{} ({}/{})]".format("*" * barra_vida_pikachu, " " * (TAMAÑO_BARRA-barra_vida_pikachu), vida_pikachu, VIDA_INICIAL_PIKACHU))

    barra_vida_squirtle = int(vida_squirtle * TAMAÑO_BARRA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:   [{}{} ({}/{}]".format("*" * barra_vida_squirtle, " " * (TAMAÑO_BARRA - barra_vida_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE))
    time.sleep(1)
    print("")
    print("Tienes estos ataques:")
    print("1.Placaje que inflinje {} puntos de daño".format(daño_placaje))
    print("2.Pistola de agua que inflinje {} puntos de daño".format(daño_pistola_agua))
    print("3.Burbuja que inflinje {} puntos de daño".format(daño_burbuja))
    print("4.No hacer nada")
    input_user = int(input("Que ataque quieres realizar: 1, 2, 3, 4 "))
    if input_user == 1:
        time.sleep(1)
        print("")
        print("Se a realizado el ataque placaje")
        vida_pikachu -= daño_placaje
        if vida_pikachu <= 0:
            vida_pikachu = 0
        else:
            print("")
            print("Ahora la vida de pikachu es de {} puntos de vida".format(vida_pikachu))

    elif input_user == 2:
        time.sleep(1)
        print("")
        print("Se arealizado el ataque pistola de agua")
        vida_pikachu -= daño_pistola_agua
        if vida_pikachu <= 0:
            vida_pikachu = 0
        else:
            print("")
            print("Ahora la vida de pikachu es de {} puntos de vida".format(vida_pikachu))

    elif input_user == 3:
        time.sleep(1)
        print("")
        print("Se a realizado el ataque burbuja")
        vida_pikachu -= daño_burbuja
        if vida_pikachu < 0:
            vida_pikachu = 0
        else:
            print("")
            print("Ahora la vida de pikachu es de {} puntos de vida".format(vida_pikachu))
    else:
        time.sleep(1)
        print("")
        print("No se a realizado ningun ataque")


    ataque = randint(1,2)
    if ataque == 1:
        time.sleep(1)
        print("")
        print("Pikachu a realizado el ataque de onda trueno")
        vida_squirtle -= daño_onda_trueno
        if vida_squirtle < 0:
            vida_squirtle = 0
        print("")
        print("Ahora tu vida es de {} puntos de vida".format(vida_squirtle))

    else:
        time.sleep(1)
        print("")
        print("Pikachu a realizado el ataque de bola voltio")
        vida_squirtle -= daño_bola_voltio
        if vida_squirtle < 0:
            vida_squirtle = 0
        print("")
        print("Ahora tu vida es de {} puntos de vida".format(vida_squirtle))
    time.sleep(0.5)
    os.system('cls')

print("")
print("Las barras de vidas finales son:")

barra_vida_pikachu = int(vida_pikachu * TAMAÑO_BARRA / VIDA_INICIAL_PIKACHU)
print("Pikachu:    [{}{} ({}/{})]".format("*" * barra_vida_pikachu, " " * (TAMAÑO_BARRA - barra_vida_pikachu), vida_pikachu, VIDA_INICIAL_PIKACHU))

barra_vida_squirtle = int(vida_squirtle * TAMAÑO_BARRA / VIDA_INICIAL_SQUIRTLE)
print("Squirtle:   [{}{} ({}/{}]".format("*" * barra_vida_squirtle, " " * (TAMAÑO_BARRA - barra_vida_squirtle), vida_squirtle, VIDA_INICIAL_SQUIRTLE))