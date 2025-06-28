## Ejercicio N° 1
Un supermercado mayorista necesita un informe de ventas, para lo cual cuenta con una secuencia
de caracteres y una secuencia de enteros, ambas contienen información del mes de JUNIO, para
las distintas sucursales. La estructura de dichas secuencias es la siguiente:

**Secuencia de caracteres:**
Sucursal (cantidad indeterminada de caracteres) & cantidad de tickets (3 caracteres), sucursal &
cantidad de tickets....FDS

*Ejemplo:*
| R | e | s | i | s | t | e | n | c | i | a | & | 0 | 2 | 5 | B | a | r | r | a | n | q | u | e | r | a | s | & | 1 | 2 | 3 | …FDS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|------|

**Secuencia de enteros:**
Para cada ticket: Forma de pago (1: efectivo, 2: tarjeta débito y 3: tarjeta crédito) | Nro ticket |
cantidad de artículos | importe

*Ejemplo:*
| 1 | 2345 | 9 | 12500 | 3 | 2950 | 4 | 9864 |...FDS |
|---|------|---|-------|---|------|---|------|-------|

Si considera necesario, puede utilizar una función ConvertiraNumero(caracter), que recibe como
parámetro un carácter y devuelve un dato entero. No es necesario desarrollar la función.

Se solicita diseñar un algoritmo que:
1) Genere una secuencia de salida de caracteres que contenga el nombre de la sucursal y la
cantidad de ventas en efectivo.
2) Informe el porcentaje de ventas en efectivo sobre el total de tickets.

## Ejercicio N° 2
Un supermercado mayorista que cuenta con un sistema de atención en cajas necesita un informe de ventas,
para lo cual cuenta con el archivo secuencial VENTAS que contiene información de todos los tickets
emitidos durante el mes de JUNIO. Para cada venta se registra:
VENTAS, Ordenado por Nro de Caja, Forma de pago, Nro de ticket

| Nro de Caja | Forma de pago (EF, TD y TC) | Nro de ticket | Fecha de venta | Cantidad de artículos | Importe de la venta |
|-------------|-----------------------------|---------------|----------------|-----------------------|---------------------|

Nota: EF: efectivo, TD: tarjeta débito y TC: tarjeta crédito.

Se pide escribir un algoritmo que permita:
1) Imprimir un informe que muestre por pantalla el total de dinero recaudado por caja y por forma
de pago.
2) Crear un fichero de salida que contenga Nro de caja, total pago (importes) en efectivo y total
pago (importes) con tarjetas (TD o TC). (1 registro por caja)

| Nro de Caja | Total Efectivo | Total Tarjetas |
|-------------|----------------|----------------|

3) Informar cuáles son las cajas que tuvieron mayor recaudación (importes) en efectivo que con
tarjetas.
