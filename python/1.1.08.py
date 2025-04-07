def calcular_fecha():
    print("Ingrese la fecha de nacimiento en el formato DIA-MES-AÑO")
    dia_nac = int(input("Ingresa el dia: "))
    mes_nac = int(input("Ingresa el mes: "))
    año_nac = int(input("Ingresa el año: "))

    print("Ahora ingrese la fecha actual siguiendo el mismo formato")
    dia_act = int(input("Ingrese el dia: "))
    mes_act = int(input("Ingrese el mes: "))
    año_act = int(input("Ingrese el año: "))

    edad = año_act - año_nac - 1

    if mes_act == mes_nac:
        if dia_act > dia_nac:
            edad += 1
    elif mes_nac < mes_act:
        edad += 1

    print(f'La edad  actual de la persona es de {edad} años')


calcular_fecha()
