def guardar_pendientes(ruta):
    archivo = open("pendientes.txt","a")
    direcciones_sr= []
    direcciones = []
    for encomienda in ruta.entregas:
        if encomienda.entregado == False:
            if encomienda.direccion not in direcciones_sr:
                direcciones_sr.append(encomienda.direccion)
            direcciones.append(encomienda.direccion)
    resultado = []
    for direc in direcciones_sr:
        contador = 0
        for direc2 in direcciones:
            if direc == direc2:
                contador += 1
        resultado.append([direc, contador])
    for d in resultado:
        texto = f"{d[0]} - {d[1]}\n"
        archivo.write(texto)
    archivo.close()