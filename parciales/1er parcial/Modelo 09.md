## Ejercicio 1
En Julio próximo se realizará la Bienal de Esculturas en Resistencia.
Como aporte tecnológico, la Fundación Urunday ha solicitado una aplicación
que permita la decodificación de información almacenada en códigos QR. Cada
código decodificado se guarda en una secuencia de caracteres con el siguiente formato:

Continente (A-América, E-Europa, F-África), Nombre del Escultor (alfanumérico de 30 caracteres),
Año de Inicio en la disciplina (4 dígitos). Cada escultor se separa del otro con el símbolo "|".

Sin embargo en el proceso de decodificación se registraron errores en la información
correspondiente a algunos de los escultores de Europa, pues en el año de inicio se almacenó
en el último dígito una vocal (a= 1, e = 2, i=3).

Por ello le solicitan a Ud que diseñe un algoritmo en pseudocódigo que permita:
1. Generar tres secuencias de salida, separando escultores por continente. Tener en cuenta que para
la secuencia de Europa hay que verificar y corregir el error del último dígito del año de inicio.
2. Informar cantidad de escultores por continente que hayan comenzado en la disciplina después del año 2000.
3. Informar porcentaje de escultores con información errónea sobre el total de escultores.

## Ejercicio 2
La Fundación Urunday cuenta con un archivo con información de emplazamiento de esculturas en la ciudad.

ECL, ordenado por AÑO, MES, MATERIAL, CODIGO

| AÑO N(4) | MES N(2) | MATERIAL (M: Mármol - D: Madera) | CODIGO AN(12) | NOMBRE AN(20|) |
|----------|----------|----------------------------------|---------------|----------------|

Realizar un algoritmo en pseudocódigo que permita:
1. Obtener un informe con el total de esculturas emplazadas por Año, Mes y Material. Y un total general.
Dar al informe el formato que considere adecuado.
2. Generar un archivo de salida con la cantidad de esculturas emplazadas por mes durante el año 2015.

EMPL, ordenado por MES, MATERIAL

| MES N(2) | MATERIAL (M:Mármol - D:Madera) | CANT N(3) |
|----------|--------------------------------|-----------|
