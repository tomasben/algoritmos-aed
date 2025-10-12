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

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    playlist, canciones, salida: secuencia de caracter
    play, can, gen, may_can_gen: caracter
    i, j, contador: entero
    cant_rock, cant_pop, cant_elec, cant_folk: entero
    cant_can, cant_play, total, may_can, longitud: entero

    FUNCION convertir(car: caracter): entero ES
      SEGUN car HACER
        '0': car_a_num := 0
        '1': car_a_num := 1
        '2': car_a_num := 2
        '3': car_a_num := 3
        '4': car_a_num := 4
        '5': car_a_num := 5
        '6': car_a_num := 6
        '7': car_a_num := 7
        '8': car_a_num := 8
        '9': car_a_num := 9
      FIN_SEGUN
    FIN_FUNCION
  PROCESO
    ARR(playlist); AVZ(playlist, play)
    AVZ(canciones); AVZ(canciones, can)
    CREAR(salida)

    cant_rock := 0; cant_pop := 0; cant_elec := 0; cant_folk := 0
    cant_play := 0; cant_can := 0

    MIENTRAS NO FDA(playlist) HACER
      cant_play := cant_play + 1

      gen := play
      SEGUN gen HACER
        'R': cant_rock := cant_rock + 1
        'P': cant_pop := cant_pop + 1
        'E': cant_elec := cant_elec + 1
        'F': cant_folk := cant_folk + 1
      FIN_SEGUN
      AVZ(playlist, play)
      AVZ(playlist, play)

      MIENTRAS play <> '+' HACER
        SI gen = 'R' ENTONCES
          ESCRIBIR(salida, play)
        FIN_SI
        AVZ(playlist, play)
      FIN_MIENTRAS
      ESCRIBIR(salida, play)
      AVZ(playist, play)

      contador := 0
      REPETIR
        contador := contador + 1

        MIENTRAS play <> '+' HACER
          AVZ(playlist, play)
        FIN_MIENTRAS
        AVZ(playlist, play)
      HASTA QUE contador = 3

      longitud := 0
      PARA i := 2 HASTA 0, -1 HACER
        longitud := longitud + convertir(play) * 10 ** i
        AVZ(playlist, play)
      FIN_PARA
      AVZ(playlist, play)

      cant_can := cant_can + longitud

      SI may_can < cant_can ENTONCES
        may_can := cant_can
        may_can_gen := gen
      FIN_SI

      PARA j := 1 HASTA longitud HACER
        MIENTRAS can <> '#' HACER
          SI gen = 'R' ENTONCES
            ESCRIBIR(salida, can)
          FIN_SI
          AVZ(canciones, can)
        FIN_MIENTRAS
        ESCRIBIR(salida, '+')
        AVZ(canciones, can)

        contador := 0
        REPETIR
          contador := contador + 1

          MIENTRAS can <> '#' HACER
            AVZ(canciones, can)
          FIN_MIENTRAS
          AVZ(canciones, can)
        HASTA QUE contador = 2

        MIENTARS can <> '/' HACER
          ESCRIBIR(salida, can)
          AVZ(canciones, can)
        FIN_MIENTRAS
        AVZ(canciones, can)
        ESCRIBIR(salida, '#')
      FIN_PARA
    FIN_MIENTRAS

    total := cant_rock + cant_pop + cant_elec + cant_folk

    ESC("Los porcentajes de los generos sobre el total son: ")
    ESC("Rock: ", cant_rock)
    ESC("Pop: ", cant_pop)
    ESC("Electrónica: ", cant_elec)
    ESC("Folklore: ", cant_folk)

    ESC("El promedio de canciones por playlist fue de: ", cant_can / cant_play, " canciones.")
    ESC("El genéro de la playlist con la mayor cantidad de canciones fue el ", may_can_gen,
    " con un total de ", may_can, " canciones.")

    CERRAR(playlist)
    CERRAR(canciones)
    CERRAR(salida)
FIN_ACCION
```

</details>

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

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Cancion = REGISTRO
      gen: AN(20)
      art: AN(70)
      alb: AN(70)
      nom: AN(12)
      cod: N(15)
      pub = REGISTRO
        año: N(4)
        mes: 1..12
        dia: 1..31
      FIN_REGISTRO
      repro: N(20)
    FIN_REGISTRO

    Informe = REGISTRO
      art: AN(70)
      can: N(3)
    FIN_REGISTRO

    entrada: archivo de Cancion ordenado por gen, art, alb, nom, cod
    can: Cancion
    salida: archivo de Informe ordenado por art
    inf: Informe

    cant_can, may_rep: entero
    cant_gral, cant_gen, cant_art: entero
    resg_art, may_rep_art: AN(70)
    resg_gen: AN(20)

    PROCEDIMIENTO corte_genero() ES
      corte_artista()
      ESCRIBIR("Para el genero ", resg_gen, " la cantidad de reproducciones
      fue de: ", cant_gen)
      cant_gral := cant_gral + cant_gen
      cant_gen := 0
      resg_gen := can.gen
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_artista() ES
      SI may_rep < cant_art ENTONES
        may_rep := cant_art
        may_rep_art := resg_art
      FIN_SI
      cant_can := 0

      inf.art := resg_art
      inf.can := cant_art
      ESCRIBIR(salida, inf)

      cant_gen := cant_gen + cant_art
      cant_art := 0
      resg_art := can.art
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (entrada); LEER(entrada, can)
    ABRIR /S (salida)

    resg_gen := can.gen; resg_art := can.art; may_rep_art := can.art
    cant_gral := 0; cant_gen := 0; cant_art := 0; cant_can := 0; may_rep := 0

    MIENTRAS NO FDA(entrada) HACER
      SI resg_gen <> can.gen ENTONCES
        corte_genero()
      CONTRARII
        SI resg_art <> can.art ENTONCES
          corte_artista()
        FIN_SI
      FIN_SI

      cant_can := cant_can + 1
      cant_art := cant_art + can.repro

      LEER(entrada, can)
    FIN_MIENTRAS
    corte_genero()

    ESCRIBIR("El total de reproducciones para todos los generos fue de: ", cant_gral, " reproducciones.")
    ESCRIBIR("E artista con la mayor cantidad de reproducciones fue: ", may_rep_art,
    " con un total de ", may_rep, " reproducciones.")

    CERRAR(entrada)
    CERRAR(salida)
FIN_ACCION
```

</details>
