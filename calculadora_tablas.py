# Calculadora interactiva de tablas
# Usa while, for, range() y condicionales (sin listas ni funciones)

print("¡Hola! Bienvenido a la calculadora de tablas 😊")

opcion = 0

# Requerimiento 1: bucle principal que mantiene el programa en ejecución
while opcion != 5:
    print()
    print("===== MENÚ =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = int(input("¿Qué te gustaría hacer? (1-5): "))

    # Requerimiento 2: validar la opción elegida
    if opcion == 5:
        print("¡Gracias por usar la calculadora! Hasta pronto 👋")

    elif opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
        # Requerimiento 3: pedir número base y límite
        base = float(input("Dime el número base para la tabla: "))
        limite = int(input("¿Hasta qué número quieres la tabla?: "))

        print()
        print("Aquí tienes tu tabla:")

        # Requerimiento 4: bucle for con range() desde 1 hasta el límite
        for i in range(1, limite + 1):
            if opcion == 1:
                print(base, "+", i, "=", base + i)
            elif opcion == 2:
                print(base, "-", i, "=", base - i)
            elif opcion == 3:
                print(base, "x", i, "=", base * i)
            else:
                print(base, "÷", i, "=", round(base / i, 2))

    else:
        print("Mmm, esa opción no existe. Intenta con un número del 1 al 5 🙂")
