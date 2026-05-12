
def contar_a_recursiva(palabra):
    if len(palabra) == 0:
        return ""
    letra = palabra[0] # H
    if letra == "a":
        return 1 + contar_a_recursiva(palabra[1:])
    else:
        return contar_a_recursiva(palabra[1:])

print(contar_a_recursiva("banana")) #->  1 + (1 + (1 + 0)) = 3
# letra = H
# return contar_a_recursiva("anana") -> 1 + (1 + (1 + 0))
# 2da
# letra = a
# return 1 +contar_a_recursiva("nana") -> 1 + (1 + (1 + 0))
# 3era 
# letra = n
# return contar_a_recursiva("ana") -> 1 + (1 + 0)
# 4ta llamada 
# letra = a
# return 1 + contar_a_recursiva("na") -> 1 + (1 + 0)
# 5ta llamada
# letra = n
# return contar_a_recursiva("a") -> 1 + 0
# 6ta llmada
# letra = a
# return  1 + ""
# return ""


 