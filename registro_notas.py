# ============================================================
# SISTEMA DE REGISTRO DE NOTAS DE ESTUDIANTES
# Curso: Fundamentos de Programación - Proyecto Integrador
# ============================================================
import os

estudiantes = []  # Lista global de estudiantes


def ingresar_nota(mensaje):
    """Solicita y valida una nota entre 0 y 20."""
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 20:
                return nota
            else:
                print("   La nota debe estar entre 0 y 20. Intente de nuevo.")
        except ValueError:
            print("   Ingrese un número válido.")


def calcular_promedio(n1, n2, n3):
    """Calcula el promedio de tres notas."""
    return (n1 + n2 + n3) / 3


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


def mostrar_estudiantes():
    """Muestra la lista completa de estudiantes registrados."""
    print("\n--- LISTA DE ESTUDIANTES ---")
    if not estudiantes:
        print("  No hay estudiantes registrados aún.")
        return

    print(f"{'N°':<4} {'Nombre':<20} {'N1':>5} {'N2':>5} {'N3':>5} {'Prom':>7} {'Estado':<12}")
    print("-" * 60)
    for i, e in enumerate(estudiantes, 1):
        n = e["notas"]
        print(f"{i:<4} {e['nombre']:<20} {n[0]:>5.1f} {n[1]:>5.1f} {n[2]:>5.1f} "
              f"{e['promedio']:>7.2f} {e['estado']:<12}")


def mostrar_menu():
    """Muestra el menú principal."""
    print("\n=============================")
    print("  SISTEMA DE NOTAS")
    print("=============================")
    print("  1. Registrar estudiante")
    print("  2. Ver lista de estudiantes")
    print("  3. Salir")
    print("-----------------------------")


def main():
    """Función principal: controla el flujo del programa."""
    print("Bienvenido al Sistema de Registro de Notas")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            print("\nCerrando el programa. ¡Hasta pronto!\n")
            break
        else:
            print("Opción inválida. Ingrese 1, 2 o 3.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
