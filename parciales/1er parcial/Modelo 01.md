## Ejercicio 1
Un supermercado mayorista necesita un informe de ventas, para lo cual cuenta con una secuencia
de caracteres y una secuencia de enteros, ambas contienen información del mes de JUNIO, para
las distintas sucursales. La estructura de dichas secuencias es la siguiente:

**Secuencia de caracteres Sucursal:**
(cantidad indeterminada de caracteres), cantidad de tickets (3 caracteres): sucursal & cantidad de tickets....FDS
Resistencia&025Barranqueras&123...FDS

**Secuencia de enteros para cada ticket:**
Forma de pago (1: efectivo, 2: tarjeta débito y 3: tarjeta crédito), Nro ticket, cantidad de artículos, importe
1 | 2345 | 9 | 12500 | 3 | 2950 | 4 | 9864 |...FDS

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

## Ejercicio 2
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

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Ticket = REGISTRO
      nro_caja: N(2)
      metodo: AN(2)
      nro_tik: N(15)
      fecha = REGISTRO
        año: N(4)
        mes: 1..12
        dia: 1..31
      FIN_REGISTRO
      cant: N(3)
      importe: real
    FIN_REGISTRO

    Informe = REGISTRO
      nro_caja: N(2)
      tot_efec: real
      tot_tarj: real
    FIN_REGISTRO

    ventas: archivo de Ticket ordenado por nro_caja, metodo, nro_tik
    tik: Ticket
    salida: archivo de Informe
    inf: Informe

    cant_caja, cant_metodo, tot_efec, tot_tarj: entero
    resg_caja: N(2)
    resg_metodo: AN(2)

    PROCEDIMIENTO corte_caja() ES
      corte_metodo()
      ESCRIBIR("Para la caja número ", resg_caja, " se registraron ",
      cant_caja, " ventas en total.")
      cant_caja := 0

      SI tot_efec > tot_tarj ENTONCES
        ESCRIBIR("La caja número ", resg_caja, " registró más ventas en efectivo que con tarjeta.")
      FIN_SI
      inf.nro_caja := tik.nro_caja
      inf.tot_efec := tot_efec
      inf.tot_tarj := tot.tarj
      ESCRIBIR(salida, inf)

      tot_efec := 0
      tot_tarj := 0
      resg_caja := tik.nro_caja
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_metodo() ES
      ESCRIBIR("Se asentaron un total de ", cant_metodo, " ventas para
      la forma de pago: ", resg_metodo)
      cant_caja := cant_caja + cant_metodo
      cant_metodo := 0
      resg_metodo := tik.metodo
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (ventas); LEER(ventas, tik)
    ABRIR /S (salida)

    resg_caja := tik.nro_caja; resg_metodo := tik.metodo
    cant_caja := 0; cant_metodo := 0; tot_efec := 0; tot_tarj := 0

    MIENTRAS NO FDA(ventas) HACER
      SI resg_caja <> tik.nro_caja ENTONCES
        corte_caja()
      CONTRARIO
        SI resg_metodo <> tik.metodo ENTONCES
          corte_metodo()
        FIN_SI
      FIN_SI

      cant_caja := cant_caja + tik.cant
      SI tik.metodo = "EF" ENTONCES
        tot_efec := tot_efec + tik.cant
      CONTRARIO
        tot_tarj := tot_tarj + tik.cant
      FIN_SI

      LEER(ventas, tik)
    FIN_MIENTRAS
    corte_caja()

    CERRAR(ventas)
    CERRAR(salida)
FIN_ACCION
```

</details>
