## Ejercicio 1
Una Empresa que distribuye productos farmacéuticos dispone de una secuencia de
caracteres con la siguiente información sobre sus productos:

- Venta libre o con receta: VL - RE (2 caracteres)
- Línea terapéutica: A(antiinflamatorio) – G(gastroenterológica) – R(respiratoria/antialérgica)(1 carácter)
- Nombre del producto: cantidad no conocida de caracteres, finaliza con el carácter #

Se ubican agrupados por Laboratorios, al inicio de cada grupo está el nombre del laboratorio
y luego un guión, y el fin de cada grupo se indica @.

*Ejemplo:*
PharmaS.A.-VLAibuflash#REAcalmidol#REGlanzopral#VLRalerpriv#...#...#@Tecnoquimica-VLGsertal#VLAibuprofeno#...#...#@Bago-...#...#@FDS

La empresa solicita:
1. Generar dos secuencias de salida a fin de disponer, por separado, los datos de
los productos que son de “venta libre” y los que son de venta “con receta”; los datos
que le interesa tener son: línea terapéutica y nombre del producto, indicando el fin
de cada producto con el carácter #.

*Ejemplo:* Aibuflash#Ralerpriv#Gsertal#Aibuprofeno#...#...#...#FDS

2. Se pide además un listado (por pantalla) de cantidad de productos de venta “con receta”
de la línea “gastroenterológica”, por Laboratorio. Por ejemplo:

**Laboratorio**		**Cantidad**
PharmaS.A:		    50
Tecnoquimica:		  87
Bago:		          23

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    medicamentos, receta, libre: secuencia de caracter
    car: caracter
    cant_gast
  PROCESO
    ARR(medicamentos); AVZ(medicamentos, car)
    CREAR(receta)
    CREAR(libre)

    MIENTRAS NO FDS(medicamentos) HACER
      ESCRIBIR("Para el laboratorio: ")
      MIENTRAS car <> '-' HACER
        ESCRIBIR(car)
        AVZ(medicamentos, car)
      FIN_MIENTRAS
      AVZ(medicamentos, car)

      cant_gast := 0
      MIENTRAS car <> '@' HACER
        SI car = 'R' ENTONCES
          AVZ(medicamentos, car)
          AVZ(medicamentos, car)

          SI car = 'G' ENTONCES
            cant_gast := cant_gast + 1
          FIN_SI
          ESCRIBIR(receta, car)
          AVZ(medicamentos, car)

          MIENTRAS car <> '#' HACER
            ESCRIBIR(receta, car)
            AVZ(medicamentos, car)
          FIN_MIENTRAS
          ESCRIBIR(receta, car)
          AVZ(medicamentos, car)
        CONTRARIO
          AVZ(medicamentos, car)
          AVZ(medicamentos, car)

          SI car = 'G' ENTONCES
            cant_gast := cant_gast + 1
          FIN_SI
          ESCRIBIR(libre, car)
          AVZ(medicamentos, car)

          MIENTRAS car <> '#' HACER
            ESCRIBIR(receta, car)
            AVZ(medicamentos, car)
          FIN_MIENTRAS         MIENTRAS car <> '#' HACER

          ESCRIBIR(receta, car)
          AVZ(medicamentos, car)
        FIN_SI
      FIN_MIENTRAS
      ESCRIBIR("Cantidad de medicamentos de línea gastroenterológica: ", cant_gast)
    FIN_MIENTRAS

    CERRAR(medicamentos)
    CERRAR(receta)
    CERRAR(libre)
FIN_ACCION
```

</details>

## Ejercicio 2
a misma Empresa del ejercicio 1 dispone de un archivo secuencial con la siguiente
información de su stock de productos, ordenado por laboratorio, código de producto
y lote.

| Laboratorio N(3) | Código Producto N(4) | Lote AN(5) | Descripción AN(150) | Cantidad N(4) | Fecha_vencimiento (dd-mm-aaaa) |
|------------------|----------------------|------------|---------------------|---------------|--------------------------------|

Hay varios registros para cada código de producto, con distintos números de lote,
el cual es único. La Empresa necesita:
1. Generar otro archivo de salida que contenga los lotes vencidos (cuya fecha de
vencimiento sea posterior a la actual), con el siguiente formato:

| Laboratorio N(3) | Código Producto N(4) |	Lote AN(5) | Cantidad N(4) | Fecha_vencimiento (aaaa-mm-dd) |
|------------------|----------------------|------------|---------------|--------------------------------|

2. Mostrar por pantalla la cantidad total de productos vencidos por Laboratorio,
Código de Producto y total General.
3. Al final informar cuál fue el laboratorio con mayor cantidad de productos vencidos

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

    Producto = REGISTRO
      lab: N(3)
      cod_prod: N(4)
      lote: AN(5)
      desc: AN(150)
      cant: N(4)
      vencimiento: Fecha
    FIN_REGISTRO

    Informe = REGISTRO
      lab: N(3)
      cod_prod: N(4)
      lote: AN(5)
      cant: N(4)
      vencimiento: Fecha
    FIN_REGISTRO

    stock: archivo de Producto ordenado por lab, cod_prod, lote
    prod: Producto
    salida: archivo de Informe
    inf: Informe

    actual: Fecha
    cant_gral, cant_lab, cant_prod, may_venc: entero
    resg_lab, may_venc_lab: N(3)
    resg_prod: N(4)

    PROCEDIMIENTO corte_laboratorio() ES
      corte_producto()
      ESCRIBIR("La cantidad de productos vencidos para el laboratorio N° ", resg_lab,
      " es de: ", cant_lab, " productos.")
      cant_gral := cant_gral + cant_lab

      SI may_venc > cant_lab ENTONCES
        may_venc := cant_lab
        may_venc_lab := resg_lab
      FIN_SI

      resg_lab := prod.lab
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_producto() ES
      ESCRIBIR("El número de productos vencidos con código ", resg_prod
      " es de: ", cant_prod, " productos vencidos.")
      cant_lab := cant_lab + cant_prod
      cant_prod := 0
      resg_prod := prod.cod_prod
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (stock); LEER(stock, prod)
    CREAR(salida)

    resg_lab := prod.lab; resg_prod := prod.cod_prod
    cant_gral := 0; cant_lab := 0; cant_prod := 0

    ESCRIBIR("Ingrese la fecha actual para conocer los productos de la farmacéutica que ya hayan vencidos")
    ESCRIBIR("Año: "); LEER(actual.año)
    ESCRIBIR("Mes: "); LEER(actual.mes)
    ESCRIBIR("Día: "); LEER(actual.dia)

    MIENTRAS NO FDA(stock) HACER
      SI resg_lab <> prod.lab ENTONCES
        corte_laboratorio()
      CONTRARIO
        SI resg_prod <> prod.cod_prod ENTONCES
          corte_producto()
        FIN_SI
      FIN_SI

      SI actual.año >= prod.vencimiento.año ENTONCES
        SI actual.mes >= prod.vencimiento.mes ENTONCES
          SI actual.dia > prod.vencimiento.dia ENTONES
            cant_prod := cant_prod + prod.cant

            inf.lab := prod.lab
            inf.cod_prod := prod.lab
            inf.lote := prod.lote
            inf.cant := prod.cant
            inf.vencimiento := prod.vencimiento
            ESCRIBIR(salida, inf)
          FIN_SI
        FIN_SI
      FIN_SI

      LEER(stock, prod)
    FIN_MIENTRAS
    corte_laboratorio()

    ESCRIBIR("La cantidad productos vencidos al dia ingresado: ", actual.dia, "-", actual.mes, "-", actual.año,
    " es de: ", cant_gral, " productos vencidos.")
    ESCRIBIR("Y el laboratorio con la mayor cantidad de estos fue el nro ", may_venc_lab,
    " con un total de ", may_venc, " productos vencidos.")

    CERRAR(stock)
    CERRAR(entrada)
FIN_ACCION
```

</details>
