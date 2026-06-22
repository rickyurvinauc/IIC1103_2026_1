def criterio(item):
    return -item[1], item[0]
def podio(tabla, continente):
    resultado = []
    for pais in tabla:
        puntaje = 10 * pais[2] + 5 * pais[3] + pais[4]
        if continente == "*":
            resultado.append([pais[0], puntaje])
        else:
            if pais[1] == continente:
                resultado.append([pais[0], puntaje])
    resultado.sort(key=criterio)
    return resultado[:3]
