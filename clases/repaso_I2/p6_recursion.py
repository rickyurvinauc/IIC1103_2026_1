def fallado(n, ultimo):
    # Escribe tu codigo aqui
    n = str(n)
    # casp base
    if len(n) == 1:
        return -1
    if len(n) == 2:
        if n[0] == n[1]:
            return n[0]
        else:
            return -1
    if n[0] == n[1]:
        return n[1]
    else:
        return fallado(n[1:], ultimo)