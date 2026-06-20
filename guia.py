# Importación de funciones desde el módulo externo
from utils import mostrar_bienvenida, calcular_promedio, validar_email, sumar_numeros
def ejecutar_pruebas():
    """
    Función principal que ejecuta todas las pruebas del sistema.
    """
    # 1. Mostrar bienvenida
    mostrar_bienvenida()
    
    # 2. Probar función de promedio
    print("\n--- PRUEBA DE PROMEDIO ---")
    num1 = 8
    num2 = 4
    resultado_promedio = calcular_promedio(num1, num2)
    print(f"El promedio de {num1} y {num2} es: {resultado_promedio}")
    
    # 3. Probar función de validación de email
    print("\n--- PRUEBA DE VALIDACIÓN DE EMAIL ---")
    emails_prueba = [
        "usuario@dominio.com",
        "usuario@dominio",
        "usuariodominio.com",
        "usuario@dominio.c"
    ]
    
    for email in emails_prueba:
        resultado = validar_email(email)
        print(f"Email: '{email}' -> {'VÁLIDO' if resultado else 'INVÁLIDO'}")
    
    # 4. Probar función de suma
    print("\n--- PRUEBA DE SUMA ---")
    print(f"La suma de {num1} y {num2} es: {sumar_numeros(num1, num2)}")

# 5. Función modificada con funcionalidad adicional
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
