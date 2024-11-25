# menu.py
def mostrar_menu():
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    opcion = int(input("Selecciona una opción: "))
    return opcion

# Importa las funciones de operaciones desde operaciones.py
from operaciones import sumar, restar, multiplicar

if __name__ == "__main__":  # Este bloque se ejecuta solo si este archivo es ejecutado directamente
    # Llamamos a la función mostrar_menu para mostrar el menú al usuario y obtener la opción seleccionada
    # 'opcion' es la opción seleccionada y 'numero' es el número introducido por el usuario
    opcion, numero = mostrar_menu()  
    
    # Si el usuario selecciona la opción 1 (sumar)
    if opcion == 1:
        # Pedimos al usuario otro número para realizar la suma
        # Convertimos la entrada del usuario en un número decimal (float)
        a = float(input("Introduce otro número: "))  
        # Llamamos a la función sumar y mostramos el resultado
        # Imprime el resultado de la suma entre 'numero' y 'a'
        print(sumar(numero, a))  

    # Si el usuario selecciona la opción 2 (restar)
    elif opcion == 2:
        # Pedimos al usuario otro número para realizar la resta
        # Convertimos la entrada del usuario en un número decimal (float)
        a = float(input("Introduce otro número: "))  
        # Llamamos a la función restar y mostramos el resultado
        print(restar(numero, a))  

    # Si el usuario selecciona la opción 3 (multiplicar)
    elif opcion == 3:
        # Pedimos al usuario otro número para realizar la multiplicación
        # Convertimos la entrada del usuario en un número decimal (float)
        a = float(input("Introduce otro número: "))  
        # Llamamos a la función multiplicar y mostramos el resultado
        print(multiplicar(numero, a))  

    # Si el usuario introduce una opción no válida
    else:
        print("Opción no válida.")  # Muestra un mensaje de error si la opción no es 1, 2 o 3






