# Escribe una funcion que reciba un nombre de un archivo .csv
# y permita actualizar la nota final segun todas las notas
# la nota final se calcula como el promedio de todos los sets

# leer el archivo
# obtener los datos en una lista
# construir una lista de listas con los datos
# modifico esta lista
# guardo la lista en el arhcivo

def modificar_notas(nombre):
    archivo = open(nombre,"r")
    contenido = archivo.readlines()
    cabecera = contenido[0]
    notas = contenido[1:]
    archivo.close()
    lista_listas = []
    for linea in notas:
        datos = linea.strip().split(",")
        notas_sets = datos[2:] # ["600","600","600","600","600"]
        suma = 0
        for nota in notas_sets:
            suma += int(nota)
        promedio = suma / len(notas_sets)
        datos[1] = str(promedio)
        lista_listas.append(datos)
    archivo = open(nombre, "w")
    # archivo.writelines(lista_listas)
    archivo.write(cabecera)
    for alumno in lista_listas:
        texto = ",".join(alumno)
        texto = texto + "\n"
        archivo.write(texto)
    archivo.close()
 
modificar_notas("notas.csv")