## Ejercicio N° 1
Una cadena de hoteles necesita un informe de ocupación y pagos para el mes de JUNIO. Para
esto, se cuenta con dos secuencias de datos:

**Secuencia de caracteres:**
Estructura: Hotel (cantidad indeterminada de caracteres) &a cantidad de reservas (3 caracteres)
hotel & cantidad de reservas....FDS

*Ejemplo:*
| H | o | t | e | l | A | l | a | s | & | 3 | 4 | 0 | H | o | t | e | l | B | a | h | i | a | & | 9 | 9 | 9 | …FDS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|------|

**Secuencia de enteros:**
Estructura: Para cada reserva: Nro de reserva, tipo de habitación (1: single, 2: doble, 3: suite),
cantidad de noches, importe.

*Ejemplo:*
| 1234 | 1 | 3 | 120.000 | 2345 | 3 | 2 | 65.000 |...FDS |
|------|---|---|---------|------|---|---|--------|-------|

Nota: La función ConvertiraNumero(caracter) puede ser utilizada si se considera necesario para
convertir un carácter a un dato entero.

Se pide escribir un algoritmo que permita:
1) Generar una secuencia de salida de enteros que contenga el número de reserva y el importe,
cuando el importe sea menor a 90.000.
2) Informe, para cada hotel, cuál fue la reserva (NroReserva) con mayor cantidad de noches (y la
cantidad de noches).

## Ejercicio N° 2
La cadena de hoteles del ejercicio anterior cuenta con un sistema de gestión de reservas y ahora
le solicita a Ud. un informe de ocupación y facturación para el mes de JUNIO. Para cada reserva
se registra:

RESERVAS, Ordenado por Número de Hotel, Tipo de Habitación, Número de Reserva

| Nro. de Hotel | Tipo de Habitación (IND, DOB, SUITE) | Nro de Reserva | Fecha de ingreso | Cantidad de noches | Importe de la reserva |
|---------------|--------------------------------------|----------------|------------------|--------------------|-----------------------|

Tipo de Habitación: (IND: Individual, DOB: Doble, SUITE: Suite)

Se pide escribir un algoritmo que permita:
1) Imprimir un informe que muestre el total de noches reservadas por hotel y por tipo de
habitación.
2) Crear un fichero de salida que contenga Número de Hotel, total de noches reservadas en
habitaciones dobles y suites.

| Nro de Hotel | Total hab. dobles | Total hab. suites |
|--------------|-------------------|-------------------|

3) Informar cuáles son los hoteles que tuvieron mayor cantidad de noches reservadas en
habitaciones dobles (DOB) que en suites (SUITE).
