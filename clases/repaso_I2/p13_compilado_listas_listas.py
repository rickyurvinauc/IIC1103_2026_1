def dcc_en_fila(l):

    for indice_f in range(len(l)):
        d_encontrada = False
        c1_encontrada = False
        c2_encontrada = False
        for indice_c in range(len(l[0])):
            item = l[indice_f][indice_c]
            if item == "d" and d_encontrada == False:
                d_encontrada = True
                pos_inicio = [indice_f, indice_c]
            elif item == "c" and d_encontrada and c1_encontrada == False:
                c1_encontrada = True
                pos_mitad = [indice_f, indice_c]
            elif item == "c" and d_encontrada and c1_encontrada:
                c2_encontrada = True
                pos_fin = [indice_f, indice_c]
        if d_encontrada and c1_encontrada and c2_encontrada:
            break
    return [pos_inicio, pos_mitad, pos_fin]