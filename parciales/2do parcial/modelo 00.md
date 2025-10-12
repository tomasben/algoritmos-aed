## Ejercicio 1
Un importante banco del país cuenta con la información de todos sus clientes en
un archivo secuencial con el siguiente formato:

**CLIENTES** *ordenado por id_sucursal, id_cliente*
| **id_sucursal** | **id_cliente** | nombre y apellido | saldo a la fecha | fecha alta | fecha baja |
|-----------------|----------------|-------------------|------------------|------------|------------|

Al final de cada mes, corre un proceso de actualización con todos los movimientos
generados por cada cliente durante el mes.

La información se encuentra en un archivo secuencial con la siguiente estructura:

**MOVIMIENTOS** *ordenado por id_sucursal, id_cliente, cod_movimiento*
| **id_sucursal** | **id_cliente** | **cod_movimiento** (0..99) | nombre y apellido | fecha_movimiento | monto | detalle | categoría (1..6) | tipo |
|-----------------|----------------|----------------------------|-------------------|------------------|-------|---------|------------------|------|

Donde:
- cod_movimiento indica: 0 (alta de un nuevo cliente), 99 (baja de un cliente),
y cualquier otro valor entre 1 y 98 es una transacción en la cuenta del cliente.
- detalle: indica una descripción del movimiento.
- categoría: indica la categoría del movimiento (1-Supermercado, 2-Farmacia,
3-Carniceria, 4-Transferencia, 5-Pago de servicios, 6-Otros).
- tipo: indica "I" si es un ingreso, "E" si es un egreso.

Se pide:
1. Desarrollar un algoritmo que permita mantener actualizado el archivo CLIENTES
con sus respectivos saldos. Informar por pantalla cualquier tipo de error que
considere pertinente durante el proceso.
2. Indicar la cantidad de clientes nuevos que se produjeron durante el proceso.

## Ejercicio 2
El banco ha solicitado un informe para conocer cómo se integra su cartera de clientes,
agrupándolos por sucursal y categoría de cliente, a partir de los datos del archivo
de CLIENTES (usar las estructuras de datos del ejercicio anterior).

Considerando que son 15 sucursales, y la información de las sucursales se encuentra
en un archivo indexado:

**Sucursales** *indexado por id_sucursal*
| **id sucursal** | nombre de la sucursal | direccion | localidad |
|-----------------|-----------------------|-----------|-----------|

La estructura del informe solicitado es la siguiente:

|                     | Categoría diamante | Categoría oro |	Categoría estándar | Totales por suc. |
|:-------------------:|:------------------:|:-------------:|:-------------------:|:----------------:|
| Nombre sucursal 1   |                    |               |                     |                  |
| Nombre sucursal 2	  |                    |               |                     |                  |
| ...                 |                    |               |                     |                  |
| Nombre sucursal 15  |                    |               |                     |                  |
| Totales x categoría |                    |               |                     |                  |

La categoría del cliente dependerá de los montos obtenidos en su saldo de la cuenta
al último día del mes.
- Montos menores a $100.000 serán de categoría estándar.
- Montos menores a $1.500.000 serán de categoría oro.
- Montos superiores serán de categoría diamante.

*Nota:* no considerar clientes dados de baja.
