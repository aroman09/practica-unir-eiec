def main():
    print("***********Proyecto UNIR***********")
    print("Calculadora:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    choice = input("Ingrese numero de la operacion (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))

        if choice == '1':
            print("Suma")
        elif choice == '2':
            print("Resta")
        elif choice == '3':
            print(f"Multiplicacion:  {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            print("Division")
    else:
        print("Operacion no existente...")

if __name__ == "__main__":
    main()
