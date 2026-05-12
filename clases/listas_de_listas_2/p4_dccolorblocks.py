def es_posible_insertar(tablero, pieza):
    for pie in pieza:
        pos_x = pie[0]
        pos_y = pie[1]
        pos_tablero = tablero[pos_x][pos_y]
        if pos_tablero != 0:
            return False
    return True