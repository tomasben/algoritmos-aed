## Ejercicio 1
La provincia del chaco atendió la problemática de animales abandonados en las calles con la campaña
“Adopta un compañero”. Como parte de esta gestión, solicitó a la UTN, FRRe una solución tecnológica
para llevar registro de cuáles animales han sido adoptados.

Se cuenta con dos secuencias de caracteres. Una secuencia con todos los animales que la provincia ha
rescatado y otra con los datos de las adopciones. Con las siguientes estructuras:

**Rescatados:** id_mascTipo_animalSexoEdadNombre#id_albergue_asignado

*Ejemplo:* 01CM010Huesos#25603FM030Michi#230516345…*

Descripción de los datos: id_masc: 2 caracteres. Tipo animal: 1 caracter C(caninos), F (felinos). Sexo: 1
caracter H, M. Edad: 3 caracteres (en meses). Nombre: cantidad indefinida de caracteres, finaliza con #.
id_albergue: 3 caracteres. La secuencia finaliza con *

**Adopciones:** id_mascFecha_adopcionDirección%Nro_telefono

*Ejemplo:* 01240307EvergreenTerrace742%3624112233…*

Descripción de los datos: id_masc: 2 caracteres; fecha adopción: 6 caracteres (aammdd), dirección
cantidad indefinida de caracteres, finaliza con %, nro teléfono: 10 caracteres. La secuencia finaliza con *.
Pueden existir mascotas rescatadas que no fueron adoptadas, con lo cual no aparecerán en la
secuencia de adopciones.

Se pide :
1. Generar una salida que contenga únicamente los perros (caninos) que han sido adoptados se
desea saber: sexo, edad, nombre, telefono del adoptante. separar las adopciones en la salida
con el signo \$.
*Ejemplo Salida:* M01Huesos#3624112233$
2. Generar una secuencia de enteros, con todos los id_masc de las mascotas no adoptados, cada
ventana es un id (entero de dos dígitos)
3. Informar porcentaje de gatos y perros no adoptados sobre el total de no adoptados.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    rescates, adopciones, perr_adop: secuencia de caracter
    anim_nadop: secuencia de entero
    res, adop: caracter
    i, j, k: entero
    gat_na, per_na, no_adoptados, id_adop, id_anim: entero
    fue_adoptado: logico
  PROCESO
    ARR(rescates); AVZ(rescates, res)
    ARR(adopciones); AVZ(adopciones, adop)
    CREAR(perr_adop); CREAR(anim_nadop)

    gat_na := 0; per_na := 0; no_adoptados := 0;

    MIENTRAS adop <> '*' HACER
      id_adop := 0
      PARA i := 1 HASTA 0, -1 HACER
        id_adop := id_adop + convertir(adop) * 10 ** i
        AVZ(adopciones, adop)
      FIN_PARA

      REPETIR
        id_anim := 0
        PARA j := 1 HASTA 0, -1 HACER
          id_anim := id_anim + convertir(res) * 10 ** j
          AVZ(rescates, res)
        FIN_PARA

        SI id_adop = id_anim ENTONCES
          fue_adoptado := verdadero
        CONTRARIO
          fue_adoptado := falso
        FIN_SI

        SI fue_adoptado ENTONCES
          // Solo escribimos a la secuencia de salida los perros adoptados
          SI res = 'C' ENTONCES
            AVZ(rescates, res)

            MIENTRAS res <> '#' HACER
              ESCRIBIR(perr_adop, res)
              AVZ(rescates, res)
            FIN_MIENTRAS

            //Avanzo el '#' y 3 digitos del albergue
            AVZ(rescates, res); AVZ(rescates, res)
            AVZ(rescates, res); AVZ(rescates, res)

            MIENTRAS adop <> '%' HACER
              AVZ(adopciones, adop)
            FIN_MIENTRAS
            AVZ(adopciones, adop) <- Avanzo el '%'

            // Escribo el número de teléfono del dueño
            PARA k := 1 HASTA 10 HACER
              ESCRIBIR(perr_adop, adop)
              AVZ(adopciones, adop)
            FIN_PARA
            ESCRIBIR(perr_adop, '$')
          CONTRARIO
            // En caso de ser un gato simplemente avanzamos hasta el siguiente animal
            ambas secuencias hasta el final

            MIENTRAS res <> '#' HACER
              AVZ(rescates, res)
            FIN_MIENTRAS
            AVZ(rescates, res); AVZ(rescates, res)
            AVZ(rescates, res); AVZ(rescates, res)

            MIENTRAS adop <> '%' HACER
              AVZ(adopciones, adop)
            FIN_MIENTRAS
            AVZ(adopciones, adop)

            PARA k := 1 HASTA 10 HACER
              AVZ(adopciones, adop)
            FIN_PARA
          FIN_SI
        CONTRARIO
          no_adoptados := no_adoptados + 1

          SI res = 'C' ENTONCES
            per_na := per_na + 1
          CONTRARIO
            gat_na := gat_na + 1
          FIN_SI
          AVZ(rescates, res)

          // Escribimos el ID del animal no adoptado
          ESCRIBIR(anim_nadop, id_anim)

          MIENTRAS res <> '#' HACER
            AVZ(rescates, res)
          FIN_MIENTRAS
          AVZ(rescates, res); AVZ(rescates, res)
          AVZ(rescates, res); AVZ(rescates, res)
        FIN_SI
      HASTA QUE fue_adoptado = verdadero
    FIN_MIENTRAS

    // Avanzo el caracter final de la secuencia '*'
    AVZ(adopciones, adop)

    ESCRIBIR("De un total de ", no_adoptados, " animales no adoptados: ")
    ESCRIBIR("Gatos (felinos): ", gat_na * 100 / no_adoptados, "%.")
    ESCRIBIR("Perros (caninos): ", per_na * 100 / no_adoptados, "%.")

    CERRAR(resctates); CERRAR(adopciones)
    CERRAR(perr_adop); CERRAR(anim_nadop)
FIN_ACCION
```

</details>

## Ejercicio 2
Además de la información previamente mencionada, se dispone de un archivo que registra las
adopciones organizadas por departamento, localidad, barrio y adoptante. Este archivo también
proporciona datos adicionales como el tipo de animal (canino o felino), y la cantidad de
mascotas que ya tiene el adoptante.

| Departamento | localidad | barrio | dni | adoptante | id_mascota | Tipo (C,F) | cant | anteriores |
|--------------|-----------|--------|-----|-----------|------------|------------|------|------------|

Se solicita:
1. Informar la cantidad de adopciones por localidad y barrio ; discriminando por perros y
gatos.
2. Informar el porcentaje de gatos adoptados en la provincia.
3. Generar un nuevo archivo con el siguiente formato, considerando solo las adopciones
por familias que ya tenían más de 3 mascotas.

| Departamento | Localidad | Cantidad de adopciones |
|--------------|-----------|------------------------|

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Adopcion = REGISTRO
      depto: AN(30)
      local: AN(30)
      barrio: AN(30)
      dni: N(8)
      adop: AN(30)
      id_masc N(8)
      tipo: caracter
      cant: N(2)
      anteriores: N(2)
    FIN_REGISTRO

    Informe = REGISTRO
      depto: AN(30)
      local: AN(30)
      cant: N(2)
    FIN_REGISTRO

    adopciones: archivo de Adopcion ordenado por depto, local, barrio, adop
    reg: Adopcion
    salida: archivo de Informe
    inf: Informe

    bar_per, bar_gat, loc_per, loc_gat, prov_per, prov_gat, total: entero
    resg_loc, resg_bar: AN(30)

    PROCEDIMIENTO corte_localidad() ES
      corte_barrio()
      ESCRIBIR("Para la localidad de ", resg_loc, " se registraron adopciones de ",
      loc_per, " perros y ", loc_gat, " gatos.")
      prov_per := prov_per + loc_per
      prov_gat := prov_gat + loc_gat
      loc_per := 0
      loc_gat := 0
      resg_loc := reg.local
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_barrio() ES
      ESCRIBIR("En el barrio ", resg_bar, " se registraron adopciones de ",
      bar_per, " perros y ", bar_gat, " gatos.")
      loc_per := loc_per + bar_per
      loc_gat := loc_gat + bar_gat
      bar_per := 0
      bar_gat := 0
      resg_bar := reg.barrio
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (adopciones); LEER(adopciones, reg)
    ABRIR /S (salida)

    resg_loc := reg.local; resg_bar := reg.barrio
    prov_per := 0; prov_gat := 0; loc_per := 0
    loc_gat := 0; bar_per := 0; bar_gat := 0

    MIENTRAS NO FDA(adopciones) HACER
      SI resg_loc <> reg.local ENTONCES
        corte_localidad()
      CONTRARIO
        SI resg_bar <> reg.barrio ENTONCES
          corte_barrio()
        FIN_SI
      FIN_SI

      SI reg.tipo = 'C' ENTONCES
        bar_per := bar_per + 1
      CONTRARIO
        bar_gat := bar_gat + 1
      FIN_SI

      SI reg.anteriores > 3 ENTONCES
        inf.depto := reg.depto
        inf.local := reg.local
        inf.cant := reg.cant

        ESCRIBIR(salida, inf)
      FIN_SI

      LEER(adopciones, reg)
    FIN_MIENTRAS
    total := prov_per + prov_gat

    ESCRIBIR("De un total de ", total, " adopciones en la provincia, un "
    prov_gat * 100 / total, "% pertenecieron a adopciones de gatos.")

    CERRAR(adopciones)
    CERRAR(salida)
FIN_ACCION
```

</details>
