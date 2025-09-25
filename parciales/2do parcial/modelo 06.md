## Ejercicio 1
Previaje es un programa estatal de preventa turística que le reintegra el 50% del
valor de tu viaje en crédito con un tope de $100.000, este año se habilitó el programa
para realizar viajes durante todo el 2022. Se podrán ingresar facturas del 1 de agosto
al 15 de septiembre inclusive. Luego de esta fecha no se tomarán como válidos los
comprobantes subidos.

Para poder realizar el archivo tarjeta, que almacena el monto final a reintegrar por
usuario. Para eso se debe controlar que las facturas presentadas para el reintegro se
encuentren dentro de los plazos establecidos.

**TARJETA:** *Indexado por DNI*
| DNI N(8) | Num_cuenta N(8) | Crédito N(10) | Ult_Carga | Fecha |
|----------|-----------------|---------------|-----------|-------|

Un archivo tarjeta, donde se va actualizando el valor final que se reintegrará por usuario.

**TURISTA:** *Indexado por DNI*
| DNI N(8) | Nombre AN(100) | Fecha_nacimiento | Teléfono AN(100) |
|----------|----------------|------------------|------------------|

Un archivo turistas, donde se almacena la información de todos los usuarios que se
registraron para utilizar el beneficio del pre-viaje.

**FACTURAS** *Ordenado por nro_factura, DNI*
| Nro N(10) | DNI N(8) | id_servicio N(10) | monto N(2) | fecha_carga | fecha |
|-----------|----------|-------------------|------------|-------------|-------|

Un archivo facturas, donde se almacenan los comprobantes que suben a la página del pre-viaje.

Se pide:
1. Crear el monto correspondiente de crédito en archivo TARJETA, que corresponde al 50%
del monto facturado y un tope máximo de $100.000 de reintegro total. Solamente hacerlo
si la fecha_carga fue hasta del 15 de septiembre y el servicio esta habilitado para el
previaje (para esto se cuenta con un arreglo que contiene información de los id_servicio
inscriptos cuyo posición 1 contiene en el arreglo el id_servicio, y contiene un valor 1
si esta habilitado, y un cero si no lo esta).
2. Si el turista no existe en el archivo TURISTAS, debe darlo de alta y también en el
archivo TARJETA, puede generar el nro_cuenta llamando a la función obtener_nrocuenta()
(no se debe definir la función antes, se considera que ya existe).
3. Emitir total de facturas con fecha_carga fuera del plazo indicado

## Ejercicio 2
Posterior al proceso de actualización del punto anterior, se generó un archivo con todos
los viajes realizados donde se dio el beneficio de previaje. Destino se corresponde a cada
provincia, el nombre de las mismas está guardado en un arreglo de 23 posiciones.

**VIAJES**
| DNI N(8) | Fecha Fecha | Provincia_Destino N(2) | Monto_Crédito N(10) |
|----------|-------------|------------------------|---------------------|

Se pide realizar un algoritmo que permita determinar:
1. Por cada provincia y mes: cantidad de viajes y monto de crédito
2. Mayor monto de crédito otorgado discriminado por destino y mes
3. Destino con más turistas
4. promedio de crédito por provincia
