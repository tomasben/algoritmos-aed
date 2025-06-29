## Ejercicio 1
Consigna: un importante supermercado de la provincia del Chaco posee la información del stock de todos
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
