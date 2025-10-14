## Ejercicio 1
Santa Claus y su equipo de duendes registran toda la información de los niños que
esperan regalos durante la Navidad.

Cada niño está registrado en un archivo secuencial llamado NIÑOS, donde se guarda
información sobre su comportamiento y su deseo principal.

Al final de la temporada previa a Navidad, los duendes recopilan los eventos ocurridos
durante el mes en un archivo secuencial llamado EVENTOS, que detalla las novedades,
incluyendo cambios de comportamiento, solicitudes de regalos, y demás actualizaciones.

**NIÑOS** *ordenado por id_pais, id_niño*
| **id_pais** | **id_niño** | nombre y apellido | puntaje_buen_comportamiento | id_regalo | nombre_regalo | fecha_registro | fecha_retiro |
|-------------|-------------|-------------------|-----------------------------|-----------|---------------|----------------|--------------|

- id_pais: Identificador del País del niño.
- id_niño: Identificador único del niño.
- puntaje_buen_comportamiento: Puntaje que indica el comportamiento del niño (puede ser positivo o negativo).
- regalo_deseado: Nombre del regalo que desea recibir.
- fecha_registro: Fecha en la que se registró al niño.
- fecha_retiro: Fecha en la que fue retirado de la lista de navidad (si corresponde).

**EVENTOS** *ordenado por id_pais, id_niño, cod_evento*
| **id_pais** | **id_niño** | **cod_evento** (0..99) | fecha_evento | detalle | puntaje_cambio | tipo | id_regalo_deseado | regalo_deseado |
|-------------|-------------|------------------------|--------------|---------|----------------|------|-------------------|----------------|

- cod_evento: 0: Alta de un nuevo niño; 99: Retiro de un niño de la lista; 1-98:
Actualización de puntaje de comportamiento o cambio de regalo deseado.
- detalle: Descripción del evento (por ejemplo, "Ayudó a su hermano", "Se peleó
en la escuela", etc.).
- puntaje_cambio: Valor que se sumará o restará al puntaje de comportamiento del niño.
- tipo: "A" si el evento mejora el puntaje (positivo), "R" si lo reduce (negativo),
vacío si es un cambio de regalo.
- regalo_deseado: Nuevo regalo deseado (si corresponde a un cambio).

Se pide:
- Desarrollar un algoritmo que permita mantener actualizado el archivo NIÑOS con
los eventos registrados en el archivo EVENTOS.
- El algoritmo debe ajustar los puntajes de comportamiento y actualizar los regalos deseados si corresponde.
- Informar por pantalla cualquier tipo de error que considere pertinente durante el proceso.

Además indicar:
1. La cantidad total de niños nuevos que se registraron durante el proceso.
2. El nombre del niño con mejor puntaje de buen comportamiento.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Fecha = REGISTRO
      año: N(4)
      mes: 1..12
      dia: 1..31
    FIN_REGISTRO

    Niño = REGISTRO
      clave = REGISTRO
        id_pais: N(5)
        id_niño: N(5)
      FIN_REGISTRO
      nom: AN(30)
      pun: entero
      id_reg: N(5)
      nom_reg: AN(20)
      registro: Fecha
      retiro: Fecha
    FIN_REGISTRO

    Evento = REGISTRO
      clave = REGISTRO
        id_pais: N(5)
        id_niño: N(5)
      FIN_REGISTRO
      cod_eve: 0..99
      fecha: Fecha
      detalle: AN(50)
      pun: entero
      tipo: ('A', 'R')
      id_reg: N(5)
      nom_reg: N(5)
    FIN_REGISTRO

    niños: archivo de Niño ordenado por id_pais y id_niño
    nin: Niño
    eventos: archivo de Evento ordenado por id_pais, id_niño y cod_eve
    eve: Evento
    salida: archivo de Niño
    aux, regsal: Niño

    nuevos, may: entero
    may_nom: AN(30)

    PROCEDIMIENTO leer_niño() ES
      LEER(niños, nin)
      SI FDA(niños) ENTONCES
        nin.clave := HV
      FIN_SI
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO leer_evento() ES
      LEER(eventos, eve)
      SI FDA(eventos) ENTONCES
        eve.clave := HV
      FIN_SI
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (niños)
    ABRIR E/ (eventos)
    ABRIR /S (salida)

    leer_niño()
    leer_evento()

    may := 0; nuevos := 0

    MIENTRAS (nin.clave <> HV) O (eve.clave <> HV) HACER
      SI (nin.clave > eve.clave) ENTONCES
        SEGUN eve.cod_eve HACER
          0:
            regsal.clave := eve.clave
            regsal.registro := eve.fecha

            SI (eve.tipo = ' ') ENTONCES
              regsal.id_reg := eve.id_reg
              regsal.nom_reg := eve.nom_reg
            CONTRARIO
              SI (eve.tipo = 'A') ENTONCES
                regsal.pun := eve.pun
              CONTRARIO
                regsal.pun := 0 - eve.pun
              FIN_SI
            FIN_SI

            SI (may < regsal.pun) ENTONCES
              may := regsal.pun
              may_nom := regsal.nom
            FIN_SI

            ESCRIBIR(salida, regsal)
            nuevos := nuevos + 1
          1..98:
            ESCRIBIR("ERROR: no se puede actualizar niño inexistente: ", eve.clave.id_niño)
          99:
            ESCRIBIR("ERROR: no se puede dar de baja niño inexistente: ", even.clave.id_niño)
        FIN_SEGUN
        leer_evento()
      CONTRARIO
        SI (nin.clave < eve.clave) ENTONCES
          SI (may < nin) ENTONCES
            may := nin
            may_nom := nin.nom
          FIN_SI

          regsal := nin
          ESCRIBIR(salida, regsal)
          leer_niño()
        CONTRARIO
          SEGUN eve.cod_eve HACER
            0:
              ESCRIBIR("ERROR: no se puede dar de alta niño existente: ", eve.clave.id_niño)
              leer_evento()
            1..98:
              regsal := nin

              MIENTRAS (regsal.clave = eve.clave) HACER
                SI (eve.tipo = ' ') ENTONCES
                  regsal.id_reg := eve.id_reg
                  regsal.nom_reg := eve.nom_reg
                CONTRARIO
                  SI (eve.tipo = 'A') ENTONCES
                    regsal.pun := regsal.pun + eve.pun
                  CONTRARIO
                    regsal.pun := regsal.pun - eve.pun
                  FIN_SI
                FIN_SI
                leer_evento()
              FIN_MIENTRAS

              SI (may < regsal.pun) ENTONCES
                may := regsal.pun
                may_nom := regsal.nom
              FIN_SI
              ESCRIBIR(salida, regsal)
            99:
              regsal := nin
              regsal.retiro := eve.fecha
              ESCRIBIR(salida, regsal)
              leer_evento()
          FIN_SEGUN
          leer_niño()
        FIN_SI
      FIN_SI
    FIN_MIENTRAS

    ESCRIBIR("Se añadieron un total de ", nuevos, " nuevos niños a la lista.")
    ESCRIBIR("El niño con el mejor puntaje fue: ", may_nom, " con un total de ", may, " puntos.")

    CERRAR(niños)
    CERRAR(eventos)
    CERRAR(salida)
FIN_ACCION
```

</details>

##  Ejercicio 2
Santa Claus y su equipo desean conocer cómo se distribuyen los regalos entregados
por región y categoría de niños según su nivel de comportamiento (registrado en el
archivo NIÑOS del Ejercicio 1).

Para ello, cuentan con un archivo indexado que contiene la información de las regiones
donde Santa Claus realiza sus entregas de regalos (importante: las regiones abarcan
varios países).

**REGIONES** *indexado por id_pais*
| **id_pais** | nombre_pais | id_region | nombre_region |
|-------------|-------------|-----------|---------------|

Santa Claus solicita un informe con la siguiente estructura:

|	Categoría           | Excelente | Categoría Buena |	Categoría Regular |	Totales por Región |
|:-------------------:|:---------:|:---------------:|:-----------------:|:------------------:|
| Nombre Región 1     |           |                 |                   |                    |
| ...                 |           |                 |                   |                    |
| Nombre Región 15    |           |                 |                   |                    |
| Totales x categoría |           |                 |                   |                    |

La categoría del niño dependerá de su nivel de comportamiento:
- Puntaje mayor o igual a 80: Categoría Excelente.
- Puntaje entre 50 y 79: Categoría Buena.
- Puntaje menor a 50: Categoría Regular.

*Nota:* Incluir únicamente los niños que no hayan sido retirados de la lista de Navidad.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Fecha = REGISTRO
      año: N(4)
      mes: 1..12
      dia: 1..31
    FIN_REGISTRO

    Niño = REGISTRO
      clave = REGISTRO
        id_pais: N(5)
        id_niño: N(5)
      FIN_REGISTRO
      nom: AN(30)
      pun: entero
      id_reg: N(5)
      nom_reg: AN(20)
      registro: Fecha
      retiro: Fecha
    FIN_REGISTRO

    Region = REGISTRO
      id_pais: N(5)
      nom_pais: AN(30)
      id_region: N(5)
      nom_region: N(5)
    FIN_REGISTRO

    niños: archivo de niños ordenado por id_pais y id_niño
    nin: Niño
    regiones: archivo de Region indexado por id_pais
    reg: Region
    informe: arreglo [1..16, 1..4] de entero
    i, j, total: entero
  PROCESO
    ABRIR E/ (niños); LEER(niños, nin)
    ABRIR E/S (regiones)

    PARA i := 1 HASTA 16 HACER
      PARA j := 1 HASTA 4 HACER
        informe[i, j] := 0
      FIN_PARA
    FIN_PARA

    MIENTRAS NO FDA(niños) HACER
      reg.id_pais := nin.clave.id_pais
      LEER(regiones, reg)

      SI EXISTE ENTONCES
        i := reg.id_region

        SEGUN nin.pun HACER
          < 50: j := 3
          < 80: j := 2
          >= 80: j := 1
        FIN_SEGUN

        SI (nin.retiro.año = 0) ENTONCES
          informe[i, j] := informe[i, j] + 1
          informe[16, j] := informe[16, j] + 1
          informe[i, 4] := informe[i, 4] + 1
        FIN_SI
      FIN_SI
      LEER(niños, nin)
    FIN_MIENTRAS

    total := 0
    PARA j := 1 HASTA 3 HACER
      total := total + informe[16, j]
    FIN_PARA
    informe[16, 4] := total

    ESCRIBIR(| Región | Excelente | Cat. Buena | Cat. Regular | Total por región |")
    PARA i := 1 HASTA 15 HACER
      reg.id_pais := i
      LEER(regiones, reg)

      SI EXISTE ENTONCES
        ESCRIBIR("Región: ", reg.nom_region)

        PARA j := 1 HASTA 4 HACER
          ESCRIBIR(informe[i, j])
        FIN_PAR
      FIN_SI
    FIN_PARA

    ESCRIBIR("Totales por categoría: ")
    PARA j := 1 HASTA 3 HACER
      ESCRIBIR(informe[16, j])
    FIN_PARA

    ESCRIBIR("Total general de regalos a entregar: ", informe[16, 4])

    CERRAR(niños)
    CERRAR(regiones)
FIN_ACCION
```

</details>
