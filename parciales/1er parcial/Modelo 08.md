## Ejercicio 1
La empresa TICKET-TEC ha generado una secuencia de caracteres con información
de sus ventas para los eventos de los últimos 3 meses, cuya estructura se describe
a continuación.

Inicialmente existe el nombre del local de los eventos, cuya longitud se desconoce,
termina con un #; a continuación se tiene la información de todos los tickets vendidos
para ese local, separado cada ticket del siguiente con el carácter '!', y al final de
todas las ventas para ese local, el carácter &. Por último la marca de fin de secuencia.
También en el caso de butaca se desconoce la longitud del número, termina con un guión.

*Ejemplo:*
Teatro Ópera#2030270520171A45-!223027052017J3D120-!203028052017Z C233-!&Galpon de las Luces#2030070720171C5-!2230301020172A233-!&(fin)

local de eventos#horario evento [hhmm] Fecha del evento [ddmmaaaa] código del evento [1..3] butaca [sector [A,C o D], número]|—!
Solo hay dos horarios 20:30 y 22:30.

La empresa solicita un algoritmo que cumpla con las siguientes consignas:
1. Generar una nueva secuencia que contenga los tickets correspondientes a un horario ingresado por el usuario.
2. Informar total general de tickets vendidos, total de tickets por sector y porcentaje de cada uno sobre el total general.

<details open>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    ventas, salida: secuencia de caracter
    fac: caracter
    i, j: entero
    sec_a, sec_c, sec_d, total: entero
    elegido, actual: entero
    condicion: logico

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
    ARR(ventas); AVZ(ventas, fac)
    CREAR(salida)

    sec_a := 0; sec_c := 0; sec_d := 0; actual := 0

    ESCRIBIR("A continuación ingrese un horario para el cual se desea conocer todos los tickets: [HHMM]")
    LEER(elegido)

    MIENTRAS NO FDS(ventas) HACER
      MIENTRAS fac <> '#' HACER
        AVZ(ventas, fac)
      FIN_MIENTRAS
      AVZ(ventas, fac)

      MIENTRAS fac <> '&' HACER
        PARA i := 3 HASTA 0, -1 HACER
          actual := actual + convertir(fac) * 10 ** i
          AVZ(ventas, fac)
        FIN_PARA

        // Almaceno el resultado logico de comparar si el horario HHMM introducido
        por el usuario coincide con el entero sacado de la secuencia
        condicion := actual = elegido

        SI condicion ENTONCES
          PARA k := 1 HASTA 7 HACER
            ESCRIBIR(salida, fac)
            AVZ(ventas, fac)
          FIN_PARA

          SEGUN fac HACER
            'A': sec_a := sec_a + 1
            'C': sec_c := sec_c + 1
            'D': sec_d := sec_d + 1
          FIN_SEGUN
          ESCRIBIR(salida, fac)
          AVZ(ventas, fac)

          MIENTRAS fac <> '!' HACER
            ESCRIBIR(salida, fac)
            AVZ(ventas, fac)
          FIN_MIENTRAS
          AVZ(ventas, fac)
        CONTRARIO
          PARA k := 1 HASTA 7 HACER
            AVZ(ventas, fac)
          FIN_PARA

          SEGUN fac HACER
            'A': sec_a := sec_a + 1
            'C': sec_c := sec_c + 1
            'D': sec_d := sec_d + 1
          FIN_SEGUN
          AVZ(ventas, fac)

          MIENTRAS fac <> '!' HACER
            AVZ(ventas, fac)
          FIN_MIENTRAS
          AVZ(ventas, fac)
        FIN_SI

        actual := 0
      FIN_MIENTRAS

      // Avanzo el '&' que separa teatros
      AVZ(ventas, fac)
    FIN_MIENTRAS

    total := sec_a + sec_c + sec_d
    ESCRIBIR("El total de tickets vendidos es de: ", total, " tickets.")

    ESCRIBIR("De los cuales corresponden a cada sector: ")
    ESCRIBIR("Sector A: ", sec_a, ", con un ", sec_a ** 100 / total, "%.")
    ESCRIBIR("Sector C: ", sec_c, ", con un ", sec_c ** 100 / total, "%.")
    ESCRIBIR("Sector D: ", sec_d, ", con un ", sec_d ** 100 / total, "%.")

    CERRAR(ventas)
    CERRAR(salida)
FIN_ACCION
```

</details>

## Ejercicio 2

Dado el siguiente Enunciado, contestar los puntos que se enumeran en la Consigna. NO HACER EL ALGORITMO.

Enunciado:
La empresa de Servicios Energéticos de una Ciudad posee un archivo histórico desde el año 2000 hasta la actualidad
con todos los consumos de los usuarios ordenados por Barrio, Usuario y fecha de medición de la siguiente manera:

| Barrio | Usuario | fecha de medición | consumo |
|--------|---------|-------------------|---------|

Se pide:
1. Generar un archivo de salida con todos los consumos de los usuarios, cuyo registro tenga el siguiente formato:

| Barrio | Usuario | Consumo |
|--------|---------|---------|

2. Muestre por pantalla el total de consumo solo del año 2015, por cada barrio y el total general para toda la ciudad

Consigna:
1. Responda: cuantos niveles de corte hay? Enumere cuales son. Escriba el trozo de algoritmo donde se verifica si hay corte.
2. ¿Cuantos totalizadores se necesitan? Indicar cuales son (utilizar nombres descriptivos del valor que representan)
3. Escriba la subacción que permite cumplir con el punto a) del enunciado.

<details open>
<summary>Solución</summary>

1. Un solo corte, porque se pide discriminar los datos por barrio y total general, donde el último no requiere un corte.
```
SI resg_barrio <> reg.barrio ENTONCES
  corte_barrio()
FIN_SI
```

2. Se necesitan 2 totalizadores, 1 para el consumo de los usuarios por cada barrio y otro para el consumo general.

3.

```
PROCEDIMIENTO corte_barrio() ES
  ESCRIBIR("El consumo total registrado para el barrio ", resg_barrio,
  " fue de: ", cant_barrio)
  cant_gral := cant_gral + cant_barrio
  cant_barrio := 0
  resg_barrio := reg.barrio
FIN_PROCEDIMIENTO
```

</details>
