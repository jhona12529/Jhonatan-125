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


