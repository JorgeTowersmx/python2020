peso = float(input("Captura tu peso"))
altura = float(input("Captura tu altura"))
#operador de potencia ** 2,2  el segundo caracter es para redondear
imc = round(peso / altura **2,2)
print("Tu indice de masa corporal es:" + str(imc))

if imc<16:
    print("Criterio de ingreso a hospital")
elif imc
