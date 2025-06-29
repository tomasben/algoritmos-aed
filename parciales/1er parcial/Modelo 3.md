## Ejercicio 1
La plataforma de música digital Spotify almacena información sobre las playlists y
sus canciones en secuencias de caracteres. Durante todo el año, las canciones son
reproducidas por los usuarios y también se generan nuevas playlists. Al final de
cada año suelen emitir un resumen para sus usuarios (Spotify wrapped) por lo que
necesitan ayuda con un algoritmo que les brinde la información necesaria.

En la secuencia PLAYLISTS se almacena en el siguiente orden:
- Género de música ('R' – Rock, 'P' – Pop, 'E' – Electrónica, 'F' – Folklore).
- Nombre de la playlist.
- Usuario que la creó.
- Fecha de creación.
- Duración (4 dígitos).
- Cantidad de canciones (3 dígitos).

Los datos de cada playlist están separados entre sí por el símbolo '+' y
finalizan con el símbolo '?'.

**Formato de la secuencia PLAYLISTS:**
Genero(1AN)+Nombre+usuario+aammdd+duracion(hhmm)+cantidad(3AN)?

*Ejemplo de la secuencia PLAYLISTS:*
R+Una Playlist Linda+Valentina1+001203+1352+012?P+Hits Taylor Swift+Majo00+231013+0922+015?

En la secuencia CANCIONES se almacena en el siguiente orden:
- Nombre de la canción.
- Duración en minutos.
- Año en que fue publicada.
- Nombre artista.

Todos los datos de las canciones están separados por el símbolo '#' y
finalizan con el símbolo '/'.

**Formato de la secuencia CANCIONES:**
Nombre#duracion(mmss)#aaaa#nombreArtista/

*Ejemplo de la secuencia PLAYLISTS:*
One#0744#1989#Metallica/Dress#0350#2017#Taylor Swift/

La playlist de cada canción se determina de acuerdo al dato
'cantidad de canciones' de la secuencia PLAYLISTS, por ej.: la playlist
de ROCK ARGENTINO tiene 2 canciones, por lo cual las primeras 2 canciones
de la secuencia CANCIONES le pertenecen, las siguientes 6 pertenecen a LA
CUMBIA DEL MOMENTO, etc.

Se pide:
1. Informar el porcentaje de playlists de cada género sobre el total.
2. Cantidad promedio de canciones de las playlists.
3. Identificar e informar el género de la playlist con la mayor cantidad de canciones.
4. Generar una secuencia de salida con información de las playlists de rock. La secuencia
debe contener el nombre de la playlist seguido de sus canciones (nombre y artista). Los
datos correspondientes a la misma playlist deben separarse entre sí con el signo '+' y
finalizar con el signo '#'.

## Ejercicio 2
Para continuar con su análisis de fin de año, Spotify cuenta con un archivo con todas sus
canciones según el siguiente formato:

CANCIONES: ordenado por Genero, Artista, Album, Nombre y Codigo.

| Genero AN(20) | Artista AN(70) | Album AN(70) | Nombre AN(12) | Codigo N(15) | Fecha_publicacion | Cantidad_Reproducciones N(20) |
|---------------|----------------|--------------|---------------|--------------|-------------------|-------------------------------|

Se pide:
1. Emitir un archivo que contenga la cantidad de canciones publicadas por cada artista:

CANCIONES_SALIDA: ordenado por ARTISTA

| Artista AN(70) | Cant_canciones N(3) |
|----------------|---------------------|

2. Emitir la cantidad total de reproducciones por cada género y el total
general de cantidad de reproducciones.
3. Identificar el artista con la mayor cantidad de reproducciones.
