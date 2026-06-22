from funciones import estaciones_comunes
def criterio(item):
    return item[1], item[0]

def k_menos_conectadas(metro, k):
    estaciones = estaciones_comunes(metro)
    if len(estaciones) == 0:
        resultado = []
        for est in metro:
            resultado.append(est[0])
        resultado.sort()
        return resultado[:k]
    lineas_sin_r = []
    todas_lineas = []
    for estacion in estaciones:
        for linea in estacion[1]:
            if linea not in lineas_sin_r:
                lineas_sin_r.append(linea)
            todas_lineas.append(linea)
    resultado = []
    for linea in lineas_sin_r:
        contador = 0
        for linea2 in todas_lineas:
            if linea == linea2:
                contador += 1
        resultado.append([linea, contador])
    resultado.sort(key=criterio)
    res2 = []
    for item in resultado:
        res2.append(item[0])
    return res2[:k]