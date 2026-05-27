def horarios_comunes(integrantes):
    lista = []
    for columna in range(len(integrantes[0])):
        estado = True
        for fila in range(len(integrantes)):
            item = integrantes[fila][columna]
            if item == "-":
                estado = False
                break
        if estado:
            lista.append(columna)

    return lista