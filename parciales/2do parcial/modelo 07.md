## Ejercicio 1
Una importante empresa de Turismo de la ciudad de Resistencia ha realizado a comienzos
de año la venta de PAQUETES TURISTICOS con la posibilidad de que los clientes puedan ir
pagando las cuotas mensualmente. Para premiar a los clientes con flexibilidad para
realizar pagos durante todo este año, ya que en el último mes se correría un proceso que
actualizará el estado de los clientes en su saldo.

La información de todos los clientes se encuentra dentro de un archivo secuencial, con el
siguiente formato:

**CLIENTES:**, *ordenado por nro_cliente*
| nro_cliente | apellido, nombre | dni | id_paquete | saldo | estado | categoria | puntos | fecha_baja |
|-------------|------------------|-----|------------|-------|--------|-----------|--------|------------|

El campo saldo indica el "SALDO" que el paquete se encuentra pagando en su totalidad.
"SALDO A FAVOR" si el cliente, luego del proceso de recuentos de pagos, tiene un saldo
a favor, o bien "DEUDOR" en caso de que el cliente no haya llegado a pagar la totalidad
del costo del paquete turístico.

Además, las categorías de la empresa están agrupados por categorías, lo cual les permite
acceder a importantes descuentos. Las categorías pueden ser: SIMPLE, PLATA, ORO, DIAMANTE.

Todos los clientes que se dan de alta por primera vez en la empresa acceden a la categoría
SIMPLE. Los clientes en categoría PLATA tienen una bonificación del 10% y suman 10 puntos
por el paquete adquirido. Los clientes en categoría ORO tienen una bonificación del 15% y
suman 20 puntos por el paquete adquirido. Los clientes en categoría DIAMANTE tienen una
bonificación del 20% y además suman 30 puntos por el paquete adquirido.

La información de todos los movimientos de los clientes se encuentra dentro de un archivo
secuencial, con el siguiente formato:

**NOVEDADES**, *ordenado por nro_cliente, nro_novedad*
| nro_cliente | nro_novedad | apellido_nombre | dni | id_paquete | fecha_novedad | monto |
|-------------|-------------|-----------------|-----|------------|---------------|-------|

Si el nro_novedad = 0 implica un nuevo cliente que adquirió un paquete, en este caso
la cantidad de puntos arrancará en 0, y el estado será "SALDO".
Si el nro_novedad = 999, entonces significa que el cliente desea cancelar (dar de baja)
su paquete turístico, y por ende se deberá actualizar además, el campo de fecha_baja (el
estado quedará con SALDO A FAVOR).
Los valores intermedios de 1...998 indican los pagos realizados por los clientes. Puede
haber más de una o ninguna novedad para cada cliente.

Además se cuenta con la información de los PAQUETES TURISTICOS en un archivo indexado.

**PAQUETES_TURISTICOS**, *indexado por id_paquete*
| id_paquete | nombre | costo | destino |
|------------|--------|-------|---------|

Desarrollar un algoritmo que permita actualizar el archivo de clientes, informando al
usuario por pantalla cualquier tipo de error, e informar al final.
1. La cantidad de clientes que se dieron de baja, y el monto total que debería
reintegrar la empresa.
2. El porcentaje de clientes de cada categoría.

## Ejercicio 2
Luego del proceso de actualización del archivo de CLIENTES, se requiere un informe
de totales. Es necesario conocer estadísticas de cantidad de paquetes adquiridos
por categoría de socio, teniendo en cuenta que la empresa ofrece 12 paquetes turísticos
distintos (id_paquete=1...12). Considerando además todo lo mencionado en el Ejercicio 1,
escribir un algoritmo que permita informar por pantalla:

1. Cantidad de paquetes adquiridos por cada categoría de cliente y nombre de paquete
(considerar sólo paquetes saldados, es decir cuyo saldo del cliente sea SALDADO O con
SALDO A FAVOR).
2. Cantidad total de paquetes saldados.
3. El paquete con más ventas.
