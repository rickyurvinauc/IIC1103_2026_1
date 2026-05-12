def contar(carton, ya_extraidos):
    contador = 0

    for extraido in ya_extraidos:

        for fila in carton:
            if extraido in fila:
                contador += 1

    return contador