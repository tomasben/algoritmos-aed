Se desea generar una secuencia, a partir de la secuencia del problema 2.01, donde se actualice la fecha de
aprobación del último exámen, para ello se cuenta con información del último turno de exámen, según el siguiente
detalle:

**Fichero EXAMENES:**
| Nro. de Legajo | Carrera | Cód. Materia | Fecha de exámen | Nota |
|----------------|---------|--------------|-----------------|------|

Se debe considerar que no necesariamente todos los alumnos se presentan en cada turno de exámen, y que un
alumno puede presentarse a rendir más de una materia en un mismo turno. Supónganse ambas secuencias
ordenadas por Número de Legajo.

```
ACCION ejercicio ES
  AMBIENTE
    HV = 999999

    Alumno = REGISTRO <- del ejercicio 2.01
      nombre: alfanumerico
      carrera: ("ISI", "IEM", "IQ")
      legajo: N(5)
      fdn: Fecha
      ingreso: Fecha
      documento: N(8)
      sexo: ('M', 'F')
      ult_examen = REGISTRO
        año: N(4)
        mes: 1..12
        dia: 1..31
      FIN_REGISTRO
      nota: N(3)
    FIN_REGISTRO

    Examen = REGISTRO
      legajo: N(5)
      carrera: ("ISI", "IEM", "LAR", "IQ")
      cod_mat: N(2)
      fecha = REGISTRO
        año: N(4)
        mes: 1..12
        dia: 1..31
      FIN_REGISTRO
      nota: ("unicornio", "duquesa", "tricota", ..., "diego") <- N(3) 0..100
    FIN_REGISTRO

    maestro, salida: archivo de Alumno ordenado por legajo
    regmae, regsal, aux: Alumno
    examenes: archivo de Examenes ordenado por legajo
    regex: Examen

    PROCEDIMIENTO leer_alumno() ES
      LEER(maestro, regmae)
      SI FDA(maestro) ENTONCES
        regmae.legajo := HV
      FIN_SI
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO leer_examenes() ES
      LEER(examenes, regex)
      SI FDA(examenes) ENTONCES
        regex.legajo := HV
      FIN_SI
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (maestro); LEER(maestro, regmae)
    ABRIR E/ (examenes); LEER(examenes, regmae)
    ABRIR /S (salida);

    MIENTRAS (regmae.legajo <> HV) O (regex.legajo <> HV) HACER
      SI (regmae.legajo = regex.legajo) ENTONCES
        aux := regmae

        MIENTRAS (aux.legajo = regex.legajo) HACER
          aux.ult_examen := regex.fecha
          leer_examenes()
        FIN_MIENTRAS
        regsal := aux
        ESCRIBIR(salida, regsal)

        leer_alumno()
      CONTRARIO
        SI (regmae.legajo < regex.legajo) ENTONCES
          regsal := regmae
          ESCRIBIR(salida, regsal)
          leer_alumno()
        CONTRARIO
          ESCRIBIR("ERROR: registro no encontrado en el archivo maestro")
          leer_examenes()
        FIN_SI
      FIN_SI
    FIN_MIENTRAS

    CERRAR(maestro)
    CERRAR(examenes)
    CERRAR(salida)
FIN_ACCION
```
