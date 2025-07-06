## Ejercicio N° 1
Un supermercado mayorista necesita un informe de ventas, para lo cual cuenta con una secuencia
de caracteres y una secuencia de enteros, ambas contienen información del mes de JUNIO, para
las distintas sucursales. La estructura de dichas secuencias es la siguiente:

**Secuencia de caracteres Sucursal:**
(cantidad indeterminada de caracteres), cantidad de tickets (3 caracteres): sucursal & cantidad de tickets....FDS
| R | e | s | i | s | t | e | n | c | i | a | & | 0 | 2 | 5 | B | a | r | r | a | n | q | u | e | r | a | s | & | 1 | 2 | 3 | ...FDS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|--------|

**Secuencia de enteros para cada ticket:**
Forma de pago (1: efectivo, 2: tarjeta débito y 3: tarjeta crédito), Nro ticket, cantidad de artículos, importe
| 1 | 2345 | 9 | 12500 | 3 | 2950 | 4 | 9864 |...FDS |
|---|------|---|-------|---|------|---|------|-------|

Si considera necesario, puede utilizar una función ConvertiraNumero(caracter), que recibe como
parámetro un carácter y devuelve un dato entero. No es necesario desarrollar la función.
Se solicita diseñar un algoritmo que:
1) Genere una secuencia de salida de enteros que contenga el número de ticket y el importe,
cuando el importe sea mayor a 50.000.
2) Informe, para cada sucursal, cuál fue el ticket de mayor importe (y el importe).

**Razonamiento:**
- 2 secuencias donde la segunda depende de la secuencia sucursal porque hay una correspondencia entre sucursales y tickets
- Secuencia sucursal indefinida con subsecuencia palabra terminando en un '&', seguido de un número que sabemos es de 3 dígitos.
Secuencia tickets, que es definida porque la primer secuencia nos indica la cantidad de tickets correspondientes a esa sucursal, y por
consecuencia la cantidad de veces que vamos a iterarla con un PARA
- Crear secuencia de salida con tickets de monto mayor a 50.000
- Llevar el control del ticket con mayor importe para cada sucursal

<details>
<summary>Solución</summary>

```
ACCION parcial ES
  AMBIENTE
    sucursal: secuencia de caracter
    car: caracter
    tickets, salida: secuencia de entero
    tik: entero
    iter, nro_tik, mayor_importe: entero
    i, k: entero

    PROCEDIMIENTO mostar_sucursal(sec: secuencia de caracter, car: caracter) ES
      AMBIENTE
      PROCESO
        MIENTRAS car <> '&' HACER
          ESC(car)
          AVZ(sec, car)
        FIN_MIENTRAS
    FIN_PROCEDIMIENTO

    FUNCION car_a_num(car: caracter): entero ES
      AMBIENTE
      PROCESO
        SEGUN car HACER
          '0': car_a_num := 1
          '1': car_a_num := 1
          '2': car_a_num := 2
          '3': car_a_num := 3
          '4': car_a_num := 4
          '5': car_a_num := 5
          '6': car_a_num := 6
          '7': car_a_num := 7
          '8': car_a_num := 8
          '9': car_a_num := 9
        FIN_SEGUN
    FIN_FUNCION
  PROCESO
    ARR(sucursal); AVZ(sucursal, car)
    ARR(tickets); AVZ(tickets, tik)
    CREAR(salida)

    MIENTRAS NFDS(sucursal) HACER
      ESC("Para la sucursal de: ")
      mostrar_sucursal(sucursal, car)
      AVZ(sucursal, car)

      iter := 0
      PARA i := 2 HASTA 0 HACER
        iter := iter + car_a_num(car) * 10 ** i
        AVZ(sucursal, car)
      FIN_PARA

      PARA j := 0 HASTA iter HACER
        AVZ(tickets, tik)
        nro_tik := tik
        AVZ(tickets, tik)
        AVZ(tickets, tik)

        SI tik > 50000 ENTONCES
          ESCRIBIR(salida, nro_tik)
          ESCRIBIR(salida, tik)
        FIN_SI

        SI mayor_importe < tik ENTONCES
          mayor_importe := tik
        FIN_SI

        AVZ(tickets, tik)
      FIN_PARA

      ESC("el ticket de mayor importe fue de: ", mayor_importe)
    FIN_MIENTRAS

    CERRAR(salida)
    CERRAR(tickets)
    CERRAR(sucursal)
FIN_ACCION
```

</details>

## Ejercicio N° 2 - No resuelto
Un supermercado mayorista que cuenta con un sistema de atención en cajas necesita un informe
de ventas, para lo cual cuenta con el archivo secuencial VENTAS que contiene información de
todos los tickets emitidos durante el mes de JUNIO. Para cada venta se registra:
VENTAS, Ordenado por Nro de Caja, Forma de pago, Nro de ticket

| Nro de Caja | Forma de pago (EF, TD y TC) | Nro de ticket | Fecha de venta | Cantidad de artículos | Importe de la venta |
|-------------|-----------------------------|---------------|----------------|-----------------------|---------------------|

Nota: EF: efectivo, TD: tarjeta débito y TC: tarjeta crédito.

Se pide escribir un algoritmo que permita:
1) Imprimir un informe del total de artículos vendidos por caja y por forma de pago.
2) Crear un fichero de salida que contenga Nro de caja, total artículos que se pagaron en efectivo
y total artículos que se pagaron con tarjetas (TD o TC). (1 registro por caja)

| Nro de Caja | Total articulos Efectivo | Total articulos Tarjetas |
|-------------|--------------------------|--------------------------|

3) Informar cuáles son las cajas que tuvieron mayor cantidad de artículos vendidos en efectivo
que con tarjetas.
