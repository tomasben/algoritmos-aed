## Ejercicio 1
Un importante banco del país cuenta con la información de todos sus clientes en
un archivo secuencial con el siguiente formato:

**CLIENTES** *ordenado por id_sucursal, id_cliente*
| **id_sucursal** | **id_cliente** | nombre y apellido | saldo a la fecha | fecha alta | fecha baja |
|-----------------|----------------|-------------------|------------------|------------|------------|

Al final de cada mes, corre un proceso de actualización con todos los movimientos
generados por cada cliente durante el mes.

La información se encuentra en un archivo secuencial con la siguiente estructura:

**MOVIMIENTOS** *ordenado por id_sucursal, id_cliente, cod_movimiento*
| **id_sucursal** | **id_cliente** | **cod_movimiento** (0..99) | nombre y apellido | fecha_movimiento | monto | detalle | categoría (1..6) | tipo |
|-----------------|----------------|----------------------------|-------------------|------------------|-------|---------|------------------|------|

Donde:
- cod_movimiento indica: 0 (alta de un nuevo cliente), 99 (baja de un cliente),
y cualquier otro valor entre 1 y 98 es una transacción en la cuenta del cliente.
- detalle: indica una descripción del movimiento.
- categoría: indica la categoría del movimiento (1-Supermercado, 2-Farmacia,
3-Carniceria, 4-Transferencia, 5-Pago de servicios, 6-Otros).
- tipo: indica "I" si es un ingreso, "E" si es un egreso.

Se pide:
1. Desarrollar un algoritmo que permita mantener actualizado el archivo CLIENTES
con sus respectivos saldos. Informar por pantalla cualquier tipo de error que
considere pertinente durante el proceso.
2. Indicar la cantidad de clientes nuevos que se produjeron durante el proceso.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Fecha = REGISTRO
      año: N(4)
      mes: 1..12
      dia: 1..31
    FIN_REGISTRO

    Cliente = REGISTRO
      clave = REGISTRO
        id_suc: N(5)
        id_cli: N(5)
      FIN_REGISTRO
      apeynom: AN(30)
      saldo: real
      alta: Fecha
      baja: Fecha
    FIN_REGISTRO

    Movimiento = REGISTRO
      clave = REGISTRO
        id_suc: N(5)
        id_cli: N(5)
      FIN_REGISTRO
      cod_mov: 0..99
      apeynom: AN(30)
      fecha: Fecha
      monto: real
      detalle: AN(100)
      cat: 1..6
      tipo: ('I', 'E')
    FIN_REGISTRO

    HV = 99999
    clientes: archivo de Cliente ordenado por id_suc y id_cli
    cli: Cliente
    salida: archivo de Cliente
    aux, regsal: Cliente
    movimientos: archivo de Movimiento ordenado por id_suc y id_cli
    mov: Movimiento

    añadidos: entero

    PROCEDIMIENTO leer_cliente() ES
      LEER(clientes, cli)
      SI FDA(clientes) ENTONCES
        cli.clave := HV
      FIN_SI
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO leer_movimiento() ES
      LEER(movimientos, mov)
      SI FDA(movimientos) ENTONCES
        mov.clave := HV
      FIN_SI
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (clientes)
    ABRIR E/ (movimientos)
    ABRIR /S (salida)

    leer_cliente()
    leer_movimiento()

    añadidos := 0

    MIENTRAS (cli.clave <> HV) O (mov.clave <> HV) HACER
      SI (cli.clave > mov.clave) ENTONCES
        SEGUN mov.cod_mov HACER
          0:
            regsal.clave := mov.clave
            regsal.apeynom := mov.apeynom
            regsal.alta := mov.fecha

            SI mov.tipo = 'I' ENTONCES
              regsal.saldo := mov.monto
            CONTRARIO
              regsal.saldo := 0 - mov.monto
            FIN_SI
            ESCRIBIR(salida, regsal)
            añadidos := añadidos + 1
          1..98:
            ESCRIBIR("ERROR: no se puede completar transacción para cliente inexistente: ", mov.clave)
          99:
            ESCRIBIR("ERROR: no se puede dar de baja a cliente inexistente: ", mov.clave)
        FIN_SEGUN
        leer_movimiento()
      CONTRARIO
        SI (cli.clave < mov.clave) ENTONCES
          regsal := cli
          ESCRIBIR(salida, regsal)
          leer_cliente()
        CONTRARIO
          SEGUN mov.cod_mov HACER
            0:
              ESCRIBIR("ERROR: no se puede dar de alta a cliente existente: ", mov.clave)
              leer_movimiento()
            1..98:
              aux := cli

              MIENTRAS (aux.clave = mov.clave) HACER
                SI mov.tipo = 'I' ENTONCES
                  aux.saldo := aux.saldo + mov.monto
                CONTRARIO
                  aux.saldo := aux.saldo - mov.monto
                FIN_SI
                leer_movimiento()
              FIN_MIENTRAS

              regsal := aux
              ESCRIBIR(salida, regsal)
            99:
              regsal := cli
              regsal.baja := mov.fecha
              ESCRIBIR(salida, regsal)
              leer_movimiento()
          FIN_SEGUN
          leer_cliente()
        FIN_SI
      FIN_SI
    FIN_MIENTRAS

    ESCRIBIR("El número de clientes dados de alta fue de: ", añadidos)

    CERRAR(clientes)
    CERRAR(movimientos)
    CERRAR(salida)
FIN_ACCION
```

</details>

## Ejercicio 2
El banco ha solicitado un informe para conocer cómo se integra su cartera de clientes,
agrupándolos por sucursal y categoría de cliente, a partir de los datos del archivo
de CLIENTES (usar las estructuras de datos del ejercicio anterior).

Considerando que son 15 sucursales, y la información de las sucursales se encuentra
en un archivo indexado:

**Sucursales** *indexado por id_sucursal*
| **id sucursal** | nombre de la sucursal | direccion | localidad |
|-----------------|-----------------------|-----------|-----------|

La estructura del informe solicitado es la siguiente:

|                     | Categoría diamante | Categoría oro |	Categoría estándar | Totales por suc. |
|:-------------------:|:------------------:|:-------------:|:-------------------:|:----------------:|
| Nombre sucursal 1   |                    |               |                     |                  |
| Nombre sucursal 2	  |                    |               |                     |                  |
| ...                 |                    |               |                     |                  |
| Nombre sucursal 15  |                    |               |                     |                  |
| Totales x categoría |                    |               |                     |                  |

La categoría del cliente dependerá de los montos obtenidos en su saldo de la cuenta
al último día del mes.
- Montos menores a $100.000 serán de categoría estándar.
- Montos menores a $1.500.000 serán de categoría oro.
- Montos superiores serán de categoría diamante.

*Nota:* no considerar clientes dados de baja.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Fecha = REGISTRO
      año: N(4)
      mes: 1..12
      dia: 1..31
    FIN_REGISTRO

    Cliente = REGISTRO
      clave = REGISTRO
        id_suc: N(5)
        id_cli: N(5)
      FIN_REGISTRO
      apeynom: AN(30)
      saldo: real
      alta: Fecha
      baja: Fecha
    FIN_REGISTRO

    Sucursal = REGISTRO
      id_suc: N(5)
      nom: AN(20)
      direc: AN(50)
      localidad: AN(20)
    FIN_REGISTRO

    clientes: archivo de Cliente ordenado por id_suc y id_cli
    cli: Cliente
    sucursales: archivo de Sucursal indexado por id_suc
    suc: Sucursal

    informe: arreglo [1..16, 1..4] de real
    i, j, total: entero
  PROCESO
    ABRIR E/ (clientes); LEER(clientes, cli)
    ABRIR E/S (sucursales)

    PARA i := 1 HASTA 16 HACER
      PARA i := 1 HASTA 4 HACER
        informe[i, j] := 0
      FIN_PARA
    FIN_PARA

    MIENTRAS NO FDA(clientes) HACER
      i := cli.clave.id_suc

      SEGUN cli.saldo HACER
        < 100000: j := 1
        < 1500000: j := 2
        OTRO: j := 3
      FIN_SEGUN

      SI cli.baja.año = 0 ENTONCES
        informe[i, j] := informe[i, j] + cli.saldo
        informe[16, j] := informe[16, j] + cli.saldo
        informe[i, 4] := informe[i, 4] + cli.saldo
      FIN_SI

      LEER(clientes, cli)
    FIN_MIENTRAS

    total := 0
    PARA j := 1 HASTA 3 HACER
      total := total + informe[16, j]
    FIN_PARA
    informe[16, 4] := total

    ESCRIBIR("|    | Cat. Diamante | Cat. Oro | Cat. Estándar | Totales por cat. |")
    PARA i := 1 HASTA 15 HACER
      suc.id_suc := i
      LEER(sucursales, suc)

      SI EXISTE ENTONCES
        ESCRIBIR(suc.nom)
      CONTRARIO
        ESCRIBIR("Sucursal N° ", i)
      FIN_SI

      PARA j := 1 HASTA 4 HACER
        ESCRIBIR(informe[i, j])
      FIN_PARA
    FIN_PARA

    ESCRIBIR("Totales por categoría: ")
    PARA i := 1 HASTA 3 HACER
      ESCRIBIR(informe[16, j])
    FIN_PARA

    ESCRIBIR("Total general de saldos: ", informe[16, 4])

    CERRAR(clientes)
    CERRAR(sucursales)
FIN_ACCION
```

</details>
