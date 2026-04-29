palabras = ["hola", "mundo", "python"]
resultado = " ".join(palabras)

print(resultado)
# hola mundo python
numeros = [1, 2, 3]
for indice_n in range(0, len(numeros)):
    numeros[indice_n] = str(numeros[indice_n])

resultado = "-".join(numeros)
print(resultado)
# 1-2-3