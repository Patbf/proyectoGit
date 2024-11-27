from menu import mostrar_menu
from operaciones import sumar, restar, multiplicar, dividir

if __name__ == "__main__":
    while True:
        opcion, numero = mostrar_menu()

        if opcion == 1:
            a = float(input("Introduce otro número: "))
            print(f"Resultado: {sumar(numero, a)}")
        elif opcion == 2:
            a = float(input("Introduce otro número: "))
            print(f"Resultado: {restar(numero, a)}")
        elif opcion == 3:
            a = float(input("Introduce otro número: "))
            print(f"Resultado: {multiplicar(numero, a)}")
        elif opcion == 4:
            a = float(input("Introduce otro número: "))
            try:
                print(f"Resultado: {dividir(numero, a)}")
            except ValueError as e:
                print(e)
        elif opcion == 5:
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción no válida.")