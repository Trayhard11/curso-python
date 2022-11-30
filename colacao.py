print("¡vamos a preparar un colacao!")
print("Vamos a la cocina")
hay_leche = input("¿Hay leche en la nevera? ")

if hay_leche == "si":
    print("Muy bien")
    hay_colacao = input("¿Hay colacao? ")
    if hay_colacao == "Si":
        print("Perfecto!")
        print("Voy a mezclar el colacao")
        print("Ya tienes el colacao")
    else:
        print("apunta comprar colacao")
else:
    print("apunta comprar colacao")
