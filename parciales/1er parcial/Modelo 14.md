## Ejercicio 1
La empresa "Caminos del Litoral" quiere conocer las estadísticas del tráfico existente
en el puente General Belgrano (popularmente conocido como Puente Chaco Corrientes).
Para esto cuenta con los datos del movimiento ocurrido en el mes de junio de 2024 en un
día (desde el día 1 del mes, hasta 30), sabiendo que todos los días hubieron movimientos,
se dispone de una secuencia de caracteres con el siguiente formato:

día(2 caracter)ESferiado(S o N)InformacionDeVehiculos! [...]día(2 caracter)ESferiado(S o N)InformacionDeVehiculos!

Donde InformacionDeVehiculos se corresponde con:
Categoria (1 caracter: 1..5) HHMM(horaminuto) Patente (7 caracteres)$

*Ejemplo:*
12S22230AC13FE32231AB45HI42231AB21HU13N58615AD23HF_!

El monto a pagar del peaje depende de la categoría. Se puede obtener a partir de una
función ya implementada, monto_peaje(), que recibe como parámetro el carácter de la
categoría.

Se le solicita:
1. Generar una secuencia de salida con la información de todos los vehículos de una determinada
categoría (que ingrese el usuario) y que han circulado los días feriados. Interesará conocer:
HHMMPatente (separar la información de cada vehículo por el carácter '#'.
2. Por cada día, indicar la cantidad recaudada.
3. Porcentaje de vehículos de cada categoría sobre el total.

## Ejercicio 2
Los datos históricos de los vehículos que pasaron por el peaje se encuentra en un archivo
con el siguiente formato:

PEAJE (Ordenado por año, mes, día, categoría y patente)

| Año | Mes | Día | Categoría | Patente | Cantidad de pases |
|-----|-----|-----|-----------|---------|-------------------|

Se le solicita:
1. Informar la cantidad total de vehículos que pasaron por año y mes, y total general.
2. Informar el año en el que hubo la mayor cantidad de pases.
3. Generar un archivo de salida con la siguiente información:

| Año | Mes | Día | Cantidad de pases |
|-----|-----|-----|-------------------|
