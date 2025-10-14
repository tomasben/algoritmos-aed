## Ejercicio 1
La Secretaría de Turismo de la ciudad de Resistencia habilitó el programa "EcoBici"
para promover el uso de la bici con fines turísticos. Se trata de 6 circuitos para recorrer
14 barrios de la ciudad. Se cuenta con un archivo secuencial con la información de todas las
bicicletas disponibles en la ciudad:

**BICICLETAS** *(ordenado por nro_serie y modelo)*
| Nro_serie | Modelo | Fecha_adquisición | Fecha_ult_mantenimiento | Disponibilidad |
|-----------|--------|-------------------|-------------------------|----------------|

Además se cuenta con información de todas las novedades para una bicicleta. Las mismas pueden
tratarse de movimientos de préstamos, o bien de una novedad respecto a un mantenimiento
realizado a la unidad.

**NOVEDADES** *(ordenado por nro_serie, modelo, tipo_novedad y fecha_novedad)*
| Nro_serie | Modelo | Tipo_novedad | Fecha_novedad | Hora_inicio | Hora_fin | Circuito_nro | ID_usuario |
|-----------|--------|--------------|---------------|-------------|----------|--------------|------------|

Tipo de novedad puede ser:
- Alta de una nueva unidad: cuando se da de alta, la fecha de último mantenimiento debe estar
vacía y la disponibilidad debe ser verdadero.
- Préstamo: no afecta los datos de las bicicletas, la secretaría lo utiliza con fines estadísticos.
- Mantenimiento: implica que deberá actualizarse el campo de disponibilidad y marcarlo como falso,
además de actualizar la fecha de último mantenimiento.

La información de los usuarios que contratan el servicio se encuentra dentro de un archivo indexado
por ID_usuario.

**USUARIOS**
| ID_usuario | DNI | Sexo (M o F) | Apellido y nombre | Domicilio | Localidad | Provincia | Edad |
|------------|-----|--------------|-------------------|-----------|-----------|-----------|------|

Se pide:
1. Desarrollar un algoritmo que permita mantener actualizado el archivo de bicicletas, considerando
que pueden existir múltiples novedades para un mismo número de serie. Considerar cualquier tipo de
error informando por pantalla al usuario.
2. Indicar la cantidad total de préstamos realizados por sexo.

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

    Bicicleta = REGISTRO
      nro_serie: N(5)
      modelo: ('A', 'B', 'C')
      adquisicón: Fecha
      ult_mant: Fecha
      disponibilidad: lógico
    FIN_REGISTRO

    Novedad = REGISTRO
      nro_serie: N(5)
      modelo: ('A', 'B', 'C')
      tipo: ("Alta", "Preśtamo", "Mantenimiento")
      fecha: Fecha
      hora_inicio: N(4)
      hora_fin: N(4)
      circuito: 1..6
      id_usu: N(5)
    FIN_REGISTRO

    Usuario = REGISTRO
      id_usu: N(5)
      dni: N(8)
      sexo: ('M', 'F')
      apeynom: AN(30)
      domicilio: AN(20)
      localidad: AN(20)
      provincia: AN(15)
      edad: N(2)
    FIN_REGISTRO

    HV = 99999
    bicicletas: archivo de Bicicleta ordenado por nro_serie y modelo
    bic: Bicicleta
    novedades: archivo de Novedad ordenado por nro_serie, modelo, tipo y fecha
    nov: Novedad
    usuarios: archivo indexado por nro_usu
    usu: Usuario
    salida: archivo de Bicicleta
    regsal: Bicicleta

    pres_m, pres_f: entero

    PROCEDIMIENTO leer_bicicleta() ES
      LEER(bicicletas, bic)
      SI FDA(bicicletas) ENTONCES
        bic.nro_serie := HV
      FIN_SI
    FIN_PRPOCEDIMIENTO

    PROCEDIMIENTO leer_novedad() ES
      LEER(novedades, bic)
      SI FDA(novedades) ENTONCES
        nov.nro_serie := HV
      FIN_SI
    FIN_PRPOCEDIMIENTO
  PROCESO
    ABRIR E/ (bicicletas); LEER(bicicletas, bic)
    ABRIR E/ (novedades); LEER(novedades, nov)
    ABRIR /S (salida)
    ABRIR E/S (usuarios)

    pres_m := 0; pres_f := 0

    MIENTRAS (bic.nro_serie <> HV) O (nov.nro_serie <> HV) HACER
      SI (bic.nro_serie < nov.nro_serie) ENTONCES
        regsal := bic
        ESCRIBIR(salida, regsal)
        leer_bicicleta()
      CONTRARIO
        SI (bic.nro_serie > nov.nro_serie) ENTONCES
          SEGUN nov.tipo HACER
            "Prestamo": ESCRIBIR("ERROR: no se encontró la bicicleta ", nov.nro_serie, " para realizar el préstamo")
            "Mantenimiento": ESCRIBIR("ERROR: no se encontró la bicicleta ", nov.nro_serie, " para realizarle un mantenimiento")
            "Alta": regsal.nro_serie := nov.nro_serie
                    regsal.modelo := nov.modelo
                    regsal.adquisicion := nov.fecha
                    regsal.ult_mant := nov.fecha
                    disponibilidad: verdadero

                    ESCRIBIR(salida, regsal)
                    leer_novedad()
          FIN_SEGUN
        CONTRARIO
          SEGUN nov.tipo HACER
            "Alta": ESCRIBIR("ERROR: no se puede dar de alta una bicicleta que ya existe")
            "Mantenimiento":  regsal := bic
                              regsal.ult_mant := nov.fecha
                              regsal.disponibilidad := falso

                              ESCRIBIR(salida, regsal)
            "Prestamo": usu.id_usu := nov.id_usu
                        LEER(usuarios, usu)

                        SI EXISTE ENTONCES
                          SEGUN usu.sexo HACER
                            'M': pres_m := pres_m + 1
                            'F': pres_f := pres_f + 1
                          FIN_SEGUN
                        CONTRARIO
                          ESCRIBIR("ERROR: no se encontró el usuario ", nov.id_usu, " para realizar el préstamo")
                        FIN_SI
          FIN_SEGUN

          leer_bicicleta()
          leer_novedad()
        FIN_SI
      FIN_SI
    FIN_MIENTRAS

    ESCRIBIR("De un total de ", pres_m + pres_f, " preśtamos: ")
    ESCRIBIR(pres_m, " fueron préstamos a hombres y ", pres_f, " préstamos a mujeres.")

    CERRAR(bicicletas)
    CERRAR(novedades)
    CERRAR(usuarios)
    CERRAR(salida)
FIN_ACCION
```

</details>

## Ejercicio 2
Considerando el escenario presentado en el ejercicio anterior, la información suministrada en el
archivo de NOVEDADES y también lo siguiente:

Los paseos tienen un costo dependiendo de su duración:
- Paseos intensivos: superan las 6 hs. Tienen un costo fijo inicial de $1500 más un costo variable
dependiendo del circuito y cantidad de horas utilizadas.
- Paseos recreativos: duran 6 hs. o menos. Tienen un costo fijo inicial de $1000 más un costo
variable dependiendo del circuito y cantidad de horas utilizadas.

Los costos variables de los paseos se encuentran en un arreglo de dos dimensiones donde cada posición
corresponde al número de circuito y tipo de paseo, respectivamente.

Se pide:
1. Escribir un algoritmo que calcule: (a) cantidad de préstamos y (b) monto total recaudado por
circuito y por tipo de paseo.

2. Indicar: (a) el circuito con la mayor cantidad de paseos, (b) el total recaudado para un tipo de
paseo y circuito ingresados por el usuario, y (c) el importe total recaudado y la cantidad de paseos
realizados.

Consideraciones:
- Se provee una función "diff_horas" que recibe como parámetros una hora de inicio y una hora de fin
(en formato de registros), y devuelve un entero indicando la diferencia de horas entre ambos registros.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Hora = REGISTRO
      hora: N(2)
      minuto: N(2)
      segundo: N(2)
    FIN_REGISTRO

    Novedad = REGISTRO
      nro_serie: N(5)
      modelo: ('A', 'B', 'C')
      tipo: ("Alta", "Preśtamo", "Mantenimiento")
      fecha: Fecha
      hora_inicio: Hora
      hora_fin: Hora
      circuito: 1..6
      id_usu: N(5)
    FIN_REGISTRO

    i, j, horas, ingreso, linea, total: entero
    novedades: archivo de Novedades ordenado por nro_serie, modelo, tipo y fecha
    nov: Novedad
    ingresos_pas: arreglo [1..7, 1..3] de real
    costos_pas: arreglo [1..6, 1..2] de real
    cantidad_pas: arreglo[1..7] de entero
    cant_prestamos: entero
  PROCESO
    ABRIR E/ (novedades); LEER(novedades)

    cant_prestamos := 0

    PARA i := 0 HASTA 7 HACER
      PARA j := 0 HASTA 3 HACER
        costos[i, j] := 0
      FIN_PARA
    FIN_PARA

    MIENTRAS NO FDA(novedades) HACER
      SI nov.tipo == "Prestamo" ENTONCES
        cant_prestamos := cant_prestamos + 1
      FIN_SI

      i := nov.circuito
      horas := diff_horas(nov.hora_inicio, hora_fin)
      SI (horas > 6) ENTONCES
        ingresos_pas[i, 2] := ingresos_pas[i, 2] + (1500 + costos_pas[i, 2])
      CONTRARIO
        ingresos_pas[i, 1] := ingresos_pas[i, 1] + (1000 + costos_var[i, 1])
      FIN_SI

      // matriz con la cantidad de paseos por circuito
      cantidad_pas[i] := cantidad_pas[i] + 1
      cantidad_pas[7] := cantidad_pas[7] + 1

      LEER(novedades, nov)
    FIN_MIENTRAS

    PARA i := 1 HASTA 6 HACER
      linea := 0
      PARA j := 1 HASTA 2 HACER
        linea := linea + ingresos_pas[i, j]
      FIN_PARA
      ingresos_pas[i, 3] := linea
    FIN_PARA

    total := 0
    PARA j := 1 HASTA 2 HACER
      linea := 0
      PARA i := 1 HASTA 6 HACER
        linea := linea + ingresos_pas[i, j]
      FIN_PARA
      ingresos_pas[7, i] := linea
      total := total + linea
    FIN_PARA
    ingresos_pas[7, 3] := total

    may_pas := cantidad_pas[1]
    may_pas_circ := 1
    PARA i := 2 HASTA 6 HACER
      SI (cantidad_pas[i] > may_pas) ENTONCES
        may_pas := cantidad_pas[i]
        may_pas_circ := i
      FIN_SI
    FIN_PARA
    ESCRIBIR("El circuito con la mayor cantidad de paseos fue el número ", may_pas_circ, " con un total de ", may_pas, " paseos.")

    ESCRIBIR("Ingrese un número de circuito para conocer el monto recaudado: [1..6]")
    LEER(i)
    ESCRIBIR("Ingrese un tipo de paseo para el circuito anteriormente ingresado: [1..2]")
    LEER(j)
    ESCRIBIR("El monto recaudado para el paso seleccionado fue de: $", ingresos_pas[i, j])

    ESCRIBIR("Para un total de ", cantidad_pas[7], " paseos, el monto total recaudado fue de: ", ingresos_pas[7, 3])

    CERRAR(novedades)
FIN_ACCION
```

</details>
