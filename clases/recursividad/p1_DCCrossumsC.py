def validez_fila(numeros, total):
    if len(numeros) == 0:
        if total == 0:
            return True
        else:
            return False
    return validez_fila(numeros[1:],total-numeros[0])