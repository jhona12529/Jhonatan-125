import os
estudiantes = []  # Lista global de estudiantes
def determinar_estado(promedio):
    """Retorna 'Aprobado' si el promedio es >= 11, caso contrario 'Desaprobado'."""
    return "Aprobado" if promedio >= 11 else "Desaprobado"


def registrar_estudiante():
    """Registra un nuevo estudiante con sus notas."""
    print("\n--- REGISTRAR ESTUDIANTE ---")
    nombre = input("Nombre del estudiante: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    nota1 = ingresar_nota("   Nota 1: ")
    nota2 = ingresar_nota("   Nota 2: ")
    nota3 = ingresar_nota("   Nota 3: ")

    promedio = calcular_promedio(nota1, nota2, nota3)
    estado = determinar_estado(promedio)

    estudiante = {
        "nombre": nombre,
        "notas": [nota1, nota2, nota3],
        "promedio": promedio,
        "estado": estado
    }
    estudiantes.append(estudiante)

    print(f"\n {nombre} | Promedio: {promedio:.2f} | {estado}")
