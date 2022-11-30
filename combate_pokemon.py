from random import randint
import time
vida_pikachu = 90
vida_squirtle = 80
daño_placaje = 10
daño_pistola_agua = 12
daño_burbuja = 9
daño_onda_trueno = 10
daño_bola_voltio = 11
continuar_user = True

print("Benvenido al combate pokemon, tu vas a jugar con squirtle")

while vida_squirtle>0 and vida_pikachu>0:
    print("Tienes estos ataques:")
    print("1.Placaje que inflinje {} puntos de daño".format(daño_placaje))
    print("2.Pistola de agua que inflinje {} puntos de daño".format(daño_pistola_agua))
    print("3.Burbuja que inflinje {} puntos de daño".format(daño_burbuja))
    input_user = input("Que ataque quieres realizar: 1, 2, 3 ")
    if input_user == 1:
        time.sleep(1)
        print("Se a realizado el ataque placaje")
        vida_pikachu -= daño_placaje
        print("Ahora la vida de pikachu es de {} puntos de vida".format(vida_pikachu))

    elif input_user == 2:
        time.sleep(1)
        print("Se arealizado el ataque pistola de agua")
        vida_pikachu -= daño_pistola_agua
        print("Ahora la vida de pikachu es de {} puntos de vida".format(vida_pikachu))

    elif input_user == 3:
        time.sleep(1)
        print("Se a realizado el ataque burbuja")
        vida_pikachu -= daño_burbuja
        print("Ahora la vida de pikachu es de {} puntos de vida".format(vida_pikachu))

    else:
        print("Introduce un valor valido")


    ataque = randint(1,2)
    if ataque == 1:
        time.sleep(1)
        print("Pikachu a realizado el ataque de onda trueno")
        vida_squirtle -= daño_onda_trueno
        print("Ahora tu vida es de {} puntos de vida".format(vida_squirtle))

    else:
        time.sleep(1)
        print("Pikachu a realizado el ataque de bola voltio")
        vida_squirtle -= daño_bola_voltio
        print("Ahora tu vida es de {} puntos de vida".format(vida_squirtle))