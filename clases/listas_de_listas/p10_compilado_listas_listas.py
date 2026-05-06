def obtener_confirmados(respuestas):
    confirmados = []
    for resp in respuestas:
        nombre = resp[0]
        answ = resp[1]
        if answ == "si" and nombre not in confirmados:
            confirmados.append(nombre)
        elif answ == "no" and nombre in confirmados:
            confirmados.remove(nombre)
    return confirmados
