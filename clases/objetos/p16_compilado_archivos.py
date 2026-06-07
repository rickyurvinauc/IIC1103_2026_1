from funciones import leer_archivos
informacion = leer_archivos()
aprobados = open("aprobados.csv","a")
reprobados = open("reprobados.csv","a")
for estudiante in informacion:
    rut = estudiante[0]
    nombre = estudiante[1]
    puntaje = int(estudiante[2])
    texto = f"{rut},{nombre},{puntaje}\n"
    if puntaje >= 20:
        aprobados.write(texto)
    else:
        reprobados.write(texto)
aprobados.close()
reprobados.close()