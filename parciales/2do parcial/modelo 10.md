## Ejercicio 1
Una empresa dedicada a la venta de combustibles para automotores anunció una promoción
mediante la cual los clientes pueden acceder a beneficios importantes. En cada carga
los clientes suman 10 puntos por cada $100 de combustible y una vez que el cliente llega
a los 100 puntos este los puede canjear por un descuento de $100 en el importe total.

La cantidad de puntos que tiene cada cliente están almacenados en el archivo indexado
PUNTOS el cual tiene el siguiente formato:

**PUNTOS** *Indexado por DNI*
| DNI N(8) | Cant_Puntos N(5) | Ult_Carga (Fecha AAMMDDHHMM) |
|----------|------------------|------------------------------|

**CLIENTE** *Indexado por DNI*
| DNI N(8) | Ape_Nom AN(30) | Edad N(2) | Ciudad AN(30) |
|----------|----------------|-----------|---------------|

Se pide realizar el algoritmo que permita:
1. Realizar la carga interactiva de las cargas de combustible (ingresando monto),
actualizando la cantidad de puntos y la fecha de ultima carga del archivo PUNTOS.
2. Si no existe el Cliente, se lo debe dar de alta en ambos archivos completando
los datos correspondientes
3. Permitir al cliente aplicar descuentos a las cargas realizadas siempre y cuando
tenga puntos suficientes (solo se puede canjear 100 puntos por carga)
4. Determinar la cantidad de cargas realizadas de usuarios no existentes

## Ejercicio 2
Además la empresa cuenta con un archivo secuencial CARGAS con las cargas del primer
trimestre de 2018 con el siguiente formato

**CARGAS** *(no ordenado)*
| Fecha | DNI_Cliente N(8) | Sucursal N(2) | Importe N(5) |
|-------|------------------|---------------|--------------|

Se pide realizar un algoritmo que permite determinar:
1. Mes con mayor importe generado
2. Sucursal con mayor cantidad de cargas (existen 10 sucursales)
3. En que mes y en que sucursal se genero el mayor importe acumulado
