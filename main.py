import os

def ejecutar_ejercicio(ejercicio):
    if ejercicio == 1:
        os.system('python ejercicio1/main.py')
    elif ejercicio == 2:
        os.system('python ejercicio2/main.py')
    else:
        print("Ejercicio no válido")

def mostrar_menu():
    print("Menú de Ejercicios")
    print("1. Ejecutar Ejercicio 1")
    print("2. Ejecutar Ejercicio 2")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            ejecutar_ejercicio(1)
        elif opcion == '2':
            ejecutar_ejercicio(2)
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
    