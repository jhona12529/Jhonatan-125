def validar_email(email):
    """
    Valida si una cadena de texto tiene formato de correo electrónico.
    
    Parámetros:
        email (str): Cadena de texto a validar
    
    Retorno:
        bool: True si es un correo válido, False en caso contrario
    
    Criterios de validación:
        - Debe contener un '@'
        - Debe contener un '.' después del '@'
        - El dominio debe tener al menos 2 caracteres después del punto
    """
    if '@' not in email:
        return False
    
    partes = email.split('@')
    if len(partes) != 2:
        return False
    
    usuario, dominio = partes
    if len(usuario) == 0:
        return False
    
    if '.' not in dominio:
        return False
    
    partes_dominio = dominio.split('.')
    if len(partes_dominio) < 2:
        return False
    
    if len(partes_dominio[-1]) < 2:
        return False
    
    return True

def sumar_numeros(a, b):
    """
    Suma dos números.
    
    Parámetros:
        a (int/float): Primer número
        b (int/float): Segundo número
    
    Retorno:
        float: Suma de los dos números ingresados
    """
    return a + b
