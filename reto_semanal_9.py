
bucle_infinito = ""

def letras_del_alfabeto(msg):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    abecedario_mas1 = "bcdefghijklmnñopqrstuvwxyza"
    abecedario_menos1 = "zancdefghihjlmnñopqrstuvwxy"
    tabla = str.maketrans(abecedario, abecedario_mas1)
    tabla2 = str.maketrans(abecedario, abecedario_menos1)

    msg = msg.lower()
    msg1 = msg.translate(tabla)
    msg2 = msg.translate(tabla2)
    print(f"Más una letra: {msg1} Menos una letra: {msg2}")

while bucle_infinito != "alto":
    advertencia = print("Estás en un bucle infinito, para detenerlo solo debes escribir: ' alto '")
    bucle_infinito = input("Introduca el mensaje: ")
    if bucle_infinito == "alto":
        break
    letras_del_alfabeto(bucle_infinito)
