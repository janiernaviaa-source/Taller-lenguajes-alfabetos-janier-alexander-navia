import random

# Alfabeto
alfabeto = set()

# Lenguaje
lenguaje = set()


def agregar_alfabeto():
    cantidad = int(input("¿Cuántos símbolos desea agregar al alfabeto? "))

    for i in range(cantidad):
        simbolo = input(f"Ingrese el símbolo {i + 1}: ")

        if len(simbolo) == 1:
            alfabeto.add(simbolo)
        else:
            print("El símbolo debe tener un solo carácter.")

    print("Alfabeto Σ =", alfabeto)


def generar_cadenas():
    if not alfabeto:
        print("Primero debe crear el alfabeto.")
        return

    cantidad = int(input("¿Cuántas cadenas desea generar? "))

    for i in range(cantidad):
        longitud = random.randint(1, 10)
        cadena = ""

        for j in range(longitud):
            cadena += random.choice(list(alfabeto))

        print("Cadena aleatoria:", cadena)
        print("Longitud:", len(cadena))


def definir_lenguaje():
    lenguaje.clear()

    cantidad = int(input("¿Cuántas cadenas tendrá el lenguaje? "))

    for i in range(cantidad):
        cadena = input(f"Ingrese la cadena {i + 1}: ")
        lenguaje.add(cadena)

    print("Lenguaje L =", lenguaje)


def verificar_pertenencia():
    if not lenguaje:
        print("Primero debe definir el lenguaje.")
        return

    cadena = input("Ingrese una cadena para verificar: ")

    if cadena in lenguaje:
        print(f'"{cadena}" pertenece al lenguaje -> True')
    else:
        print(f'"{cadena}" pertenece al lenguaje -> False')


def mostrar_menu():
    while True:
        print("\n========== TALLER DE LENGUAJES ==========")
        print("1. Agregar símbolos al alfabeto")
        print("2. Generar cadenas aleatorias")
        print("3. Definir lenguaje")
        print("4. Verificar pertenencia")
        print("5. Mostrar alfabeto")
        print("6. Mostrar lenguaje")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_alfabeto()
        elif opcion == "2":
            generar_cadenas()
        elif opcion == "3":
            definir_lenguaje()
        elif opcion == "4":
            verificar_pertenencia()
        elif opcion == "5":
            print("Alfabeto Σ =", alfabeto)
        elif opcion == "6":
            print("Lenguaje L =", lenguaje)
        elif opcion == "7":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")


mostrar_menu()