## Ejercicio 1
1- Una cadena de restaurantes de la ciudad de Resistencia necesita realizar un
informe con todos los comentarios que realizaron los clientes, para ello cuenta
con dos secuencias de caracteres con el siguiente formato:

**Secuencia Comentarios:**
Contiene los comentarios realizados, cada comentario finaliza con el carácter #,
están agrupados por restaurante, el fin de cada grupo se indica con el carácter @
y el fin de la secuencia con una marca *. Posee la siguiente información:

puntuación (del 01 al 10), la fecha en que se realizó el comentario (en formato AAAAMMDD),
si fue una cena o un almuerzo (C o A), la cantidad de personas que asistieron (2 dígitos),
luego de estos datos posee un comentario (palabras y espacios) con un máximo de 999 caracteres.

**Secuencia Restaurantes:**
Es una secuencia de caracteres, que contiene el nombre y la dirección (palabras y espacios)
separados por una coma. Cada restaurante termina con un . y la secuencia termina con un *.

Se pide generar una secuencia de salida de caracteres que posea todos los comentarios donde
la puntuación sea menor o igual a 4, con el siguiente formato:

para cada restaurante se copia el nombre una sola vez y luego todos los comentarios que le
pertenecen, de la siguiente manera:

...nombre del restaurante - puntuación(01, 02, 03 o 04), fecha en que se realizó el comentario
(formato AAAAMMDD), comentario que finaliza con el carácter #, y al finalizar mostrar la cantidad
de palabras del comentario (3 caracteres)....otro comentario...otro comentario...@

Se pide al final:
1. Informar cantidad de comentarios con puntuación perfecta (10 a 8), buena (7 a 5) o mala (de 4 a 1).
2. Cantidad promedio de personas por restaurante.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    restaurantes, comentarios, salida: secuencia de caracter
    res, com: caracter
    i, j, k, punt: entero
    promedio: real
    cant_pal, cant_pers, cant_res, cant_perf, cant_buen, cant_mala: entero

    FUNCION convertir_car(car: caracter): entero ES
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
        FIN_SEGUN
    FIN_FUNCION

    FUNCION convertir_num(num: entero): caracter ES
        SEGUN num HACER
          1: convertir := "1"
          2: convertir := "2"
          3: convertir := "3"
          4: convertir := "4"
          5: convertir := "5"
          6: convertir := "6"
          7: convertir := "7"
          8: convertir := "8"
          9: convertir := "9"
        FIN_SEGUN
    FIN_FUNCIÓN
  PROCESO
    ARR(restaurantes); AVZ(restaurantes, res)
    ARR(comentarios); AVZ(comentarios, com)
    CREAR(salida)

    cant_perf := 0; cant_buen := 0; cant_mala := 0
    cant_res := 0

    MIENTRAS res <> '*' HACER
      cant_res := cant_res + 1

      MIENTRAS res <> ',' HACER
        ESCRIBIR(salida, res)
        AVZ(restaurantes, res)
      FIN_MIENTRAS
      ESCRIBIR(salida, '-')
      AVZ(restaurantes, res)

      MIENTRAS res <> '.' HACER
        AVZ(restaurantes, res)
      FIN_MIENTRAS
      AVZ(restaurantes, res)

      MIENTRAS com <> '@' HACER
        punt := convertir(com) * 10
        AVZ(comentarios, com)
        punt := punt + convertir_car(com)

        SEGUN punt HACER
          >= 8: cant_perf := cant_perf + 1
          >= 5: cant_perf := cant_buen + 1
          OTRO: cant_mal := cant_mal + 1
        FIN_SEGUN

        SI punt <= 4 ENTONCES
          ESCRIBIR(salida, '0')
          ESCRIBIR(salida, com)
          AVZ(comentarios,com)

          PARA i := 1 HASTA 8 HACER
            ESCRIBIR(salida, com)
            AVZ(comentarios, com)
          FIN_PARA
          AVZ(comentarios, com)

          PARA j := 1 HASTA 0, -1 HACER
            cant_pers := cant_pers + convertir_car(com) * 10 ** j
            AVZ(comentarios, com)
          FIN_PARA

          cant_pal := 0
          MIENTRAS com <> '.' HACER
            cant_pal := cant_pal + 1

            MIENTRAS com <> ' ' O com <> '.' HACER
              AVZ(comentarios, com)
            FIN_MIENTRAS
            AVZ(comentarios, com)
          FIN_MIENTRAS
          AVZ(comentarios, com)
          ESCRIBIR(salida, '#')
          ESCRIBIR(salida, convertir_num(cant_pal DIV 10))
          ESCRIBIR(salida, convertir_num(cant_pal MOD 10))
        CONTRARIO
          PARA k := 1 HASTA 11 HACER
            AVZ(comentarios, com)
          FIN_PARA

          PARA j := 1 HASTA 0, -1 HACER
            cant_pers := cant_pers + convertir_car(com) * 10 ** j
            AVZ(comentarios, com)
          FIN_PARA

          MIENTRAS com <> '.' HACER
            AVZ(comentarios, com)
          FIN_MIENTRAS
          AVZ(comentarios, com)
        FIN_SI
      FIN_MIENTRAS
      ESCRIBIR(salida, com)
      AVZ(comentarios, com)
    FIN_MIENTRAS

    promedio := cant_pers / cant_res
    ESCRIBIR("El promedio de clientes por restaurante fue de: ", promedio, " personas.")

    ESCRIBIR("La cantidad de reviews segun su valoracion fueron: ")
    ESCRIBIR("Valoración perfecta: ", cant_perf)
    ESCRIBIR("Valoración buena: ", cant_buen)
    ESCRIBIR("Valoración mala: ", cant_mal)

    CERRAR(restaurantes)
    CERRAR(comentarios)
    CERRAR(salida)
FIN_ACCION
```

</details>

## Ejercicio 2
Un supermercado se encuentra ante la lamentable situación de aumentar el precio a sus productos.
Para realizar esta acción posee el siguiente archivo secuencial, ordenado por tipo y calidad:

| tipo | calidad | código_producto | nombre AN(150) | precio_unitario | stock_actual |
|------|---------|-----------------|----------------|-----------------|--------------|

El campo tipo se codificó del 1 al 10 y la calidad del producto se codificó del 1 al 5.

Se pide generar un archivo de salida con el siguiente formato:

| código_producto | nombre AN(150) | precio_viejo | precio_nuevo | Porcentaje_de_aumento |
|-----------------|----------------|--------------|--------------|-----------------------|

El aumento que se debe tener en cuenta en cada producto está dado por los campos tipo y calidad
según los siguientes criterios:
- Para el caso de que el stock_actual sea 0, el producto no debe aparecer en el archivo de salida.
- Si el tipo es del 1 al 5: se debe aumentar un 50 % el precio.
- Si el tipo es del 6 al 10: se debe tener en cuenta la calidad, en caso de ser 1 o 2, se aumentará
un 30% el valor del producto. Para los otros casos (calidad 3, 4 o 5) el aumento es del 40%.

Se solicita además: Mostrar por pantalla, para cada tipo y calidad y total general, cuantos productos
existen.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Producto = REGISTRO
      tipo: 1..10
      calidad: 1..5
      cod_prod: AN(15)
      nombre: AN(150)
      precio: real
      stock: entero
    FIN_REGISTRO

    Actualizacion = REGISTRO
      cod_prod: AN(15)
      nombre: AN(150)
      precio_antig: real
      precio_nuevo: real
      aumento_porc: entero
    FIN_REGISTRO

    stock: archivo de Producto ordenado por tipo, calidad
    prod: Producto
    salida: archivo de Actualizacion
    act: Actualizacion

    cant_gral, cant_tipo, cant_calidad: entero
    resg_tipo, resg_calidad: entero

    PROCEDIMIENTO corte_tipo() ES
      corte_calidad()
      ESCRIBIR("Para el tipo de producto ", resg_tipo, " existen ", cant_tipo, " unidades.")
      cant_gral := cant_gral + cant_tipo
      cant_tipo := 0
      resg_tipo := prod.tipo
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_calidad() ES
      ESCRIBIR("Para el nivel de calidad ", resg_calidad, " existen: ",
      cant_calidad, " unidades de producto.")
      cant_tipo := cant_tipo + cant_calidad
      cant_calidad := 0
      resg_calidad := prod.calidad
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (stock); LEER(stock, prod)
    ABRIR /S (salida)

    resg_tipo := prod.tipo; resg_calidad := prod.tipo
    cant_gral := 0; cant_tipo := 0; cant_calidad := 0

    MIENTRAS NO FDA(entrada) HACER
      SI resg_tipo <> prod.tipo ENTONCES
        corte_tipo()
      CONTRARIO
        SI resg_calidad <> prod.calidad ENTONCES
          corte_calidad()
        FIN_SI
      FIN_SI

      SI prod.stock > 0 ENTONCES
        act.cod_prod := prod.cod_prod
        act.nombre := prod.nombre
        act.precio_antig := prod.precio

        SI prod.tipo en <= 5 ENTONCES
          act.precio_nuevo := prod.precio * 1.50
          act.aumento_porc := 50
        CONTRARIO
          SI prod.calidad <= 2 ENTONCES
            act.precio_nuevo := prod.precio * 1.30
            act.aumento_porc := 30
          CONTRARIO
            act.precio_nuevo := prod.precio * 1.40
            act.aumento_porc := 40
          FIN_SI
        FIN_SI

        ESCRIBIR(salida, act)
      FIN_SI

      LEER(stock, prod)
    FIN_MIENTRAS
    corte_tipo()

    ESCRIBIR("La cantidad total de productos en stock actualmente es de: ", cant_gral, " productos.")

    CERRAR(stock)
    CERRAR(salida)
FIN_ACCION
```

</details>
