## Ejercicio 1
Un programa de becas para estudiantes de Ingeniería desea obtener la lista de postulantes
que están en condiciones de acceder a la ayuda económica.
Para ello se posee una secuencia de caracteres con los datos de los postulantes que ya han
aprobado la etapa de análisis de datos previo, y pueden ser evaluados respecto a sus
condiciones económicas. La secuencia, SEC1, posee la siguiente información:

Apellido y Nombre (separados por un espacio en blanco entre sí), Sexo (M o F),
DNI (8 caracteres), Correo Electrónico, Universidad y Carrera.

Todos los datos de un mismo postulante se separan por “|”, y a la vez cada postulante se
separa del otro por un “$”.

*Por ejemplo:*
Perez Juan|M|37878923|jp@gmail.com|UTN|ISI$Romero Maria|F|37234124|mr@gmail.com|UTN|IQ$*

Además se cuenta con una secuencia de números que posee el ingreso familiar.
Por ejemplo, teniendo en cuenta el ejemplo anterior de postulantes: 8000	6000

Ambas secuencias poseen la misma cantidad de datos, es decir al primer postulante de la
primera secuencia le corresponde el primer ingreso familiar de la segunda secuencia y así
sucesivamente.

Se desea una secuencia de salida de los postulantes que no superen los $10000 de ingreso familiar
con el siguiente formato:

Apellido y Nombre (separados por un espacio en blanco entre sí), CUIT y Correo Electrónico.
Todos los datos de un mismo postulante se separan por “|”, y a la vez cada postulante se separa
del otro por un “$”.

Para calcular el CUIT se debe seguir el siguiente procedimiento:
1. Agregar los primeros dos dígitos en función del sexo (27 si es femenino, 20 si es masculino).
2. Agregar un guion medio y seguido el DNI original.
3. Seguido a lo último agregar un guion medio y el código verificador del que se obtiene de la
siguiente forma:
  - Si el primer y último digito del DNI son pares entonces el código es 1.
  - Si en el DNI, el primer digito es impar y el último es par entonces el código es 2.
  - Si en el DNI, el primer digito es par y el último es impar entonces el código es 3.
  - Si el primer y último digito del DNI son impares entonces el código es 4.

La salida quedaría (teniendo en cuenta los ejemplos anteriores) de la siguiente forma:
Perez Juan|20-37878923-4|jp@gmail.com|$Romero Maria|27-37234124-2|mr@gmail.com|$*

Además se pide porcentaje de postulantes que cumplieron la condición económica y porcentaje de
postulantes que no la pudieron cumplir sobre el total.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    postulantes, salida: secuecia de caracter
    car: caracter
    ingresos: secuencia de entero
    num, i, dig1, dig2: entero
    cumplen, no_cumplen, total: entero

    FUNCION convertir(car: caracter): entero ES
      SEGUN car HACER
        '0': convertir := 0
        '1': convertir := 1
        '2': convertir := 2
        '3': convertir := 3
        '4': convertir := 4
        '5': convertir := 5
        '6': convertir := 6
        '7': convertir := 7
        '8': convertir := 8
        '9': convertir := 9
        'a': convertir := 1
        'e': convertir := 2
        'i': convertir := 3
    FIN_FUNCION

    FUNCION calcular_sufijo(primero, segundo: entero): entero ES
      SI primero MOD 2 = 0 ENTONCES
        SI segundo MOD 2 = 0 ENTONCES
          calcular_sufijo := 1
        CONTRARIO
          calcular_sufijo := 3
        FIN_SI
      CONTRARIO
        SI segundo MOD 2 = 0 ENTONCES
          calcular_sufijo := 2
        CONTRARIO
          calcular_sufijo := 4
        FIN_SI
      FIN_SI
    FIN_FUNCION
  PROCESO
    ARR(postulantes); AVZ(postulates, car)
    ARR(ingresos); AVZ(ingresos, num)
    CREAR(salida)

    cumplen := 0; no_cumplen := 0

    MIENTRAS car <> '*' HACER
      SI num > 10000 ENTONCES
        no_cumplen := no_cumplen + 1

        MIENTRAS car <> '$' HACER
          AVZ(postulantes, car)
        FIN_MIENTRAS
        AVZ(postulantes, car)
      CONTRARIO
        cumplen := cumplen + 1

        MIENTRAS car <> '|' HACER
          ESCRIBIR(salida, car)
          AVZ(postulantes, car)
        FIN_MIENTRAS
        ESCRIBIR(salida, car)
        AVZ(postulantes, car)

        ESCRIBIR(salida, '2')
        SI car = 'M' ENTONCES
          ESCRIBIR(salida, '0')
        CONTRARIO
          ESCRIBIR(salida, '7')
        FIN_SI
        ESCRIBIR(salida, '-')

        PARA i := 1 HASTA 8 ENTONCES
          SI i = 1 ENTONCES
            dig1 := convertir(car)
          CONTRARIO
            SI i = 8 ENTONCES
              dig2 := convertir(car)
            FIN_SI
          FIN_SI

          ESCRIBIR(salida, car)
          AVZ(postulantes, car)
        FIN_PARA
        ESCRIBIR(salida, '-')

        sufijo := calcular_sufijo(dig1, dig2)
        ESCRIBIR(salida, sufijo)
        ESCRIBIR(salida, car)
        AVZ(postulantes, car)

        MIENTRAS car <> '|' HACER
          ESCRIBIR(salida, car)
          AVZ(postulantes, car)
        FIN_MIENTRAS
        ESCRIBIR(salida, car)
        AVZ(postulantes, car)

        MIENTRAS car <> '$' HACER
          AVZ(postulantes, car)
        FIN_MIENTRAS
        ESCRIBIR(salida, car)
        AVZ(postulantes, car)
      FIN_SI
    FIN_MIENTRAS
    ESCRIBIR(salida, car)
    AVZ(postulantes, car)

    total := cumplen + no_cumplen

    ESCRIBIR("Del total de alumnos que aplicaron a la beca universitaria, el ", cumplen * 100 / total,
    "% de ellos cumplen con los requisitos, y el restante ", no_cumplen * 100 / total, "% de ellos no son elegibles.")

    CERRAR(postulantes)
    CERRAR(ingresos)
    CERRAR(salida)
FIN_ACCION
```

</details>

## Ejercicio 2
Dado un Archivo que contiene información de los estudiantes a los que se asignaron becas durante
el 2014, cuyos registros tienen el siguiente formato:

ESTUD (Ordenado por Provincia, Universidad, Carrera, CUIT)

| PROVINCIA AN(10) | UNIVERSIDAD AN(20) | CARRERA AN(30) | CUIT N(11) | APE_NOM AN(60) | MONTO N(10, 2) |
|------------------|--------------------|----------------|------------|----------------|----------------|

Se desea obtener el total de estudiantes beneficiarios cuyo monto de beca no supere los $800, informados
por Universidad, Provincia y total general.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Estudiante = REGISTRO
      prov: AN(10)
      univ: AN(20)
      carrera: AN(30)
      cuit: N(11)
      nombre: AN(60)
      monto: N(10, 2)
    FIN_REGISTRO

    entrada: archivo de Estudiante ordenado por prov, univ, carrera, cuit
    reg: Estudiante

    cant_gral, cant_prov, cant_univ: entero
    resg_prov: AN(10)
    resg_univ: AN(20)

    PROCEDIMIENTO corte_provincia() ES
      corte_universidad()
      ESCRIBIR("La cantidad de estudiantes beneficiarios en la provincia de ", resg_prov,
      " cuyas becas no superan los $800 es de: ", cant_prov, " estudiantes.")
      cant_gral := cant_gral + cant_prov
      cant_prov := 0
      resg_prov := reg.prov
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_universidad() ES
      ESCRIBIR("La cantidad de estudiantes beneficiarios pertenecientes a la universidad de ", resg_univ,
      " cuyas becas no superan los $800 es de: ", cant_univ, " estudiantes.")
      cant_prov := cant_prov + cant_univ
      cant_univ := 0
      resg_univ := reg.univ
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (entrada); LEER(entrada, reg)

    resg_prov := reg.prov; resg_univ := reg.univ
    cant_prov := 0; cant_univ := 0; cant_gral := 0

    MIENTRAS NO FDA(entrada) HACER
      SI resg_prov <> reg.prov ENTONCES
        corte_provincia()
      CONTRARIO
        SI resg_univ <> reg.univ ENTONCES
          corte_universidad()
        FIN_SI
      FIN_SI

      SI reg.monto <= 800 ENTONCES
        cant_univ := cant_univ + 1
      FIN_SI

      LEER(entrada, reg)
    FIN_MIENTRAS
    corte_provincia()

    ESCRIBIR("El total general de estudiantes beneficiarios cuyas becas no superan
    el monto de $800 es de: ", cant_gral, " estudiantes.")

    CERRAR(entrada)
FIN_ACCION
```

</details>
