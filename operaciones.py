def sumar(a, b):
    """
    Función para sumar dos valores.
    Comprueba si ambos parámetros son números (int o float) antes de sumar.
    Si no lo son, devuelve un mensaje de error.
    """
    # Verificar si ambos parámetros son int o float
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # Si son válidos, devuelve la suma
        return a + b
    else:
        # Si no son válidos, devuelve un mensaje de error
        return "Error: ambos deben ser int o float"

def restar(a, b):
    """
    Función para restar dos valores.
    Comprueba si ambos parámetros son números (int o float) antes de restar.
    Si no lo son, devuelve un mensaje de error.
    """
    # Verificar si ambos parámetros son int o float
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # Si son válidos, devuelve la resta
        return a - b
    else:
        # Si no son válidos, devuelve un mensaje de error
        return "Error: ambos deben ser int o float"

def multiplicar(a, b):
    """
    Función para multiplicar dos valores usando suma recurrente.
    Comprueba si ambos parámetros son números (int o float).
    Si no lo son, devuelve un mensaje de error.
    """
    # Verificar si ambos parámetros son int o float
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # Convertir b a entero en caso de ser float para iterar correctamente
        b_entero = int(b)
        # Usar un bucle para realizar la multiplicación en vez de la multiplicación directamente
        return sum(a for _ in range(b_entero))
    else:
        # Si no son válidos, devuelve un mensaje de error
        return "Error: ambos deben ser int o float"
