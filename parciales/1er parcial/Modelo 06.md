## Ejercicio 1
El Centro Bioquímico Chaco cuenta con información de análisis realizados durante el día.
Esta información se encuentra almacenada en una secuencia de caracteres, la cual inicia
con el código de protocolo (5 caracteres, el primero siempre una letra), luego el nombre
y apellido del paciente (finaliza en una "," -coma-), cantidad de estudios realizados
(2 caracteres) y los códigos de cada uno (4 caracteres).

El código de cada estudio inicia con una vocal, que indica el tipo. Si es de tipo "A"
cuesta $300, si es de tipo "E" cuesta $420 y si es de tipo "I" cuesta $670. La secuencia
finaliza en "*".

**Formato de la secuencia:**
CódigoProtocoloNombreApellido,CantidadEstudiosRealizadosCódigosEstudios*

*Ejemplo de la secuencia:*
A2462Reina Isabel,03A123E345E333P2342Rey León,01E888*

Se pide:
1. Generar otra secuencia de salida, que almacene los estudios solicitados del tipo "E",
siempre y cuando el protocolo de ese paciente comience con la letra "A".
2. Informar el total recaudado por tipo de estudio.
3. Informar el porcentaje de estudios de tipo "A" en relación al total de estudios.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    entrada, salida: secuencia de caracter
    car: caracter
    cond: logico
    estudios: entero
    cant_e, cant_i, cant_a, cant_tot: entero
    i, j: entero

    FUNCION convertir(car: caracter): entero ES
      SEGUN car HACER
        '0': convertir := 0
        '1': convertir := 1
        '2': convertir := 2
        '3': convertir := 3
        '4': convertir := 4
        '5': convertir := 5
        '6': convertir := 6
        '7': convertir := 7
        '8': convertir := 8
        '9': convertir := 9
    FIN_FUNCION
  PROCESO
    ARR(entrada); AVZ(entrada, car)
    CREAR(salida)

    cant_a := 0; cant_e := 0; cant_i := 0
    cant_tot := 0; estudios := 0

    MIENTRAS car <> '*' HACER
      SI car = 'A' ENTONCES
        cond := verdadero
      FIN_SI

      MIENTRAS car <> ',' HACER
        AVZ(entrada, car)
      FIN_MIENTRAS
      AVZ(entrada, car)

      PARA i := 2 HASTA 0, -1 HACER
        estudios := estudios + convertir(car) * 10 ** (i - 1)
        AVZ(entrada, car)
      FIN_MIENTRAS
      cant_tot := cant_tot + estudios

      PARA estudios hasta 1, -1 HACER
        SI cond Y car = 'E' ENTONCES
          cant_e := cant_e + 1

          PARA j := 1 HASTA 4 HACER
            ESCRIBIR(salida, car)
            AVZ(entrada, car)
          FIN_PARA
        CONTRARIO
          SEGUN car HACER
            'A': cant_a := cant_a + 1
            'E': cant_e := cant_e + 1
            'I': cant_i := cant_i + 1
          FIN_SEGUN

          AVZ(entrada, car); AVZ(entrada, car)
          AVZ(entrada, car); AVZ(entrada, car)
        FIN_SI
      FIN_PARA

      cond := falso;
    FIN_MIENTRAS
    AVZ(entrada, car)

    ESCRIBIR("Los totales recaudados por tipo de estudio son: ")
    ESCRIBIR("Estudios 'A': ", cant_a * 300)
    ESCRIBIR("Estudios 'E': ", cant_a * 420)
    ESCRIBIR("Estudios 'I': ", cant_a * 670)

    ESCRIBIR("El porcentaje de estudios tipo 'A' sobre el total
    fue del: ", cant_a * 100 / cant_tot, "%.")

    CERRAR(entrada)
    CERRAR(salida)
FIN_ACCION
```

</details>

## Ejercicio 2
Una empresa de servicios agropecuarios con diversas sucursales en el país necesita un
programa que le permita operar con los diferentes servicios que tiene contratados. Para
ello almacena información en un archivo: se tiene la sucursal, el área al que corresponde
el servicio (0: administración de campo, 1: siembra y cosecha de soja, etc), una clave de
identificación del servicio, la descripción o nombre del servicio, la cantidad de clientes
que han contratado el servicio y el monto facturado por el servicio.

SERVICIO (ordenado por SUCURSAL, AREA e ID_SERV)

| SUCURSAL N(4) | ÁREA N(1) | ID_SERV N(6) | DESC AN(45) | CANT_CLI N(4) | MONTO N(6, 2) |
|---------------|-----------|--------------|-------------|---------------|---------------|

Se pide:
1. Informar el monto facturado por la venta de servicios contratados, teniendo en cuenta la
sucursal, el área de servicio y total general, siempre y cuando la cantidad de clientes sea par.
2. Generar un archivo de salida con sucursal y total facturado por el área 1 de la misma.

| SUCURSAL N(4) | TOTAL N(8, 2) |
|---------------|---------------|

3. Informar si el total facturado por la sucursal 50 representa más o menos del 20% del total
facturado por toda la empresa.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Servicio = REGISTRO
      sucur: N(4)
      area: N(1)
      id: N(6)
      desc: AN(45)
      clientes: N(4)
      monto: N(6, 2)
    FIN_REGISTRO

    Reporte = REGISTRO
      sucur: N(4)
      total: N(8, 2)
    FIN_REGISTRO

    entrada: archivo de Servicio ordenado por sucur, area, id
    serv: Servicio
    salida: archivo de Reporte
    rep: Reporte

    cant_gral, cant_sucur, cant_area, sucur50: entero
    resg_sucur: N(4)
    resg_area: N(1)

    PROCEDIMIENTO corte_area() ES
      ESCRIBIR("La cantidad recaudada por el área ", resg_area, " fue de $", cant_area)
      cant_sucur := cant_sucur + cant_area

      SI resg_area = 1 ENTONCES
        rep.sucur := serv.sucur
        rep.total := cant_area
        GRABAR(salida, rep)
      FIN_SI

      cant_area := 0
      resg_area := serv.area
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_sucur() ES
      corte_area()
      ESCRIBIR("La cantidad recudada por el servicio para la sucursal ", resg_sucur,
      " fue de $", cant_sucur)
      cant_gral := cant_gral + cant_sucur

      SI resg_sucur = 50 ENTONCES
        sucur50 := cant_sucur
      FIN_SI

      cant_sucur := 0
      resg_sucur := serv.sucur
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (entrada); LEER(entrada, serv)
    ABRIR /S (salida)

    resg_sucur := serv.sucur; resg_area := serv.area
    cant_gral := 0; cant_area := 0; cant_sucur := 0

    MIENTRA NO FDA(entrada) HACER
      SI resg_sucur <> serv.sucur ENTONCES
        corte_sucur()
      CONTRARIO
        SI resg_area <> serv.area ENTONCES
          corte_area()
        FIN_SI
      FIN_SI

      SI (serv.clientes MOD 2 = 0) ENTONCES
        cant_area := cant_area + serv.monto
      FIN_SI

      LEER(entrada, serv)
    FIN_MIENTRAS

    ESCRIBIR("El total generado por la empresa en concepto de prestacion
    de servicios fue de $", cant_gral)

    SI sucur50 > cant_gral * 0.20 ENTONCES
      ESCRIBIR("Las ganancias de la sucursal 50 constituyeron mas del
      20% de las ganancias, recaudando ", sucur50, " en total.")
    FIN_SI

    CERRAR(entrada)
    CERRAR(salida)
FIN_ACION
```

</details>
