## Ejercicio 1
La FIFA desea analizar la participación de los jugadores por equipo en el Mundial
de Clubes. Para ello cuenta con dos secuencias de caracteres:

**SECUENCIA JUGADORES:**

Confederación-NombreEquipo-NombreJugadorEdad(2)NroJugador(2)#NombreJugadorEd ad(2)NroJugador(2)#...%NombreEquipo-NombreJugador*...-$Confederación-...

El guión - separa Confederaciones y nombre del equipo. El nombre del jugador termina
con *. Confederación finaliza con $. Equipo finaliza con %. Jugador termina con #.
Por cada confederación existen varios equipo y por cada equipo existen varios jugadores.

*Ejemplo:* UEFA-Real Madrid-Luka Modric3801#Vinicius Jr2402#Jude Bellingham2103#%Manchester City-Kevin De Bruyne3304#Erling Haaland2405#Phil Foden2308#-$CONMEBOL-Flamengo-Germán Cano*3407#André Trinidad*2208#%Boca Juniors-Edinson Cavani*3709#Luis Advíncula*3410#%$*

**SECUENCIA ESTADÍSTICAS:** Correspondencia 1 a 1 con cada jugador.

Goles(2caracteres)Asistencias(2caracteres)MinutosJugados(4caracteres)TarjetasAma rillas(1caracter)TarjetasRojas(1caracter)#...

*Ejemplo:* 0101027000#0403031210#0201024500#0501030010#0600028001#*

Se pide:
1. Generar una secuencia de salida con los Equipos (al final del nombre poner un "7")
y sus jugadores que hayan tenido al triple de goles que de la suma entre asistencias y
tarjetas rojas, separando los jugadores con "" y los equipos con "(". (Suponer que si un
solo de estos tienen al menos un jugador que cumple la condición)

NombreEquipo "NombreJugador... NombreJugador..."%NombreEquipo"NombreJugador_..._..."("

2. Informar por pantalla cantidad de jugadores de cada equipo. (Ej Real Madrid 22.)
3. Informar por confederación cuántos jugadores jugaron mas de 1000 minutos.

## Ejercicio 2
La FIFA desea complementar el análisis del Mundial de Clubes con un reporte de participación
y rendimiento. Se dispone del archivo secuencial PARTICIPACIONES, ordenado por Confederación,
Equipo y Posición con la siguiente estructura:

| Confederación | Equipo | Posición | NombreJugador | Asistencias | Goles | Edad |
|---------------|--------|----------|---------------|-------------|-------|------|

1. Informar el total de goles por confederación, equipo...
2. Informar por confederación el total de equipos con más de 20 goles
3. Emitir un archivo de salida llamado Equipazos que contenga el equipo, posición,
el promedio de goles de la misma (por posición).
