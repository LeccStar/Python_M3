import matplotlib.pyplot as plt

rango_inicio = int(input("¡Hola!, esta es una graficadora de ventas, para comenzar, define el año con el que empezarás a registrar: "))
rango_final = int(input("Ahora introduce el último año a graficar: "))
ventas ={}
for i in range(rango_final-rango_inicio+1):
    ventas[str(rango_inicio+i)] = int(input(f"Venta del año {rango_inicio+i}: "))

print(ventas)
plt.plot(ventas.keys(),ventas.values())
plt.xlabel('Año')
plt.ylabel('Ventas')
plt.title('Ventas por año de la empresa')
plt.show()