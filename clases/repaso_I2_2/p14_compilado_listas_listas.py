def palermo(lets, nums, pos):
    letras = [0]*len(pos)
    indice = 0
    for num in nums:
        letra = lets[num[0]][num[1]]
        letras[pos[indice]] = letra
        indice += 1
    texto = "".join(letras)
    return texto