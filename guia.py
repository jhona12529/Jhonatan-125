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
