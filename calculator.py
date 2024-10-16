def main():
    print("***********Proyecto UNIR***********")
    print("Calculadora:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raíz Cuadrada")

    choice = input("Ingrese numero de la operacion: (1-2-3-4-5): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))

        if choice == '1':
            print(f"Suma:  {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Resta:  {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Multiplicacion:  {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            print(f"Division:  {num1} / {num2} = {num1 / num2}")
        elif choice == '5':
            print("Raiz Cuadrada")
            num = float(input("Ingrese un número para calcular su raíz cuadrada: "))
            if num >= 0:
                print(f"Resultado de la raíz cuadrada: {math.sqrt(num)}")
            else:
                print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
    else:
        print("Operacion no existente...")

if __name__ == "__main__":
    main()
