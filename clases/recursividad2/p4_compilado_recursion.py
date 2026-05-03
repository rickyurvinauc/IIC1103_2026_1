def contar_valeotro(chocolates):
    if chocolates < 3 :
        return 0
    canjes = chocolates // 3
    sobra = chocolates - (canjes*3)
    chocolates = canjes+sobra
    return canjes + contar_valeotro(chocolates)