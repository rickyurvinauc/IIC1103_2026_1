def max_disponibilidad(persona):
    max_valor = 0
    contador = 0
    indice = 0
    indice_max = 0
    for item in persona:
        if item == "X":
            contador += 1
        else:
            if contador > max_valor:
                max_valor = contador
                indice_max = indice
            contador = 0
        indice += 1
    if item == "X" and  contador > max_valor:
        max_valor = contador
        indice_max = indice
    return [indice_max-max_valor, indice_max-1]