dolar_euro = 0.91
libra_euro = 1.18

tipo = int(input("Que intercanvio quieres hacer: 1 si es dolares a euros; 2 si es de euros a dolares; 3 si es de libras a euros; 4 si es de euros a libras: "))
if tipo == 1:
    print("vamos a pasar de dolares a euros")
    valor_usd_euros = input("¿Cuantos dolares tienes? ")
    print("Eso son {} euros".format(float(valor_usd_euros)*dolar_euro))
elif tipo == 3:
    print("vamos a pasar de libras a euros")
    valor_libras_euros = input("¿Cuantas libras tienes? ")
    print("Eso son {} euros".format(float(valor_libras_euros)*libra_euro))
elif tipo == 2:
    print("vamos a pasar de euros a dolares")
    valor_euros_usd = input("¿Cuantos euros tienes? ")
    print("Eso son {} dolares".format(float(valor_euros_usd/dolar_euro)))
elif tipo == 4:
    print("vamos a pasar de euros a libras")
    valor_euros_libras = input("¿Cuantos euros tienes? ")
    print("Eso son {} libras". format(float(valor_euros_libras/libra_euro)))
else:
    print("No es una respuesta valida")
