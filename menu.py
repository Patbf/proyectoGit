def mostrar_menu():
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    print("6- Factorial Recursivo")
    opcion = int(input("Selecciona una opción: "))
    
    if opcion in [1, 2, 3, 4]:
        numero = float(input("Introduce un número: "))
        return opcion, numero
    elif opcion == 5:
        return opcion, None
    else:
        print("Opción no válida.")
        return mostrar_menu()