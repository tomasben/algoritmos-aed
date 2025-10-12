## Ejercicio 1
Previaje es un programa estatal de preventa turística que le reintegra el 50% del
valor de tu viaje en crédito con un tope de $100.000, este año se habilitó el programa
para realizar viajes durante todo el 2022. Se podrán ingresar facturas del 1 de agosto
al 15 de septiembre inclusive. Luego de esta fecha no se tomarán como válidos los
comprobantes subidos.

Para poder realizar el archivo tarjeta, que almacena el monto final a reintegrar por
usuario. Para eso se debe controlar que las facturas presentadas para el reintegro se
encuentren dentro de los plazos establecidos.

**TARJETA:** *Indexado por DNI*
| DNI N(8) | Num_cuenta N(8) | Crédito N(10) | Ult_Carga Fecha |
|----------|-----------------|---------------|-----------------|

Un archivo tarjeta, donde se va actualizando el valor final que se reintegrará por usuario.

**TURISTA:** *Indexado por DNI*
| DNI N(8) | Nombre AN(100) | Fecha_nacimiento | Teléfono AN(100) |
|----------|----------------|------------------|------------------|

Un archivo turistas, donde se almacena la información de todos los usuarios que se
registraron para utilizar el beneficio del pre-viaje.

**FACTURAS** *Ordenado por nro_factura, DNI*
| Nro N(10) | DNI N(8) | id_servicio N(10) | monto N(2) | fecha_carga Fecha |
|-----------|----------|-------------------|------------|-------------------|

Un archivo facturas, donde se almacenan los comprobantes que suben a la página del pre-viaje.

Se pide:
1. Crear el monto correspondiente de crédito en archivo TARJETA, que corresponde al 50%
del monto facturado y un tope máximo de $100.000 de reintegro total. Solamente hacerlo
si la fecha_carga fue hasta del 15 de septiembre y el servicio esta habilitado para el
previaje (para esto se cuenta con un arreglo que contiene información de los id_servicio
inscriptos cuyo posición 1 contiene en el arreglo el id_servicio, y contiene un valor 1
si esta habilitado, y un cero si no lo esta).
2. Si el turista no existe en el archivo TURISTAS, debe darlo de alta y también en el
archivo TARJETA, puede generar el nro_cuenta llamando a la función obtener_nrocuenta()
(no se debe definir la función antes, se considera que ya existe).
3. Emitir total de facturas con fecha_carga fuera del plazo indicado

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

    Cuenta = REGISTRO
      dni: N(8)
      cuenta: N(8)
      credito: N(10)
      ult_carga: Fecha
    FIN_REGISTRO

    Persona = REGISTRO
      dni: N(8)
      nom: AN(20)
      nacim: Fecha
      teléfono: AN(100)
    FIN_REGISTRO

    Factura = REGISTRO
      nro: N(10)
      dni: N(8)
      id_serv: N(10)
      monto: N(2)
      carga: Fecha
    FIN_REGISTRO

    tarjeta: archivo de Cuenta indexado por dni
    cue: Cuenta
    turistas: archivo de Persona indexado por dni
    per: Persona
    facturas: archivo de Factura ordenado por nro y dni
    fac: Factura

    i, denegados: entero
    habilitados: arreglo [1..10] de 0..1
  PROCESO
    ABRIR E/S (tarjeta)
    ABRIR E/S (turistas)
    ABRIR E/ (facturas)

    denegados := 0

    MIENTAS NO FDA() HACER
      per.dni := fac.dni
      LEER(turistas, per)

      SI EXISTE ENTONCES
        SI ((fac.carga.mes <= 8) O (fac.carga.mes = 9 Y fac.carga.dia <= 15)) Y (habilitados[fac.id_serv] = 1) ENTONCES
          SI (fac.monto <= 100000) ENTONCES
            cue.dni := fac.dni
            LEER(tarjeta, cue)

            SI EXISTE ENTONCES
              cue.credito := fac.monto * 0.50
              REESCRIBIR(tarjeta, cue)
            CONTRARIO
              cue.cuenta := obtener_nrocuenta(fac.dni)
              cue.monto := fac.montp * 0.50
              cue.ult_carga := fac.carga
              ESCRIBIR(tarjeta, cue)
            FIN_SI
          CONTRARIO
            cue.dni := fac.dni
            LEER(tarjeta, dni)

            cue.credito := 50000
            ...mismo proceso de arriba
          FIN_SI
        CONTRARIO
          denegados := denegados + 1
        FIN_SI
      CONTRARIO
        definir valores cualquiera para persona y tarjeta?
      FIN_SI

      LEER(facturas, fac)
    FIN_MIENTRAS

    ESCRIBIR("El número de créditos denegados fue de: ", denegados)

    CERRAR(tarjeta)
    CERRAR(turistas)
    CERRAR(facturas)
FIN_ACCION
```

</details>

## Ejercicio 2
Posterior al proceso de actualización del punto anterior, se generó un archivo con todos
los viajes realizados donde se dio el beneficio de previaje. Destino se corresponde a cada
provincia, el nombre de las mismas está guardado en un arreglo de 23 posiciones.

**VIAJES**
| DNI N(8) | Fecha Fecha | Provincia_Destino N(2) | Monto_Crédito N(10) |
|----------|-------------|------------------------|---------------------|

Se pide realizar un algoritmo que permita determinar:
1. Por cada provincia y mes: cantidad de viajes y monto de crédito
2. Mayor monto de crédito otorgado discriminado por destino y mes
3. Destino con más turistas
4. promedio de crédito por provincia

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Viaje = REGISTRO
      dni: N(8)
      fecha = REGISTRO
        año: N(4)
        mes: 1..12
        dia: 1..31
      FIN_REGISTRO
      provincia: N(2)
      monto: N(10)
    FIN_REGISTRO

    viajes: archivo de Viaje
    reg: Viaje

    i, j: entero
    provincias: arreglo [1..23] de AN(20)
    creditos: arreglo [1..24, 1..13] de real
    viajes: arreglo [1..23, 1..12] de entero
    turistas: arreglo [1..23]

    may_cant, may_cant_dest: entero
  PROCESO
    ABRIR E/ (viajes); LEER(viajes, reg)

    PARA i := 1 HASTA 23 HACER
      PARA j := 1 HASTA 12 HACER
        creditos[i, j] := 0
      FIN_PARA
    FIN_PARA

    PARA i := 1 HASTA 23 HACER
      PARA j := 1 HASTA 12 HACER
        viajes[i, j] := 0
      FIN_PARA
    FIN_PARA

    PARA i := 1 HASTA 23 HACER
      turistas[i] := 0
    FIN_PARA

    MIENTRAS NO FDA(viajes) HACER
      creditos[reg.provincia, fecha.mes] := creditos[reg.provincia, fecha.mes] + reg.monto
      creditos[24, fecha.mes] := creditos[24, fecha.mes] + reg.monto
      creditos[reg.provincia, 13] := creditos[reg.pronvincia, 13] + reg.monto

      viajes[reg.provincia, fecha.mes] := viajes[reg.provincia, fecha.mes] + 1
      turistas[reg.provincia] := turistas[reg.pronvincia] + 1

      LEER(viajes, reg)
    FIN_MIENTRAS

    PARA i := 1 HASTA 23 HACER
      ESCRIBIR("Para la provincia: ", provincias[i])

      PARA j := 1 HASTA 12 HACER
        ESCRIBIR("Mes NRO° ", j)
        ESCRIBIR("El monto del crédito fue de $", creditos[i, j])
        ESCRIBIR("Para un total de ", turistas[i, j], " turistas.")
      FIN_PARA

      ESCRIBIR("Promedio en el año: $", creditos[i, 13] / 12)
    FIN_PARA

    may_cant := creditos[1, 13]
    may_cant_dest := 1
    PARA i := 2 HASTA 23 HACER
      SI may_cant < creditos[i, 13] ENTONCES
        may_cant := creditos[i, 13]
        may_cant_dest := i
      FIN_SI
    FIN_PARA

    ESCRIBIR("La provincia destino con el mayor monto de crédito fue: ", provincias[may_cant_dest], " con un total de $", may_cant)

    may_cant := creditos[24, 1]
    may_cant_dest := 1
    PARA j := 2 HASTA 12 HACER
      SI may_cant < creditos[24, j] ENTONCES
        may_cant := creditos[24, j]
        may_cant_dest := j
      FIN_SI
    FIN_PARA

    ESCRIBIR("El més en que se dió la mayor cantidad de créditos fue el mes N° ", may_cant_dest, " con un total de $", may_cant)



    CERRAR(viajes)
FIN_ACCION
```

</details>
