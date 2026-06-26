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