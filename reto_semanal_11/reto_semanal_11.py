from crear_lista import crear_lista as crear
from eliminar_de_lista import eliminar_lista as eliminar

contador_listas = int(input("Bienvenido, por favor ingrese la cantidad de listas a ingresar: "))
listas = []
for i in range(contador_listas):
    nombre_de_lista = input(f"Cómo desea llamarle a la lista número {i+1}? ")
    contador_elementos = (input(f"Ahora ingrese la cantidad de elementos de {nombre_de_lista}: "))
    lista = crear(nombre_de_lista, contador_elementos)
    listas.append(lista)
print(f"Las listas originales quedan así: {listas}")
for i in range(len(listas)-1):
    for j in range(len(listas)-1):
        if j>=i:
            eliminar(listas[j+1],listas[i])

    
print(f"Aquí se eliminan de las listas aquellos elementos que se encontraron en las listas posteriores: {listas}")