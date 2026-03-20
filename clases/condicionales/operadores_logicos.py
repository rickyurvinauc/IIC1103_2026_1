anio = int(input("Ingresa un anio: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El anio ",anio, "es bisiesto.")
else:
    print("El anio ", anio, " no es bisiesto.")