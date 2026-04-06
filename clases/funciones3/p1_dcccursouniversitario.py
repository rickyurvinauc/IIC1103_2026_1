# Escribe tu código aquí
from dccdatos import obtener_nota, obtener_cantidad_inscritos, obtener_curso_inscrito
nombre = input()
cant_cursos = obtener_cantidad_inscritos(nombre)
nota_min = 0
mejor_nota = 0
for n_curso in range(cant_cursos):

    codigo_curso = obtener_curso_inscrito(nombre, n_curso)
    nota = obtener_nota(codigo_curso, nombre)
    if nota > mejor_nota:
        mejor_nota = nota
print(mejor_nota)
for n_curso in range(cant_cursos):
    codigo_curso = obtener_curso_inscrito(nombre, n_curso)
    nota = obtener_nota(codigo_curso, nombre)
    if nota == mejor_nota:
        print(codigo_curso)