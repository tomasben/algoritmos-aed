def suma(a, b):
    suma = a + b

    if suma <= 50:
        print("La suma es menor o igual a 50")
    elif suma > 50 and suma <= 100:
        print("La suma esta entre 50 y 100")
    elif suma > 100 and suma <= 200:
        print("La suma está entre 100 y 200")
    else:
        print("La suma es mayor a 200")

suma(20, 190)
