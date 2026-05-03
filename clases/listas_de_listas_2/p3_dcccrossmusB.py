def borrar_col(tablero, c):
    total = tablero[0][c]
    for indice_f in range(1, len(tablero)):
        numero = tablero[indice_f][c]
        if numero > total:
            tablero[indice_f][c] = 0
    return tablero