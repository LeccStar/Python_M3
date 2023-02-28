primera_lista = []
segunda_lista = []

def eliminar_lista (lista):
    for i in lista:
        if i in primera_lista:
            primera_lista.remove(i)
    return primera_lista

def añadir_a_lista (lista,nombre,rango):
    # return lista.append(elemento)
    for i in range(rango):
         elemento = input(f"Ingrese el elemento {i+1} de la {nombre}: ")
         lista.append(elemento)
    print(f"{nombre} completa")
    return lista

try:
    contador_primera_lista = int(input("Bienvenido, por favor ingrese la cantidad de elementos de la primera lista: "))
    contador_segunda_lista = int(input("Ahora ingrese la cantidad de elementos de la segunda lista: "))
except:
    print("Debe ingresar un número")
    exit()

añadir_a_lista(primera_lista,"Primera Lista", contador_primera_lista)
añadir_a_lista(segunda_lista,"Segunda Lista", contador_segunda_lista)

print(f"La primera lista quedó así: {primera_lista}")
print(f"La segunda lista quedó así: {segunda_lista}")

eliminar_lista(segunda_lista)
print(f"Si le quitamos a la primera lista los elementos de la segunda lista, quedaría asi: {primera_lista}")