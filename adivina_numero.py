import random
ganar = False
numero = int(random.randint(0, 10))
print(numero)
print("He pensado un numero del 0 al 10, intenta adivinar qual es")
while ganar == False:
    intento = int(input("¿Que numero he pensado? "))
    if intento == numero:
        print("muy bien lo has adivinado")
        ganar = True
    if intento != numero:
        print("ese no era mi numero, vuelve a intentarlo")
        ganar = False