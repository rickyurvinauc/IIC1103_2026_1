nota = float(input("Ingrese una nota: "))

suma = 0
contador = 0

while nota >= 0:
    suma += nota
    contador += 1
    nota = float(input("Ingrese una nota: "))

if contador > 0:
    promedio = suma / contador
    print("El promedio es:", promedio)
else:
    print("No se ingresaron notas validas")