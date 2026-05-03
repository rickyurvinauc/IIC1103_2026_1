def descifrar_rec(letras, instrucciones):
    if len(instrucciones) == 0:
        return []
    accion = instrucciones[0]
    cantidad = instrucciones[1]
    if accion == "agregar":
        return letras[0:cantidad] + descifrar_rec(letras[cantidad:], instrucciones[2:])
    else:
        return descifrar_rec(letras[cantidad:], instrucciones[2:])