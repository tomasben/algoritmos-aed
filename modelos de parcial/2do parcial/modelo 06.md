## Ejercicio 1
La empresa de cruceros "TIBET" cuenta con dos archivos VENTAS, donde se almacenan
las ventas realizadas dentro del shopping de cada barco y otro de PRODUCTOS donde
se registran datos de las marcas disponibles en el shopping.

**VENTAS:** *Ordenado por Nro_Venta*
| Nro_Venta N(6) | Nro_Pro N(6) | Barco (1, 2, 3) | TipoVenta N(2) |
|----------------|--------------|-----------------|----------------|

Estado ("D" = disponible | "FT" = Fuera de Temporada)

Al finalizar el día, se realiza una depuración del archivo de PRODUCTOS y lo actualiza.
La actualización debe realizarse según los siguientes puntos:

- Se debe realizar la baja del archivo PRODUCTOS, a aquellos que contengan algún
registro de venta con estado "FT".
- Se debe modificar el campo "CAT" del archivo PRODUCTOS a la máxima categoría si
alguna venta es del TipoVenta = "Premium" (código de tipo venta=10).

**PRODUCTOS:** *Indexado por Barco y NroPro*
| **Barco (1, 2, 3)** | **Nro_Pro N(6)** | Tipo ("I" = Indumentaria - "P" = Perfumería) | TipoVent N(2) | Fumador (SI/NO) | CAT (1, 2, 3) |
|---------------------|------------------|----------------------------------------------|---------------|-----------------|---------------|

"TIBET" considera 10 tipos de ventas, cuyas nombres de las categorías se almacenan
en un arreglo donde cada posición se corresponde con el código del tipo de venta
(por ejemplo la posición 2 del arreglo es el TipoVenta = 2).

Se pide:
1. Actualizar el archivo PRODUCTOS
2. Imprimir un informe que indique la cantidad de ventas cuyo tipo sea 2 y 5.
3. Incluir en el informe el porcentaje total de ventas fuera de temporada, considerando
todas las que pertenecen a los servicios considerados (2 y 5).

## Ejercicio 2
Dado el escenario anterior, ahora se pide un algoritmo que ayude a tomar decisiones
a partir de las ventas registradas durante el primer semestre del 2017 en los diferentes
tipos de negocios que ofrecen sus barcos. Para ello cuentan con un archivo de TOTALES.

**TOTALES**
| **Barco (1, 2, 3)** | Fecha | Tipo ("I" = Indumentaria - "P" = Perfumería) | Importe N(7,2) |
|---------------------|-------|----------------------------------------------|----------------|

Se pide:
1. Informar el tipo, con mayor importe total de ventas, en qué mes y barco ocurrió
2. Informar para cada Barco, en que mes se recaudó menos
