## Ejercicio 1
Con intención de analizar la predictibilidad de la Copa América 2024, se desea
analizar los Prode provistos por diferentes páginas web. Para esto se cuenta con
un archivo de Paises, con las estadísticas del mismo:

**PAÍSES** *ordenado por codigo_pais*
| **codigo_pais** | apuestas_a_favor | apuestas_en_contra | goles_esperados | tarjetas_rojas_esperadas |
|-----------------|------------------|--------------------|-----------------|--------------------------|

Se cuenta además con un archivo con las especulaciones de los fanáticos:

**PRODE** *ordenado por codigo_pais y fecha_apuesta*
| **Codigo_Pais** | **fecha_apuesta** | Apuesta_a_favor (S/N) | goles | tarjetas_rojas |
|-----------------|-------------------|-----------------------|-------|----------------|

Adicionalmente, se cuenta con un archivo con información de la cantidad de copas
que ganó cada país.

**TROFEOS** *Indexado por codigo_pais*
| **Codigo_Pais** | cantidad_de_copas |
|-----------------|-------------------|

Se solicita actualizar el archivo Países, teniendo en cuenta que puede haber más
de una apuesta para cada país en el archivo Prode.

1. Actualizar la cantidad de apuestas a favor, en contra, y un promedio de goles
y tarjetas rojas esperadas.
2. Si en el archivo PRODE se registra un país que no se encuentra en el archivo
PAISES, añadirlo al mismo.
3. Registrar en un nuevo archivo “POPULARES” los países cuya cantidad de apuestas
a favor superan, al menos, el triple de las apuesta en contra, y que además ganaron
más de dos veces la copa. En este caso no incluirlos en el archivo PAISES (si ya
existía, eliminarlos).

## Ejercicio 2
Además de la información previamente mencionada, se dispone de un archivo histórico,
que registra los resultados de cada jugador por Edición de Copa América, con el
siguiente formato:

| Año Copa América | Selección (1..10) | Jugador (1..23) | Tarjetas Amarillas | Tarjetas Rojas | Goles | Asistencias | Cantidad Partidos Jugados |
|------------------|-------------------|-----------------|--------------------|----------------|-------|-------------|---------------------------|

Los nombres de las selecciones están en un arreglo de alfanumérico, “selecciones”,
de 10 posiciones, donde el campo selección del archivo indica la ubicación del
nombre de la selección en el arreglo.

Se solicita: *(Mostrar siempre el nombre de la seleccion, no el código)*
1. Informar el jugador que más goles hizo y en qué selección está.
2. Informar el promedio de tarjetas rojas de cada selección.
3. Informar el total de goles que hizo cada jugador, en todas las selecciones.
4. Informar cuántos arqueros (número jugador 1) hicieron algún gol
