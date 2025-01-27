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
        return a * b
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



def factorial_recursivo(n):
    # Verifica si 'n' no es un entero o si es negativo
    if not isinstance(n, int) or n < 0:
        # Si la validación falla, lanza un error explicativo
        raise ValueError("El número debe ser un entero no negativo.")
    
    # Caso base: Si 'n' es 0 o 1, el factorial es 1
    if n == 0 or n == 1:
        return 1
    
    # Llamada recursiva: Si 'n' es mayor que 1, multiplica 'n' por el resultado de 'factorial_recursivo(n-1)'
    return n * factorial_recursivo(n - 1)



def fibonacci(n):
    """
    Calcula el n-ésimo número de la secuencia de Fibonacci de forma iterativa.
    
    :param n: Un número entero no negativo
    :return: El n-ésimo número de Fibonacci
    """
    
    # Verifica si n es un entero y si es mayor o igual a 0
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    
    # Inicializa las dos primeras variables de la secuencia Fibonacci
    a, b = 0, 1
    
    # Si n es 0, el resultado es 0 (primer número de Fibonacci)
    if n == 0:
        return a
    
    # Si n es 1, el resultado es 1 (segundo número de Fibonacci)
    if n == 1:
        return b
    
    # Calcula el n-ésimo número de Fibonacci de forma iterativa
    for _ in range(n - 1):  
        a, b = b, a + b  
    
    # Devuelve el valor de b, que es el n-ésimo número de Fibonacci
    return b  

def factorial_iterativo(n):
    # Verificar que el argumento sea un número entero no negativo
    if not isinstance(n, int) or n < 0:
        # Si no es un entero o es negativo, lanzar una excepción
        raise ValueError("El número debe ser un entero no negativo.")
    
    # Inicializar la variable `resultado` en 1.
    # Este valor representará el producto acumulado.
    resultado = 1

    # Iterar desde 1 hasta `n` (inclusive) para calcular el factorial.
    for i in range(1, n + 1):
        # Multiplicar el valor actual de `resultado` por el número `i`.
        resultado *= i

    # Devolver el valo
