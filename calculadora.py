import sprint0python

bucle = 0

while bucle == 0:

    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa otro numero: "))

    opc = int(input("""
    ¿Que operacion desea?
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    """))

    if opc == 1:
        print(sprint0python.suma(num1, num2))
    elif opc == 2:
        print(sprint0python.resta(num1, num2))
    elif opc == 3:
        print(sprint0python.multiplicacion(num1, num2))
    elif opc == 4:
        print(sprint0python.division(num1, num2))



    while True:
        otra = input("¿Deseas hacer otra operación? (s/n): ").lower()
        if otra == "n" or otra == "s":
            if otra == "s":
                break
            if otra == "n":
                bucle = 1
                break
        else:
            print("Opcion no valida")




