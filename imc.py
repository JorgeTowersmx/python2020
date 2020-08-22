peso = float(input("Captura tu peso"))
altura = float(input("Captura tu altura"))
#operador de potencia ** 2,2  el segundo caracter es para redondear
imc = round(peso / altura **2,2)
print("Tu indice de masa corporal es:" + str(imc))

if imc<16:
    print("Criterio de ingreso a hospital")
elif imc>=16 and imc<=17:
    print("Infrapeso")
elif imc>17 and imc<=18:
    print("Bajo peso")
elif imc>18 and imc<=25:
    print("Normal")
elif imc>25 and imc<=30:
    print("Sobrepeso")
elif imc>30 and imc<=35:
    print("Sobrepeso cronico")
elif imc>35 and imc<=40:
    print("Obesidad premorbida")
elif imc>40:
    print("Obesidad morbida")
