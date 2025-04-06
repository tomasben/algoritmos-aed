def main():
    print("Este algoritmo permite conocer cual es el mayor, menor y el intermedio entre 3 números proporcionados. Ingrese los 3 números")

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    maximo = num1
    if num2 > num1:
        maximo = num2
    if num3 > num2:
        maximo = num3

    minimo = num1
    if num2 < num1:
        minimo = num2
    if num3 < num2:
        minimo = num3

    medio = num1 + num2 + num3 - maximo - minimo

    print(f'El mayor de los números es {maximo}')
    print(f'El menor de los números es {minimo}')
    print(f'El medio de los números es {medio}')

main()
