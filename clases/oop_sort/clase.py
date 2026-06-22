lista = [
     ["4","2"], # 8
    ["1","3"], # 3
     ["3","3"], #9
    ["0","2"],# 0
]
# [ ["0","2"],["1","3"], ["4","2"], ["3","3"]]
# ordenar segun la multiplicacion de sus elementos
def criterio(item):
    return int(item[0]) * int(item[1])
    # primer_num = int(item[0])
    # segundo_num = int(item[1])
    # return primer_num * segundo_num

# lista.sort(key=criterio)
resultado = sorted(lista, key=criterio)
print(lista)

