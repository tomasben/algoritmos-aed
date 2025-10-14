## Ejercicio 1
El régimen de jubilaciones para docentes universitarios establece que, según las leyes
vigentes, podrán acceder al beneficio jubilatorio quienes cumplan determinados requisitos:

- Edad: entre 65 y 70 años para los hombres, entre 60 y 70 para las mujeres.
- Aportes: mínimo 30 años de aportes.

La Facultad Regional Resistencia cuenta con dos secuencias, una de caracteres y otra de
enteros, con las siguientes características:

**Formato de la secuencia Docentes (de caracteres):**
RegionalSexoLegajoNombreCompleto#SexoLegajoNombreCompleto+RegionalSexoLegajoNombreCompleto#SexoLegajoNombreCompleto+FDS

Donde:
- Regional: tres caracteres que indican la facultad regional.
- Sexo: un carácter, que puede ser "M" o "F".
- Legajo: cinco caracteres que indican el legajo.
- NombreCompleto: cantidad indefinida de caracteres que indica el nombre, que finaliza con
el signo "#".

Consideraciones de la secuencia Docentes:
- Los docentes de una misma regional terminan con el signo "+".
- La regional siempre es FR seguido de un carácter, que es la inicial de la provincia.

*Ejemplo de la secuencia Docentes:*
FRMM22711Pedro González#F19245Mónica Martínez+...#...+...#...+FDS

**Formato de la secuencia Edad (de enteros):**
EdadAportes

Donde:
- Edad: dos dígitos que indican la edad.
- Aportes: dos dígitos que indican los años de aportes.

Consideraciones de la secuencia Edad:
- Existe una correspondencia uno a uno entre cada subsecuencia de Docentes y cada par
Edad-Aportes de la secuencia Edad.

*Ejemplo de la secuencia Edad:*
67205030...FDS

Para el primer par de valores, la persona tiene 67 años y 20 años de aportes.

Se pide:
1. Generar una secuencia de caracteres llamada Jubilar, solo para docentes de una región
específica ingresada por el usuario, que debe contener el legajo y nombre completo de los
docentes en condiciones de jubilarse.
2. Informar por regional la cantidad de docentes que pueden jubilarse y la cantidad de
docentes que no pueden.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    docentes, jubilar: secuencia de caracter
    car: caracter
    edad: secuencia de entero
    num: entero

    reg_eleg, reg_ac: caracter
    ed, apor, jub, no_jub: entero
    condicion: logico
  PROCESO
    ARR(docentes); AVZ(docentes, car)
    ARR(edad); AVZ(edad, num)
    CREAR(jubilar)

    ESCRIBIR("Ingrese el caracter correspondientes a la regional FR
    de la cual se desea conocer los docentes en condicion de jubilarse: ")
    LEER(reg_ac)

    MIENTRAS NO FDS(docentes) HACER
      AVZ(docentes, car)
      AVZ(docentes, car)

      // almaceno la regional actual
      reg_ac := car
      AVZ(docentes, car)

      MIENTRAS car <> '+' HACER
        ed := num; AVZ(edad, num)
        apor := num; AVZ(edad, num)

        // chequeo la condicion de jubilacion y la guardo para usarla luego
        SI car = 'M' Y ed >= 65 Y ed <= 70 ENTONCES
          condicion := verdadero
          jub := jub + 1
        CONTRARIO
          SI car = 'F' Y ed >= 60 Y ed <= 70 ENTONCES
            jub := jub + 1
            condicion := verdadero
          CONTRARIO
            no_jub := no_jub + 1
            condicion := falso
          FIN_SI
        FIN_SI
        AVZ(docentes, car) <- avanzo el caracter 'M' o 'F'

        SI reg_ac = reg_eleg Y condicion ENTONCES
          MIENTRAS car <> '+' Y car <> '#' HACER
            ESCRIBIR(jubilar, car)
            AVZ(docentes, car)
          FIN_MIENTRAS
        CONTRARIO
          MIENTRAS car <> '+' Y car <> '#' HACER
            AVZ(docentes, car)
          FIN_MIENTRAS
        FIN_SI
      FIN_MIENTRAS

      ESCRIBIR("La cantidad de docentes que se pueden jubilar, y los que no, para la FR", reg_ac,
      " es de: ", jub, " Y ", no_jub, " docentes, respectivamente.")

      jub := 0; no_jub := 0;
      AVZ(docentes, car) <- avanzo el '+' que separa regionales
    FIN_MIENTRAS

    CERRAR(docentes)
    CERRAR(edad)
    CERRAR(jubilar)
FIN_ACCION
```

</details>

## Ejercicio 2
Consigna: la Universidad Tecnológica Nacional dispone de un archivo secuencial denominado
JUBILAR con los datos de los docentes en condiciones de jubilarse, ordenado por regional,
carrera y número de legajo.

| Regional | Carrera | Legajo N(5) | Sexo | Nombre |
|----------|---------|-------------|------|--------|

Se pide:
1. Informar la cantidad de docentes en condiciones de jubilarse por carrera, por regional
y el total general. Los totales por carrera deben mostrarse discriminados por sexo, mientras
que los demás deben mostrarse en general, sin discriminar por sexo.
2. Informar la regional con mayor cantidad de docentes (total de ambos sexos) en condiciones
de jubilarse.
3. Generar un archivo de salida con la siguiente estructura:

| Regional | Cantidad Jubilados |
|----------|--------------------|

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Docente = REGISTRO
      regional: AN(3)
      carrera: ("ISI", "IEM", "IQ", "LAR")
      legajo: N(5)
      sexo: caracter
      nombre: AN(30)
    FIN_REGISTRO

    Informe = REGISTRO
      regional: AN(3)
      cantidad_jub: entero
    FIN_REGISTRO

    jubilar: archivo de Docente ordenado por regional, carrera, legajo
    doc: Docente
    salida: archivo de Informe
    inf: Informe

    may_jub: entero
    may_reg: AN(3)
    cant_carrm, cant_carrf, cant_reg, cant_gral: entero
    resg_carr, resg_reg: AN(3)

    PROCEDIMIENTO corte_regional() ES
      corte_carrera()
      ESCRIBIR("La cantidad de docentes en condición de jubilarse para la regional ",
      resg_reg, " es de: ", cant_reg, " profesores.")
      cant_gral := cant_gral + cant_reg

      inf.regional := resg_reg
      inf.cantidad_jub := cant_reg
      ESCRIBIR(salida, inf)

      SI cant_reg > may_jub ENTONCES
        may_jub := cant_reg
        may_reg := resg_reg
      FIN_SI

      cant_reg := 0
      resg_reg := doc.regional
    FIN_PROCEDIMIENTO

      PROCEDIMIENTO corte_carrera() ES
        ESCRIBIR("La cantidad de docentes en condición de jubilarse, pertenecientes a la carrera ",
        resg_carr, " es de: ", cant_carrf, " profesoras y ", cant_carrm, " profesores.")
        cant_reg := cant_reg + cant_carrf + cant_carrm
        cant_carrf := 0
        cant_carrm := 0
        resg_carr := doc.carrera
      FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (jubilar); LEER(jubilar, doc)
    ABRIR /S (salida)

    resg_reg := doc.regional; resg_carr := doc.carrera
    cant_reg := 0; cant_gral := 0; cant_carrf := 0; cant_carrm := 0
    may_jub := 0;

    MIENTRAS NO FDA(jubilar) HACER
      SI resg_reg <> doc.regional ENTONCES
        corte_regional()
      CONTRARIO
        SI resg_carr <> doc.carrera ENTONCES
          corte_carrera()
        FIN_SI
      FIN_SI

      SI doc.sexo = 'M' ENTONCES
        cant_carrm := cant_carrm + 1
      CONTRARIO
        cant_carrf := cant_carrf + 1
      FIN_SI

      LEER(jubilar, doc)
    FIN_MIENTRAS
    corte_regional()

    ESCRIBIR("El total de docentes en condiciones de jubilarse es de: ", cant_gral, " docentes.")
    ESCRIBIR("De los cuales la mayor cantidad fue de ", may_jub, " pertenecientes
    a la facultad regional ", may_reg)

    CERRAR(jubilar)
    CERRAR(salida)
FIN_ACCION
```

</details>
