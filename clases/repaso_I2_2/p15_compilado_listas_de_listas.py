def palermo_pro(lets, mensaje):
    texto = ""
    for letras in mensaje:
        letra1 = letras[0]
        letra2 = letras[1]
        pos_letra1 = []
        pos_letra2 = []
        for indice_f in range(len(lets)):
            fila = lets[indice_f]
            if letra1 in fila:
                col_letra1 = fila.index(letra1)
                fila_letra1 = indice_f
            if letra2 in fila:
                col_letra2 = fila.index(letra2)
                fila_letra2 = indice_f
            if pos_letra1 != [] and pos_letra2 != []:
                letra_1_encontrada = lets[fila_letra1][col_letra2]
                letra_2_encontrada = lets[fila_letra2][col_letra1]
                texto += letra_1_encontrada+letra_2_encontrada
                break
    return texto