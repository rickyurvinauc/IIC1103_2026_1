# Escribe tu código aquí
# Fuerza: Un entero que representa la fuerza del boxeador.
# Energía: Un entero que representa la energía de un boxeador, que se reduce con cada golpe lanzado.
# Vida: Un entero que representa la vida del boxeador, que se reduce con cada golpe recibido.
# Energia por golpe: Un entero que representa cuanta energia consume el boxeador al lanzar un golpe.

# golpe(fuerza_atacante, energia_receptor) la cual deberá 
# calcular y retornar el daño infligido por un golpe en 
# función de la fuerza del atacante que realiza el golpe, 
# y la energía del receptor de este. Especificamente, se busca que:

# from boxing import golpe

def golpe(fuerza_atacante, energia_receptor):
    danio = 0
    if energia_receptor > 60:
        danio = round(fuerza_atacante/2)
    elif energia_receptor >= 30 and energia_receptor <=60:
        danio = fuerza_atacante
    elif energia_receptor <30:
        danio = round(fuerza_atacante * 1.5)
        
    return danio

fuerza_p1 = int(input())
energia_p1 = int(input())
vida_p1 = int(input())
energia_por_golpe_p1 = int(input())

fuerza_p2 = int(input())
energia_p2 = int(input())
vida_p2 = int(input())
energia_por_golpe_p2 = int(input())

# print("f1", fuerza_p1)
# print("e1", energia_p1)
# print("v1", vida_p1)
# print("ep1", energia_por_golpe_p1)

# print("f2", fuerza_p2)
# print("e2", energia_p2)
# print("v2", vida_p2)
# print("ep2", energia_por_golpe_p2)

atacante = "p1"

while True:
    if atacante == "p1":
        if energia_p1 > 0:
            danio = golpe(fuerza_p1, energia_p1)
            # print("daniop1", danio)
            vida_p2 -= danio
            energia_p1 -= energia_por_golpe_p1
            print(f"El boxeador 1 golpea al boxeador 2, la energia del boxeador 1 ahora es {energia_p1} y la vida del boxeador 2 ahora es {vida_p2}")
        else:
            print("El boxeador 1 se quedo sin energia, no puede seguir atacando.")
            break
        if vida_p2 <= 0:
            print(f"El boxeador 1 es victorioso!")
            break
        atacante = "p2"
    elif atacante == "p2":
        if energia_p2 > 0:
            danio = golpe(fuerza_p2, energia_p2)
            # print("daniop2", danio)
            vida_p1 -= danio
            energia_p2 -= energia_por_golpe_p2
            print(f"El boxeador 2 golpea al boxeador 1, la energia del boxeador 2 ahora es {energia_p2} y la vida del boxeador 1 ahora es {vida_p1}")
        else:
            print("El boxeador 2 se quedo sin energia, no puede seguir atacando.")
            break
        if vida_p1 <= 0:
            print(f"El boxeador 2 es victorioso!")
            break
        atacante = "p1"
        
    
    

