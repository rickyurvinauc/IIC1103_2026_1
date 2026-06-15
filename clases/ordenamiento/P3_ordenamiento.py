def criterio(item):
    hora = item[1][:2]
    minutos = item[1][2:]
    return hora, minutos

def encontrar_mas_temprano(actividades):
    actividades.sort(key=criterio)
    return actividades[0][-1]