def calcular_promedio_con_verificacion(a, b):
    """
    Versión mejorada de calcular_promedio que incluye validación de tipos.
    (Funcionalidad adicional agregada en el paso 6)
    
    Parámetros:
        a: Primer número
        b: Segundo número
    
    Retorno:
        float: Promedio de los dos números o None si hay error
    """
    try:
        return (float(a) + float(b)) / 2
    except (TypeError, ValueError):
        print("Error: Los parámetros deben ser números")
        return None

# Ejecución del programa
if __name__ == "__main__":
    ejecutar_pruebas()
    
    # Prueba de la función modificada (paso 6)
    print("\n--- PRUEBA DE FUNCIÓN MODIFICADA ---")
    print(f"Promedio con verificación (10, 20): {calcular_promedio_con_verificacion(10, 20)}")
    print(f"Promedio con verificación ('10', '20'): {calcular_promedio_con_verificacion('10', '20')}")
    print(f"Promedio con verificación ('texto', 20): {calcular_promedio_con_verificacion('texto', 20)}")