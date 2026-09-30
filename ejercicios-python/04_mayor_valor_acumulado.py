# Ejercicio #4: ¿Qué lista tiene mayor valor acumulado?

list1 = [11, 45, 78, 14, 107, 55, 14]
list2 = [9, 784, 11, 22, 0, 1, 4]

acumulado1 = 0
for numero in list1:
    acumulado1 = acumulado1 + numero

acumulado2 = 0
for numero in list2:
    acumulado2 = acumulado2 + numero

print("Valor acumulado de list1:", acumulado1)
print("Valor acumulado de list2:", acumulado2)

if acumulado1 > acumulado2:
    print("list1 tiene mayor valor acumulado")
elif acumulado2 > acumulado1:
    print("list2 tiene mayor valor acumulado")
else:
    print("Ambas listas tienen el mismo valor acumulado")
