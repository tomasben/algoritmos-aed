## Ejercicio 1
La empresa TICKET-TEC ha generado una secuencia de caracteres con información
de sus ventas para los eventos de los últimos 3 meses, cuya estructura se describe
a continuación. Inicialmente existe el nombre del local de los eventos, cuya longitud
se desconoce, termina con un #; a continuación se tiene la información de todos los
tickets vendidos para ese local, separado cada ticket del siguiente con el carácter |,
y al final de todas las ventas para ese local, el carácter &. Por último la marca de
fin de secuencia. También en el caso de butaca se desconoce la longitud del número,
termina con un guión.

*Ejemplo:*
Teatro Ópera#2030270520171A45-122J3027052017J3D120-120J3028052017Z C233-1&Galpon de las Luces#2030070720171C5-12230301020172A233-1&(fin)

local de eventos#horario evento [hhmm] Fecha del evento [ddmmaaaa] código del evento [1..3] butaca [sector [A,C o D], número]|—!
Solo hay dos horarios 20:30 y 22:30.

La empresa solicita un algoritmo que cumpla con las siguientes consignas:
1. Generar una nueva secuencia que contenga los tickets correspondientes a un horario ingresado por el usuario.
2. Informar total general de tickets vendidos, total de tickets por sector y porcentaje de cada uno sobre el total general.

## Ejercicio 2

Dado el siguiente Enunciado, contestar los puntos que se enumeran en la Consigna. NO HACER EL ALGORITMO.

Enunciado:
La empresa de Servicios Energéticos de una Ciudad posee un archivo histórico desde el año 2000 hasta la actualidad con todos los consumos de los usuarios ordenados por Barrio, Usuario y fecha de medición de la siguiente manera:

| Barrio | Usuario | fecha de medición | consumo |
|--------|---------|-------------------|---------|

Se pide:
a) Generar un archivo de salida con todos los consumos de los usuarios, cuyo registro tenga el siguiente formato:

| Barrio | Usuario | Consumo |
|--------|---------|---------|

b) Muestre por pantalla el total de consumo solo del año 2015, por cada barrio y el total general para toda la ciudad

Consigna:
1. Responda: cuantos niveles de corte hay? Enumere cuales son. Escriba el trozo de algoritmo donde se verifica si hay corte.
2. ¿Cuantos totalizadores se necesitan? Indicar cuales son (utilizar nombres descriptivos del valor que representan)
3. Escriba la subacción que permite cumplir con el punto a) del enunciado.
