## Ejercicio 1
En Julio próximo se realizará la Bienal de Esculturas en Resistencia.
Como aporte tecnológico, la Fundación Urunday ha solicitado una aplicación
que permita la decodificación de información almacenada en códigos QR. Cada
código decodificado se guarda en una secuencia de caracteres con el siguiente formato:

Continente (A-América, E-Europa, F-África), Nombre del Escultor (alfanumérico de 30 caracteres),
Año de Inicio en la disciplina (4 dígitos). Cada escultor se separa del otro con el símbolo "|".

Sin embargo en el proceso de decodificación se registraron errores en la información
correspondiente a algunos de los escultores de Europa, pues en el año de inicio se almacenó
en el último dígito una vocal (a= 1, e = 2, i=3).

Por ello le solicitan a Ud que diseñe un algoritmo en pseudocódigo que permita:
1. Generar tres secuencias de salida, separando escultores por continente. Tener en cuenta que para
la secuencia de Europa hay que verificar y corregir el error del último dígito del año de inicio.
2. Informar cantidad de escultores por continente que hayan comenzado en la disciplina después del año 2000.
3. Informar porcentaje de escultores con información errónea sobre el total de escultores.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    escultores, america, europa, africa: secuencia de caracter
    car, cont: caracter
    total, esc_am, esc_eu, esc_af, esc_err: entero
    i, j, año; entero

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

    PROCEDIMIENTO escribir_sec(sec: secuencia de caracter, car: caracter) ES
      ESCRIBIR(sec, car)
      AVZ(escultores, car)
    FIN_PROCEDIMIENTO
  PROCESO
    ARR(escultores); AVZ(escultores, car)
    CREAR(america); CREAR(europa); CREAR(africa)

    total := 0; año := 0; esc_err := 0
    esc_am := 0; esc_eu := 0; esc_af := 0

    MIENTRAS NO FDS(escultores) HACER
      cont := car
      AVZ(escultores, car)

      // Escribo el nombre entero del artista en su secuencia de salida correspondiente
      PARA i := 1 HASTA 30 HACER
        SEGUN cont HACER
          'A': escribir_sec(america, car)
          'E': escribir_sec(europa, car)
          'F': escribir_sec(africa, car)
        FIN_SEGUN
      FIN_PARA

      // Saco el año de comienzo y tambien lo escribo en la salida
      PARA j := 3 HASTA 0, -1 HACER
        SEGUN cont HACER
          'A': escribir_sec(america, car)
          'E': escribir_sec(europa, car)
          'F': escribir_sec(africa, car)
        FIN_SEGUN

        SI car = 'a' O car = 'e' O car = 'i' ENTONCES
          esc_err := esc_err + 1
        FIN_SI

        año := año + convertir(car) * 10 ** j
        AVZ(escultores, car)
      FIN_PARA

      // Añado 1 por cada artista procesado
      total := total + 1

      SI año >= 2000 ENTONCES
        SEGUN cont HACER
          'A': esc_am := esc_am + 1
          'E': esc_eu := esc_eu + 1
          'F': esc_af := esc_af + 1
        FIN_SEGUN
      FIN_SI

      // Avanzo el caracter final '|' que separa artistas
      AVZ(escultores, car)
      año := 0
    FIN_MIENTRAS

    ESCRIBIR("La cantidad de escultores que comenzaron sus actividades
    luego de los años 2000, separados por continente, fueron: ")
    ESCRIBIR("América: ", esc_am)
    ESCRIBIR("Europa: ", esc_eu)
    ESCRIBIR("Africa: ", esc_af)

    ESCRIBIR("De los ", total, " artistas, ", esc_err, " de ellos
    contenian errores en la definición del año de comienzo.")

    CERRAR(escultores); CERRAR(america)
    CERRAR(europa); CERRAR(africa)
FIN_ACCION
```

</details>

## Ejercicio 2
La Fundación Urunday cuenta con un archivo con información de emplazamiento de esculturas en la ciudad.

ECL, ordenado por AÑO, MES, MATERIAL, CODIGO

| AÑO N(4) | MES N(2) | MATERIAL (M: Mármol - D: Madera) | CODIGO AN(12) | NOMBRE AN(20) |
|----------|----------|----------------------------------|---------------|---------------|

Realizar un algoritmo en pseudocódigo que permita:
1. Obtener un informe con el total de esculturas emplazadas por Año, Mes y Material. Y un total general.
Dar al informe el formato que considere adecuado.
2. Generar un archivo de salida con la cantidad de esculturas emplazadas por mes durante el año 2015.

EMPL, ordenado por MES, MATERIAL

| MES N(2) | MATERIAL (M:Mármol - D:Madera) | CANT N(3) |
|----------|--------------------------------|-----------|

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Escultura = REGISTRO
      año: N(4)
      mes: 1..12
      material: ('M', 'D')
      escultor: AN(30)
    FIN_REGISTRO

    Informe = REGISTRO
      mes: 1..12
      material: caracter
      cant: N(3)
    FIN_REGISTRO

    entrada: archivo de Escultura ordenado por año, mes, material
    esc: Escultura
    salida: archivo de Informe
    inf: Informe

    cant_gral, cant_año, cant_mes, cant_mat: entero
    resg_año: N(4)
    resg_mes: 1..12
    resg_mat: caracter

    PROCEDIMIENTO corte_año() ES
      corte_mes()
      ESCRIBIR("Durante el año ", resg_año, " se construyeron ", cant_año, " esculturas.")
      cant_gral := cant_gral + cant_año
      cant_año := 0
      resg_año := esc.año
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_mes() ES
      corte_material()
      ESCRIBIR("En el mes nro ", resg_mes, " se realizaron ", cant_mes, " esculturas.")
      cant_año := cant_año + cant_mes

      SI esc.año = 2015 ENTONCES
        inf.mes := resg_mes
        inf.material := resg_mat
        inf.cant := cant_mes
        ESCRIBIR(salida, inf)
      FIN_SI

      cant_mes := 0
      resg_mes := esc.mes
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_material() ES
      ESCRIBIR("La cantidad de esculturas realizadas a base de ", resg_mat,
      " es de ", cant_mat, " esculturas.")
      cant_mes_mad := cant_mes + cant_mat
      cant_mat := 0
      resg_mat := esc.material
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (entrada); LEER(entrada, esc)
    ABRIR /S (salida)

    resg_año := esc.año; resg_mes := esc.mes; resg_mat := esc.material
    cant_gral := 0; cant_año := 0; cant_mes := 0; cant_mat := 0

    MIENTRAS NO FDA(entrada) HACER
      SI resg_año <> esc.año ENTONCES
        corte_año()
      CONTRARIO
        SI resg_mes <> esc.mes ENTONCES
          corte_mes()
        CONTRARIO
          SI resg_mat <> esc.material ENTONCES
            corte_material()
          FIN_SI
        FIN_SI
      FIN_SI

      cant_mat := cant_mat + 1
      LEER(entrada, esc)
    FIN_MIENTRAS
    corte_año()

    ESCRIBIR("La cantidad total de esculturas presentadas en la bienal
    fue de: ", cant_gral, " esculturas.")

    CERRAR(entrada)
    CERRAR(salida)
FIN_ACCION
```

</details>
