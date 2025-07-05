## Ejercicio 1
Un importante supermercado de la provincia del Chaco posee la información del stock de todos
sus artículos en una secuencia de datos.

**Formato de la secuencia:**
CodArtCodRubroStockNombreArticulo&CodArtCodRubroStockNombreArticulo&CodArtCodRubroStockNombreArticulo&FDS

Donde:
- CodArt (5 caracteres): código del artículo.
- CodRubro (1 carácter): se refiere al rubro del artículo, las opciones son: “L”: Limpieza, “F”: Fiambrería,
“C”: Carnicería, “B”: Bazar y “H”: Higiene.
- Stock (3 caracteres): cantidad de artículos en stock.
- NombreArticulo: es el nombre del artículo y finaliza con un “&”.

*Ejemplo de la secuencia:*
12345L789Detergente Magistral&23456F078Jamon Iberico& [...] &FDS

Además, se posee una secuencia de caracteres con todas las ventas realizadas para
los artículos (el fin de las ventas de cada artículo se indica con el carácter “#”).

**Formato de la secuencia:**
DiaMesFPFEUVDiaMesFPFEUVDiaMesFPFEUV#DiaMesFPFEUVDiaMesFPFEUVDiaMesFPFEUV# [...] #

Donde:
- Dia (2 caracteres): corresponde al día de la venta.
- Mes (2 caracteres): corresponde al mes de la venta.
- FP (1 carácter): indica forma de pago, las opciones son: “T”: Tarjeta de crédito – “C”: Contado.
- FE (1 carácter): indica forma de envío, las opciones son: “S”: Entregado en sucursal y “D”: Envío a domicilio.
- UV (2 caracteres): unidades vendidas.

Consideraciones:
- Existe una correspondencia uno a uno entre las 2 secuencias, de la siguiente forma: el primer grupo de
ventas corresponde al primer artículo, el siguiente al segundo y así sucesivamente.

Se pide:
1. Generar una nueva secuencia de salida con los nombres de todos los artículos que han quedado sin stock
(stock = 0). Para poder determinar el stock de un producto solo se deberán descontar las unidades cuya forma
de envío haya sido “Entregado en sucursal”.
2. Generar un informe de las ventas realizadas para un determinado mes que ingresa un usuario, con la siguiente
estructura:

| Nombre del Artículo | Cant. unid entregadas en suc | Cant. unid enviadas a domicilio |
|---------------------|------------------------------|---------------------------------|

```
ACCION ejercicio ES
  ACCION
    productos, ventas, salida: secuencia de caracter
    prod, ven, metodo: caracter
    unid, unid_dom, unid_sucur, stock: entero
    mes_dom, mes_sucur: entero
    mes_eleg, mes_ac: N(2)
    i, k: entero

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
    ARR(productos); AVZ(productos, prod)
    ARR(ventas); AVZ(ventas, ven)
    CREAR(salida)

    unid_dom := 0; unid_sucur := 0; unid := 0; stock := 0
    mes_ac := 0; mes_dom := 0; mes_sucur := 0

    ESCRIBIR("Ingrese un mes para obtener un reporte sobre las ventas
    para ese determinador mes, discriminando por producto: 1-12")
    LEER(mes_eleg)

    MIENTRAS NO FDS(productos) HACER
      PARA i := 1 HASTA 6 HACER
        AVZ(productos, prod)
      FIN_PARA

      PARA i := 2 HASTA 0, -1 HACER
        stock := stock + convertir(prod) * 10 ** i
        AVZ(productos, prod)
      FIN_PARA

      MIENTRAS ven <> '#' HACER
        AVZ(ventas, ven); AVZ(ventas, ven)

        PARA k := 1 HASTA 0, -1 HACER
          mes_ac := mes_ac + convertir(ven) * 10 ** k
          AVZ(ventas, ven)
        FIN_PARA

        AVZ(ventas, ven)
        metodo := car
        AVZ(ventas, ven)

        SEGUN j := 1 HASTA 0, -1 HACER
          unid := unid + convertir(ven) * 10 ** j
          AVZ(ventas, ven)
        FIN_MIENTRAS

        SEGUN metodo HACER
          'S': unid_sucur := unid_sucur + unid
          'D': unid_dom := unid_dom + unid
        FIN_SEGUN

        SI mes_eleg = mes_ac ENTONCES
          mes_sucur := mes_sucur + unid
          mes_dom := mes_dom + unid
        FIN_SI

        unid := 0; mes_ac := 0;
      FIN_MIENTRAS

      ESCRIBIR("Par el mes de ", mes_eleg, " los totales fueron: ")
      SI stock - unid_sucur = 0 ENTONCES
        MIENTRAS prod <> '&' HACER
          ESCRIBIR(prod)
          ESCRIBIR(salida, prod)
          AVZ(productos, prod)
        FIN_MIENTRAS
      CONTRARIO
        MIENTRAS prod <> '&' HACER
          ESCRIBIR(prod)
          AVZ(productos, prod)
        FIN_MIENTRAS
      FIN_SI

      ESCRIBIR("Unidades entregadas en sucursal: ", mes_sucur)
      ESCRIBIR("Unidades entregadas a domicilio: ", mes_dom)

      AVZ(productos, prod)
      AVZ(ventas, ven)

      unid := 0; unid_sucur := 0; unid_dom := 0;
      stock := 0; mes_sucur := 0; mes_dom := 0;
    FIN_MIENTRAS

    CERRAR(productos)
    CERRAR(ventas)
    CERRAR(salida)
FIN_ACCION
```

## Ejercicio 2
Consigna: la misma cadena de supermercados, además cuenta con un archivo secuencial con el stock
de todos sus artículos con el siguiente formato:

Stock: ordenado por Código sucursal, Rubro y Código Artículo.

| Cod Suc N(2) | Rubro AN(20) | Cod Articulo N(5) | FechaUltRep | Stock de seguridad | Stock actual |
|--------------|--------------|-------------------|-------------|--------------------|--------------|

Consideraciones:
- FechaUltRep: fecha última reposición.
- El stock de seguridad es el nivel mínimo de existencias que se debe mantener en almacén.

Se pide:
1. Generar un informe de totales por sucursal, por rubro y total general de cantidad de artículos
cuya fecha de última reposición sea anterior a una fecha ingresada por el usuario.
2. Generar un archivo de salida que contenga todos los artículos del rubro “Bazar” cuya fecha de
última reposición sea anterior a la fecha ingresada por el usuario. Debe contener sucursal y
código de articulo.

```
ACCION ejercicio ES
  AMBIENTE
    Fecha = REGISTRO
      dia: 1..31
      mes: 1..12
      año: N(4)
    FIN_REGISTRO

    Stock = REGISTRO
      cod_suc: N(2)
      rubro: AN(20)
      cod_art: N(5)
      fecha_rep: Fecha
      stock_seg: entero
      stock_ac: entero
    FIN_REGISTRO

    Informe = REGISTRO
      cod_suc: N(2)
      cod_art: N(5)
    FIN_REGISTRO

    entrada: archivo de Stock ordenado por cod_suc, rubro, cod_art
    ficha: Stock
    salida: arch de Informe
    inf: Informe

    dia_eleg, mes_eleg, año_eleg: entero

    condicion: logico
    cant_suc, cant_rubro, cant_gral: entero
    resg_suc: N(2)
    resg_rubro: AN(20)

    PROCEDIMIENTO corte_rubro() ES
      ESCRIBIR("La cantidad de articulos cuya ultima fecha de reposición fue anterior
      a la ingresada, para el rubro ", resg_rubro, " fue de ", cant_rubro)
      cant_suc := cant_suc + cant_rubro
      cant_rubro := 0
      resg_rubro := ficha.rubro
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_sucur() ES
      corte_rubro()
      ESCRIBIR("La cantidad de articulos cuya ultima fecha de reposición fue anterior
      a la ingresada para la sucursal: ", resg_suc, " fue de ", cant_suc, " articulos.")
      cant_gral := cant_gral + cant_suc
      cant_suc := 0
      resg_suc := ficha.cod_suc
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (entrada); LEER(entrada, ficha)
    ABRIR /S (salida)

    resg_suc := ficha.cod_suc; resg_rubro := ficha.rubro
    cant_gral := 0; cant_rubro := 0; cant_suc := 0;

    ESCRIBIR("A continuacion ingrese la fecha para la cual se desea saber
    los articulos cuya ultima reposicion fue anterior a ella")
    ESCRIBIR("DIA: "); LEER(dia_eleg)
    ESCRIBIR("MES: "); LEER(mes_eleg)
    ESCRIBIR("AÑO: "); LEER(año_eleg)

    MIENTRAS NO FDA(entrada) HACER
      SI resg_suc <> ficha.cod_rubro ENTONCES
        corte_sucur()
      CONTRARIO
        SI resg_rubro <> ficha.rubro ENTONCES
          corte_rubro()
        FIN_SI
      FIN_SI

      SI año_eleg == ficha.fecha_rep.mes ENTONCES
        SI mes_eleg >= ficha.fecha_rep.mes ENTONCES
          SI dia_eleg > ficha.fecha_rep.dia ENTONCES
            cond := verdadero
          FIN_SI
        FIN_SI
      FIN_SI

      SI cond ENTONCES
        cant_rubro := cant_rubro + 1
      FIN_SI

      SI cond Y ficha.rubro = "Bazar" ENTONCES
        inf.cod_suc := ficha.cod_suc
        inf.cod_art := ficha.cod_art
        GRABAR(salida, inf)
      FIN_SI

      LEER(entrada, ficha)
    FIN_MIENTRAS

    CERRAR(entrada)
    CERRAR(salida)
FIN_ACCION
```
