#Jorge Torres
#21 Agosto 2020
#Escribir un programa que ayude al usuario a contar su cambio. 
#Deberá preguntar cuántas monedas de 10 pesos tiene, cuantas de 5, 2, 1, 	50 centavos, 20 centavos y 10 centavos.
#El programa deberá decir cuánto dinero 	tiene en pesos

Moneda10 = int(input("Cuantas monedas de 10 pesos tienes?"))
Moneda5 = int(input("Cuantas monedas de 5 pesos tienes?"))
Moneda2 = int(input("Cuantas monedas de 2 pesos tienes?"))
Moneda1 = int(input("Cuantas monedas de 1 pesos tienes?"))
Moneda50c = int(input("Cuantas monedas de 50 centavos tienes?"))
Moneda20c = int(input("Cuantas monedas de 20 centavos tienes?"))
Moneda10c = int(input("Cuantas monedas de 10  centavos tienes?"))

Moneda10t = Moneda10 * 10
Moneda5t = Moneda10 * 5
Moneda2t = Moneda10 * 2
Moneda1t = Moneda10 * 1
Moneda50ct = Moneda50c * 0.50
Moneda20ct = Moneda20c  * 0.20
Moneda10ct = Moneda10c * 0.10

TotalDinero = Moneda10t+Moneda5t+Moneda2t+Moneda1t+Moneda50ct+Moneda20ct+Moneda10ct

print("Dinero", TotalDinero ,"pesos mexicanos")
