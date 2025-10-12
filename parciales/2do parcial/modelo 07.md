## Ejercicio 1
Una importante empresa de Turismo de la ciudad de Resistencia ha realizado a comienzos
de año la venta de PAQUETES TURISTICOS con la posibilidad de que los clientes puedan ir
pagando las cuotas mensualmente. Para premiar a los clientes con flexibilidad para
realizar pagos durante todo este año, ya que en el último mes se correría un proceso que
actualizará el estado de los clientes en su saldo.

La información de todos los clientes se encuentra dentro de un archivo secuencial, con el
siguiente formato:

**CLIENTES:**, *ordenado por nro_cliente*
| **nro_cliente** | apellido, nombre | dni | id_paquete | saldo | estado | categoria | puntos | fecha_baja |
|-----------------|------------------|-----|------------|-------|--------|-----------|--------|------------|

El campo saldo indica el "SALDO" que el paquete se encuentra pagando en su totalidad.
"SALDO A FAVOR" si el cliente, luego del proceso de recuentos de pagos, tiene un saldo
a favor, o bien "DEUDOR" en caso de que el cliente no haya llegado a pagar la totalidad
del costo del paquete turístico.

Además, las categorías de la empresa están agrupados por categorías, lo cual les permite
acceder a importantes descuentos. Las categorías pueden ser: SIMPLE, PLATA, ORO, DIAMANTE.

Todos los clientes que se dan de alta por primera vez en la empresa acceden a la categoría
SIMPLE. Los clientes en categoría PLATA tienen una bonificación del 10% y suman 10 puntos
por el paquete adquirido. Los clientes en categoría ORO tienen una bonificación del 15% y
suman 20 puntos por el paquete adquirido. Los clientes en categoría DIAMANTE tienen una
bonificación del 20% y además suman 30 puntos por el paquete adquirido.

La información de todos los movimientos de los clientes se encuentra dentro de un archivo
secuencial, con el siguiente formato:

**NOVEDADES**, *ordenado por nro_cliente, nro_novedad*
| **nro_cliente** | **nro_novedad** | apellido_nombre | dni | id_paquete | fecha_novedad | monto |
|-----------------|-----------------|-----------------|-----|------------|---------------|-------|

Si el nro_novedad = 0 implica un nuevo cliente que adquirió un paquete, en este caso
la cantidad de puntos arrancará en 0, y el estado será "SALDO".
Si el nro_novedad = 999, entonces significa que el cliente desea cancelar (dar de baja)
su paquete turístico, y por ende se deberá actualizar además, el campo de fecha_baja (el
estado quedará con SALDO A FAVOR).
Los valores intermedios de 1...998 indican los pagos realizados por los clientes. Puede
haber más de una o ninguna novedad para cada cliente.

Además se cuenta con la información de los PAQUETES TURISTICOS en un archivo indexado.

**PAQUETES_TURISTICOS**, *indexado por id_paquete*
| **id_paquete** | nombre | costo | destino |
|----------------|--------|-------|---------|

Desarrollar un algoritmo que permita actualizar el archivo de clientes, informando al
usuario por pantalla cualquier tipo de error, e informar al final.
1. La cantidad de clientes que se dieron de baja, y el monto total que debería
reintegrar la empresa.
2. El porcentaje de clientes de cada categoría.

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
      nro_cli: N(5)
      apeynom: AN(30)
      dni: N(8)
      id_paq: N(10)
      saldo: ("Saldo a favor", "Deudor")
      estado: AN(20)
      cat: ("Simple", "Plata", "Oro", "Diamante")
      puntos: entero
      baja: Fecha
    FIN_REGISTRO

    Novedad = REGISTRO
      nro_cli: N(5)
      nro_nov: N(5)
      apeynom: AN(30)
      dni: N(8)
      id_paq: N(10)
      fecha: Fecha
      monto: real
    FIN_REGISTRO

    Paquete = REGISTRO
      id_paq: N(10)
      nombre: AN(20)
      costo: real
      destino: AN(50)
    FIN_REGISTRO

    HV = 99999
    clientes: archivo de Cliente ordenado por nro_cli
    cli: Cliente
    novedades: archivo de Novedad ordenado por nro_cli y nro_nov
    nov: Novedad
    salida: archivo de Cliente
    aux, regsal: Cliente
    paquetes: archivo de Paquetes indexado por nro_paq
    paq: Paquete

    bajados, total, sim, pla, oro, dia: entero
    reintegrar: real

    PROCEDIMIENTO leer_clientes() ES
      LEER(clientes, cli)
      SI FDA(clientes) ENTONCES
        cli.nro_cli := HV
      FIN_SI
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO leer_novedades() ES
      LEER(novedaes, nov)
      SI FDA(novedades) ENTONCES
        nov.nro_cli := HV
      FIN_SI
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (clientes)
    ABRIR E/ (novedades)
    ABRIR /S (salida)
    ABRIR E/S (paquetes)

    leer_clientes()
    leer_novedades()

    bajados := 0; sim := 0; pla := 0; oro := 0; dia := 0

    MIENTRAS (cli.nro_cli <> HV) O (nov.nro_cli <> HV) HACER
      SI (cli.nro_cli > nov.nro_cli) ENTONCES
        SEGUN nov.nro_nov HACER
          0:
            aux.nro_cli := nov.nro_cli
            aux.apeynom := nov.apeynom
            aux.dni := nov.dni
            aux.id_paq := nov.id_paq
            aux.saldo := "Saldo a favor"
            aux.cat := "Simple"
            aux.puntos := 0

            sim := sim + 1
            regsal := aux
            ESCRIBIR(salida, regsal)
          1..998:
            ESCRIBIR("ERROR: no se puede sumar puntos para un cliente inexistente: ", nov.apeynom)
          999:
            ESCRIBIR("ERROR: no se puede dar de baja a un cliente inexistente: ", nov.apeynom)
        FIN_SEGUN
        leer_novedades()
      CONTRARIO
        SI (cli.nro_cli < nov.nro_cli) ENTONCES
          SEGUN cli.cat HACER
            "Simple": sim := sim + 1
            "Plata": pla := pla + 1
            "Oro": oro := oro + 1
            "Diamante": dia := dia + 1
          FIN_SEGUN

          regsal := cli
          ESCRIBIR(salida, regsal)
          leer_clientes()
        CONTRARIO
          SEGUN cli.cat HACER
            "Simple": sim := sim + 1
            "Plata": pla := pla + 1
            "Oro": oro := oro + 1
            "Diamante": dia := dia + 1
          FIN_SEGUN

          SEGUN nov.nro_nov HACER
            0:
              ESCRIBIR("ERROR: no se puede dar de alta un cliente que ya existe: ", nov.apeynom)
              leer_clientes()
              leer_novedades()
            1..998:
              aux := cli
              MIENTRAS (aux.nro_cli = nov.nro_cli) HACER
                SEGUN cli.cat HACER
                  "Simple": cli.puntos := cli.puntos + 1
                  "Plata": cli.puntos := cli.puntos + 10
                  "Oro": cli.puntos := cli.puntos + 20
                  "Diamante": cli.puntos := cli.puntos + 30
                FIN_SEGUN
                leer_novedades()
              FIN_MIENTRAS

              regsal := aux
              ESCRIBIR(salida, regsal)
              leer_clientes()
            999:
              regsal := cli
              regsal.baja := nov.fecha
              bajados := bajados + 1
              paq.id_paq := nov.id_paq
              LEER(paquetes, paq)

              SI EXISTE ENTONCES
                reintegrar := reintegrar + paq.costo
              CONTRARIO
                ESCRIBIR("ERROR: no se halló el paquete ", id_paq, " para calcular su reintegro.")
              FIN_SI

              ESCRIBIR(salida, regsal)
              leer_clientes()
              leer_novedades()
          FIN_SEGUN
        FIN_SI
      FIN_SI
    FIN_MIENTRAS

    total := sim + pla + oro + dia

    ESCRIBIR("La cantidad de paquetes cancelados fue de ", bajados, " y se deberá reembolsar un monto de $", reintegrar)
    ESCRIBIR("Los nuevos totales de planes son: ")
    ESCRIBIR("Simple: ", sim / total)
    ESCRIBIR("Plata: ", pla / total)
    ESCRIBIR("Oro: ", oro / total)
    ESCRIBIR("Diamante: ", dia / total)

    CERRAR(clientes)
    CERRAR(novedades)
    CERRAR(paquetes)
    CERRAR(salida)
FIN_ACCION
```

</details>

## Ejercicio 2
Luego del proceso de actualización del archivo de CLIENTES, se requiere un informe
de totales. Es necesario conocer estadísticas de cantidad de paquetes adquiridos
por categoría de socio, teniendo en cuenta que la empresa ofrece 12 paquetes turísticos
distintos (id_paquete=1...12). Considerando además todo lo mencionado en el Ejercicio 1,
escribir un algoritmo que permita informar por pantalla:

1. Cantidad de paquetes adquiridos por cada categoría de cliente y nombre de paquete
(considerar sólo paquetes saldados, es decir cuyo saldo del cliente sea SALDADO o con
SALDO A FAVOR).
2. Cantidad total de paquetes saldados.
3. El paquete con más ventas.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Cliente = REGISTRO
      nro_cli: N(5)
      apeynom: AN(30)
      dni: N(8)
      id_paq: N(2)
      saldo: ("Saldo a favor", "Deudor")
      estado: ?
      cat: ("Simple", "Plata", "Oro", "Diamante")
      puntos: entero
      baja: N(8)
    FIN_REGISTRO

    clientes: archivo de Cliente ordenado
    cli: Cliente
    ventas: arreglo [1..5, 1..13] de entero
    i, j, total, may, may_paq: entero

    FUNCION inferir_cat(cat: AN(20)): entero ES
      SEGUN cat HACER
        "Simple": inferir_cat := 1
        "Plata": inferir_cat := 2
        "Oro": inferir_cat := 3
        "Diamante": inferir_cat := 4
      FIN_SEGUN
    FIN_FUNCION
  PROCESO
    ABRIR E/ (clientes); LEER(clientes, cli)

    PARA i := 1 HASTA 4 HACER
      PARA j := 1 HASTA 12 HACER
        ventas[i, j] := 0
      FIN_PARA
    FIN_PARA

    MIENTRAS NO FDA(clientes) HACER
      i := inferir_cat(cli.cat)
      j := cli.id_paq

      SI (cli.saldo = "Saldo a favor") ENTONCES
        ventas[i, j] := ventas[i, j] + 1
        ventas[5, j] := ventas[5, j] + 1
        ventas[i, 13] := ventas[i, 13] + 1
      FIN_SI

      LEER(clientes, cli)
    FIN_MIENTRAS

    PARA i := 1 HASTA 4 HACER
      ESCRIBIR("Para la categoría N° ", i)

      PARA j := 1 HASTA 12 HACER
        ESCRIBIR("Servicio N° ", j)
        ESCRIBIR("El total de paquetes contratados fue de: ", ventas[i, j])
      FIN_PARA
    FIN_PARA

    total := 0
    PARA i := 1 HASTA 4 HACER
      total := total + ventas[i, 13]
    FIN_PARA

    ESCRIBIR("El total de paquetes vendidos fue de: ", total, " paquetes.")
    ventas[5, 13] := total

    may := ventas[1, 1]
    may_paq := 1
    PARA j := 1 HASTA 12 HACER
      SI ventas[5, j] > may ENTONCES
        may := ventas[5, j]
        may_paq := j
      FIN_SI
    FIN_PARA

    ESCRIBIR("El paquete con la mayor cantidad de ventas es el N° ", may_paq, " con un total de: ", may, " ventas.")

    CERRAR(clientes)
FIN_ACCION
```

</details>
