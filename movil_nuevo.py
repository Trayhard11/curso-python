print("Vamos a mirar que movil te va mejor entre estos moviles: \niPhone Ultra Pro Max \niPhone segunda mano \nAndroid Chino de 100€ \nGoogle pixel supercamara \nAndroid Calidad precio")
print("")
nuevo = input("¿Quieres que sea nuevo? S/N ")
if nuevo == "N":
    print("Tu movil perfecto es el iPhone de segunda mano")
else:
    iOS = input("1 si quieres iOS; 2 si quieres android: ")
    if iOS == 1:
        print("Tu movil es el iPhone Ultra Pro Max")
    else:
        camara = input("Quieres la mejor camara? S/N ")
        if camara == "S":
            print("Tu movil perfecto es el google pixel supercamara")
        else:
            precio = input("Quieres pagar lo minimo posible? S/N ")
            if precio == "S":
                print("Tu movil perfecto es el android chino de 100€")
            else:
                print("Tu movil perfecto es el Android calidad-precio")