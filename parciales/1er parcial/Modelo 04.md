## Ejercicio 1
Se lanzó la preventa del Primavera Sound 2023, la modalidad que se elige es lanzar
una preventa de entradas, sin anunciar los artistas que se presentarán. Los early birds #1
(preventa de entradas), se lanzarán el 1 de mayo de 2023 a las 13:00 hs, pero los fanáticos
pueden hacer “fila virtual” desde las 00:00 para asegurar su lugar en el famoso festival, una
vez que se lance la venta virtual los usuarios pueden ir comprando las entradas de a tandas.

Con la finalidad de analizar si se debe optimizar el rendimiento de la plataforma, se disponen
dos secuencias de caracteres. La primera secuencia contiene a los fanáticos que hacen la
“fila virtual”, esta secuencia contiene la hora en la que se registró en la fila (hhmm), el número
en la fila (6 caracteres), el medio de pago con el que piensa pagar (“T”- tarjeta, “C”-efectivo,
“E”-transferencia) y cuántas entradas piensa comprar (como máximo puede comprar 5 entradas).

**Formato de la secuencia Fila_Virtual:**
horafilanumerofilamediopagocantentradas#

*Ejemplo de la secuencia Fila_Virtual:*
0301123456T3#0345234567E4#

En estos sistemas de fila, al colocarse en ella se obtiene un identificador o número de fila,
pero recién el usuario inicia sesión al llegar a su lugar en la fila y entrar a la sección de Compras.

En una segunda secuencia se encuentran las compras reales realizadas, esta secuencia contiene el número
en la fila (6 caracteres), el nombre de usuario (cantidad indefinida, termina en “+”) y luego contiene
los datos de para quién es cada entrada en la compra, incluyendo su DNI y nombre (separados con ‘.’).
Una compra finaliza con un “?”.

**Formato de la secuencia Compras:**
numerofilanombre_usuario+dninombre.dninombre.dninombre?

*Ejemplo de la secuencia Compras:*
123456unsuario+33254787Juan.27895614Melisa.36257489Pedro?

Si por algún motivo algún fanático deja su lugar en la fila, en la secuencia de Compras en nombre de
usuario aparece un carácter “#”, el signo “+” y luego la marca “?”. Esto implica una correspondencia
1 a 1 entre las dos secuencias.

Se pide:
1. Generar una secuencia de salida con los nombres de usuario y cada DNI de las entradas compradas que
fueron pagadas con tarjeta. Separar cada campo con un + y finalizar con “#” al completar la compra de
un usuario. EJ: nombreusuario+dni+dni#nombreusuario+dni+dni#
2. Se desea conocer cuántos usuarios compraron una cantidad de entradas distinta a la que declararon
en la fila virtual.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    fila, compras, salida: secuencia de caracter
    lug, fac: caracter
    i, k, j: entero
    esperadas, compradas, cant_dist: entero
    metodo: caracter

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
    ARR(fila); AVZ(fila, lug)
    ARR(compras); AVZ(compras, fac)
    CREAR(salida)

    cant_dist := 0

    MIENTRAS NO FDS(fila) HACER
      // avanzo los datos irrelevantes del usuario en la fila
      // 4 por la hora y 6 por el numero de fila
      PARA i := 1 hasta 10 HACER
        AVZ(fila, lug)
      FIN_PAR

      metodo := lug
      AVZ(fila, lug)

      esperadas := convertir(lug)
      AVZ(fila, lug)
      // avanzo el '#' para llegar al siguiente usuario en fila o final de secuencia
      AVZ(fila, lug)

      PARA k := 1 HASTA 6 HACER
        AVZ(compras, fac)
      FIN_PARA

      compradas := 0

      // comparo el caracter actual para saber si un usuario abandono la fila
      // si es '#' quiere decir que abandono y la secuencia es "#+?"
      SI fac <> '#' ENTONCES
        MIENTRAS fac <> '+' HACER
          SI metodo = 'T' ENTONCES
            ESCRIBIR(salida, fac)
          FIN_SI

          AVZ(compras, fac)
        FIN_MIENTRAS

        SI metodo = 'T' ENTONCES
          ESCRIBIR(salida, '+')
        FIN_SI

        MIENTRAS fac <> '?' HACER
          AVZ(compras, car)

          MIENTRAS fac <> '.' Y fac <> '?' HACER
            AVZ(compras, fac)
          FIN_MIENTRAS

          compradas := compradas + 1
        FIN_MIENTRAS
        AVZ(compras, fac)

        SI metodo = 'T' ENTONCES
          ESCRIBIR(salida, '#')
        FIN_SI

        SI compradas <> esperadas ENTONCES
          cant_dist := cant_dist + 1
        FIN_SI
      CONTRARIO
        // avanzo los caracteres '#', '+' y '?'
        AVZ(compras, fac)
        AVZ(compras, fac)
        AVZ(compras, fac)
      FIN_SI
    FIN_MIENTRAS

    ESCRIBIR("La cantidad de usuarios que compraron una cantidad de entradas
    diferente a la declarada fue de: ", cant_dist, " usuarios.")

    CERRAR(fila)
    CERRAR(compras)
    CERRAR(salida)
FIN_ACCION
```

</details>

## Ejercicio 2
Basados en el escenario del ejercicio 1, se tiene un archivo secuencial que contiene las informaciones
de ventas finales de entradas para el festival, realizadas desde el 1 de mayo del 2023 hasta el 1 de
julio de 2023.

VENTAS: ordenado por provincia, ciudad, plataforma y fecha.

| Provincia | Ciudad | Plataforma | Fecha | Entradas |
|-----------|--------|------------|-------|----------|

Se pide:
1. Generar un archivo de salida que contenga datos de las ciudades en las cuales la cantidad total de
entradas vendidas supera las 1000 con el siguiente formato:

| Provincia | Ciudad | Entradas |
|-----------|--------|----------|

2. Informar el total de ventas del 1 de junio al 1 julio, discriminado por plataforma y ciudad.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Fecha = REGISTRO
      dia: 1..31
      mes: 1..12
      año: N(4)
    FIN_REGISTRO

    Ticket = REGISTRO
      provincia: AN(30)
      ciudad: AN(30)
      plataforma: N(2)
      fecha: Fecha
      entradas: N(1)
    FIN_REGISTRO

    Informe = REGISTRO
      provincia: AN(30)
      ciudad: AN(30)
      entradas: N(5)
    FIN_REGISTRO

    ventas: archivo de Ticket ordenado por provincia, ciudad, plataforma, fecha
    tik: Ticket
    salida: archivo de Informe
    inf: Informe

    cant_plat, cant_ciud: entero
    resg_plat: N(2)
    resg_ciud: AN(30)

    PROCEDIMIENTO corte_ciudad() ES
      corte_plataforma()
      ESCRIBIR("El total de entradas vendidas desde el 1 de junio y hasta el 1 de julio
      para la ciudad ", resg_ciud, " fue de: ", cant_ciud, " entradas.")

      SI cant_ciud > 100 ENTONCES
        inf.provincia := tik.provincia
        inf.ciudad := resg_ciud
        inf.entradas := cant_ciud
        ESCRIBIR(salida, inf)
      FIN_SI

      cant_ciud := 0
      resg_ciud := tik.ciudad
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_plataforma() ES
      ESCRIBIR("El total de entradas vendidas desde el 1 de junio hasta el 1 de julio para
      la plataforma ", resg_plat, " fue de: ", cant_plat, " entradas.")
      cant_ciud := cant_ciud + cant_plat
      cant_plat := 0
      resg_plat := tik.plataforma
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (ventas); LEER(ventas, tik)
    ABRIR /S (salida)

    resg_ciud := tik.ciudad; resg_plat := tik.plataforma
    cant_plat := 0; cant_ciud := 0

    MIENTRAS NO FDA(ventas) HACER
      SI resg_ciud <> tik.ciudad ENTONCES
        corte_ciudad()
      CONTRARIO
        SI resg_plat <> tik.plataforma ENTONCES
          corte_plataforma()
        FIN_SI
      FIN_SI

      SI tik.fecha.año = 2023 ENTONCES
        SI tik.fecha.mes = 6 ENTONCES
          cant_plat := cant_plat + tik.entradas
        FIN_SI
      FIN_SI

      LEER(ventas, tik)
    FIN_MIENTRAS

    CERRAR(ventas)
    CERRAR(salida)
FIN_ACCION
```

</details>
