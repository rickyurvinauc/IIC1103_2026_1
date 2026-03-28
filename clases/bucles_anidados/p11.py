suma = 0
negativo = False
num = int(input())
cero_recibido = False
while num != 0:
    if num > 0:
        print(f"SI SUMA {num}")
        suma += num
    if num < 0:
        print(f"NO SUMA {num}")
        cero_recibido =  False
        while num != 0 or num2 == 0:
            num2 = int(input())
            if num2 == 0:
                cero_recibido = True
                break
            if num2 < 0:
                num += 1
            print(f"NO SUMA {num2}")
    if cero_recibido:
        break
    num = int(input())
print("FIN")
print(suma)