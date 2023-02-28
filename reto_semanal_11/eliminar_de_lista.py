def eliminar_lista (lista, lista_a_eliminar):
    for i in lista:
        if i in lista_a_eliminar:
            lista_a_eliminar.remove(i)
    return lista_a_eliminar