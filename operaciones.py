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

def dividir(a, b):
    """
    Función para dividir dos valores usando resta recurrente.
    Comprueba si ambos parámetros son números (int o float).
    Si no lo son, devuelve un mensaje de error.
    """
     # Verificar si ambos valores son de tipo int o float
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # Manejar la división por cero, lanzando una excepción si el divisor es 0
        if b == 0:
            raise ValueError("El divisor no puede ser cero")
        # Inicializar el cociente en 0 y tomar el valor absoluto del dividendo
        cociente = 0
        # El resto es inicialmente el valor absoluto del dividendo
        resto = abs(a)

        # Mientras el resto sea mayor o igual al valor absoluto del divisor,
        # se realiza una resta iterativa para calcular cuántas veces cabe el divisor en el dividendo
        while resto >= abs(b):
            resto -= abs(b)
            cociente += 1

        # Ajustar el signo del cociente según el producto de los signos de a y b
        # Si ambos tienen el mismo signo, el cociente es positivo; si no, es negativo
        return cociente if a * b > 0 else -cociente
    # Si los parámetros no son del tipo int o float, se lanza una excepción
    raise ValueError("Ambos valores deben ser int o float")