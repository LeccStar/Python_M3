def crear_lista (nombre,rango):
    lista = []
    # return lista.append(elemento)
    if rango.isdigit():
         rango = int(rango)
    else:
         rango=1
    for i in range(rango):
         elemento = input(f"Ingrese el elemento {i+1} de < {nombre} >: ")
         lista.append(elemento)
    print(f"{nombre} completa")
    return lista