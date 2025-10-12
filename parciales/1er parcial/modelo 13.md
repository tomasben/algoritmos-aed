## Ejercicio 1
La empresa "Caminos del Litoral" quiere conocer las estadísticas del tráfico existente
en el puente General Belgrano (popularmente conocido como Puente Chaco Corrientes).
Para esto cuenta con los datos del movimiento ocurrido en el mes de junio de 2024 en un
día (desde el día 1 del mes, hasta 30), sabiendo que todos los días hubieron movimientos,
se dispone de una secuencia de caracteres con el siguiente formato:

día(2 caracter)ESferiado(S o N)InformacionDeVehiculos! [...]día(2 caracter)ESferiado(S o N)InformacionDeVehiculos!

Donde InformacionDeVehiculos se corresponde con:
Categoria (1 caracter: 1..5) HHMM(horaminuto) Patente (7 caracteres)$

*Ejemplo:*
12S22230AC13FE32231AB45HI42231AB21HU13N58615AD23HF_!

El monto a pagar del peaje depende de la categoría. Se puede obtener a partir de una
función ya implementada, monto_peaje(), que recibe como parámetro el carácter de la
categoría.

Se le solicita:
1. Generar una secuencia de salida con la información de todos los vehículos de una determinada
categoría (que ingrese el usuario) y que han circulado los días feriados. Interesará conocer:
HHMMPatente (separar la información de cada vehículo por el carácter '#'.
2. Por cada día, indicar la cantidad recaudada.
3. Porcentaje de vehículos de cada categoría sobre el total.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    autos, salida: secuencia de caracter
    car: caracter
    cat1, cat2, cat3, cat4, cat5, cat_eleg: entero
    total, recaudado: entero
    i, j: entero
    es_feriado: logico
  PROCESO
    ARR(autos); AVZ(autos, car)
    CREAR(salida)

    cat1 := 0; cat2 := 0; cat3 := 0; cat4 := 0; cat5 := 0

    ESCRIBIR("Ingrese el caracter correspondiente a la categoria de vehículo que se desea
    conocer la cantidad de ellos que pasaron por el peaje en dias feriado: [1..5]")
    Leer(cat_eleg)

    PARA i := 1 HASTA 30 HACER
      recaudado := 0
      AVZ(autos, car)
      AVZ(autos, car)

      SI car = 'S' ENTONCES
        es_feriado := verdadero
      CONTRARIO
        es_feriado := falso
      FIN_SI
      AVZ(autos, car)

      MIENTRAS car <> '!' HACER
        SEGUN car HACER
          '1': cat1 := cat1 + 1
          '2': cat2 := cat2 + 1
          '3': cat3 := cat3 + 1
          '4': cat4 := cat4 + 1
          '5': cat5 := cat5 + 1
        FIN_SEGUN
        recaudado := recaudado + monto_peaje(car)

        SI es_feriado Y car = cat_eleg ENTONCES
          AVZ(autos, car)

          PARA j :=   1 HASTA 11 HACER
            ESCRIBIR(salida, car)
            AVZ(autos, car)
          FIN_PARA
          ESCRIBIR(salida, '#')
        CONTRARIO
          AVZ(autos, car)

          PARA j := 1 HASTA 11 HACER
            AVZ(autos, car)
          FIN_PARA
        FIN_SI
      FIN_MIENTRAS

      ESCRIBIR("Para el día nro ", i, " de junio, el monto recaudado fue de $", recaudado)
    FIN_PARA
    total := cat1 + cat2 + cat3 + cat4 + cat5

    ESC("Los porcentajes de vehículos segun su categoria fueron: ")
    ESC("Categoría 1: ", cat1 * 100 / total)
    ESC("Categoría 2: ", cat2 * 100 / total)
    ESC("Categoría 3: ", cat3 * 100 / total)
    ESC("Categoría 4: ", cat4 * 100 / total)
    ESC("Categoría 5: ", cat5 * 100 / total)

    CERRAR(autos)
    CERRAR(salida)
FIN_ACCION
```

</details>

## Ejercicio 2
Los datos históricos de los vehículos que pasaron por el peaje se encuentra en un archivo
con el siguiente formato:

PEAJE (Ordenado por año, mes, día, categoría y patente)

| Año | Mes | Día | Categoría | Patente | Cantidad de pases |
|-----|-----|-----|-----------|---------|-------------------|

Se le solicita:
1. Informar la cantidad total de vehículos que pasaron por año y mes, y total general.
2. Informar el año en el que hubo la mayor cantidad de pases.
3. Generar un archivo de salida con la siguiente información:

| Año | Mes | Día | Cantidad de pases |
|-----|-----|-----|-------------------|

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Auto = REGISTRO
      año: N(4)
      mes: 1..12
      dia: 1..31
      cat: N(1)
      pat: AN(7)
      pases: N(2)
    FIN_REGISTRO

    Informe = REGISTRO
      año: N(4)
      mes: 1..12
      mes: 1..31
      pases: N(2)
    FIN_REGISTRO

    peaje: archivo de Auto ordenado por año, mes, dia, cat, pat
    auto: Auto
    salida: archivo de Informe
    inf: Informe

    cant_gral, cant_año, cant_mes, cant_dia, may_pas: entero
    resg_año, may_pas_año: N(4)
    resg_mes, resg_dia: N(2)

    PROCEDIMIENTO corte_año() ES
      corte_mes()
      ESCRIBIR("Para el año ", resg_año, " la cantidad de vehiculos que atravesaron
      el peaje fue de: ", cant_año, " vehículos.")
      cant_gral := cant_gral + cant_año

      SI may_pas > cant_año ENTONCES
        may_pas := cant_año
        may_pas_año := resg_año
      FIN_SI

      cant_año := 0
      resg_año := auto.año
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_mes() ES
      corte_dia()
      ESCRIBIR("La cantidad de vehículos que atravesaron el peaje en el mes de ", resg_mes,
      " fue de: ", cant_mes, " vehículos.")
      cant_año := cant_año + cant_mes
      cant_mes := 0
      resg_mes := auto.mes
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_dia() ES
      cant_mes := cant_mes + cant_dia

      inf.año := resg_año
      inf.mes := resg_mes
      inf.dia := resg_dia
      inf.pases := cant_dia
      ESCRIBIR(salida, inf)

      cant_dia := 0
      resg_dia := auto.dia
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (peaje); LEER(peaje, auto)
    ABRIR /S (salida)

    resg_año := auto.año; resg_mes := auto.mes; resg_dia := auto.dia
    cant_gral := 0; cant_año := 0; cant_mes := 0; cant_dia := 0; may_pas := 0

    MIENTRAS NO FDA(peaje) HACER
      SI resg_año <> auto.año ENTONCES
        corte_año()
      CONTRARIO
        SI resg_mes <> auto.mes ENTONCES
          corte_mes()
        CONTRARIO
          SI resg_dia <> auto.dia ENTONCES
            corte_dia()
          FIN_SI
        FIN_SI
      FIN_SI

      LEER(peaje, auto)
    FIN_MIENTRAS
    corte_año()

    ESCRIBIR("El total general de vehiculos que atravesaron el peaje es de: ", cant_gral, " vehículos.")
    ESCRIBIR("Y la mayor cantidad de pases en un año fue en el ", may_pas_año, " con un total de: ", may_pas, " vehículos.")

    CERRAR(peaje)
    CERRAR(salida)
FIN_ACCION
```

</details>
