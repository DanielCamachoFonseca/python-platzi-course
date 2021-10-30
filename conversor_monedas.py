#Pesos colombianos a dolares
pesos = float(input("¿Cuantos pesos colombianos tienes?: "))
valor_dolar = 3760
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")

#dolares a pesos colombianos
usd = float(input(" ¿Cuantos dolares tienes? "))
valor_dolar = 3760
pesos_colombianos = usd * valor_dolar
pesos_colombianos = round(pesos_colombianos, 1)
pesos_colombianos = str(pesos_colombianos)
print("Tienes $" + pesos_colombianos + " pesos")