## Ejercicio N° 1
Una cadena de hoteles necesita un informe de ocupación y pagos para el mes de JUNIO. Para
esto, se cuenta con dos secuencias de datos:

**Secuencia de caracteres:**
Estructura: Hotel (cantidad indeterminada de caracteres) & cantidad de reservas (3 caracteres)
hotel & cantidad de reservas....FDS

*Ejemplo:*
| H | o | t | e | l | A | l | a | s | & | 3 | 4 | 0 | H | o | t | e | l | B | a | h | i | a | & | 9 | 9 | 9 | …FDS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|------|

**Secuencia de enteros:**
Estructura: Para cada reserva: Nro de reserva, tipo de habitación (1: single, 2: doble, 3: suite),
cantidad de noches, importe.

*Ejemplo:*
| 1234 | 1 | 3 | 120.000 | 2345 | 3 | 2 | 65.000 |...FDS |
|------|---|---|---------|------|---|---|--------|-------|

Nota: La función ConvertiraNumero(caracter) puede ser utilizada si se considera necesario para
convertir un carácter a un dato entero.

Se pide escribir un algoritmo que permita:
1) Generar una secuencia de salida de caracteres que contenga el nombre de cada hotel y su
cantidad de reservas de habitaciones dobles.
2) Promedio de reservas de habitaciones dobles por hotel.

## Ejercicio N° 2
La cadena de hoteles del ejercicio anterior cuenta con un sistema de gestión de reservas y ahora
le solicita a Ud. un informe de ocupación y facturación para el mes de JUNIO. Para cada reserva
se registra:

RESERVAS, Ordenado por Número de Hotel, Tipo de Habitación, Número de Reserva

| Nro. de Hotel | Tipo de Habitación (IND, DOB, SUITE) | Nro de Reserva | Fecha de ingreso | Cantidad de noches | Importe de la reserva |
|---------------|--------------------------------------|----------------|------------------|--------------------|-----------------------|

Tipo de Habitación: (IND: Individual, DOB: Doble, SUITE: Suite)

Se pide escribir un algoritmo que permita:
1) Imprimir un informe que muestre el total de dinero recaudado por hotel y por tipo de
habitación.
2) Crear un fichero de salida que contenga Número de Hotel y total de dinero recaudado en
habitaciones dobles y suites.

| Nro de Hotel | Total hab. dobles | Total hab. suites |
|--------------|-------------------|-------------------|

3) Informar cuáles son los hoteles que tuvieron mayor recaudación en habitaciones dobles (DOB)
que en suites (SUITE).

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Fecha = REGISTRO
      dia: 1..31
      mes: 1..12
      año: N(4)
    FIN_REGISTRO

    Reserva = REGISTRO
      nro_hotel: entero
      hab: ("IND", "DOB", "SUITE")
      nro_res: entero
      ingreso: Fecha
      noches: entero
      importe: real
    FIN_REGISTRO

    Reporte = REGISTRO
      nro_hotel: entero
      tot_dob: real
      tot_sui: real
    FIN_REGISTRO

    entrada: archivo de Reserva ordenado por nro_hot, tipo_hab, nro_res
    res: Reserva
    salida: archivo de Reporte
    rep: Reporte

    cant_ind, cant_dob, cant_sui, cant_hotel: real
    resg_hotel: entero
    resg_hab: AN(5)

    PROCEDIMIENTO corte_habitacion() ES
      SEGUN resg_hab HACER
        "IND": cant_hotel := cant_hotel + cant_ind
        "DOB": cant_hotel := cant_hotel + cant_dob
        "SUITE": cant_hotel := cant_hotel + cant_sui
      FIN_SEGUNtipo_
      resg_hab := res.hab
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_hotel() ES
      corte_habitacion()
      ESC("El total recaudado por el hotel ", resg_hotel, " fue de ", cant_hotel)
      ESC("de los cuales ", cant_ind, " corresponden a habitaciones individuales, ")
      ESC(cant_dob, " corresponden a habitaciones dobles")
      ESC("y ", cant_ind, " corresponden a habitaciones de tipo suite")

      SI cant_dob > cant_sui ENTONCES
        ESC("El hotel ", resg_hotel, " tuvo más personas hospedadas en
        habitaciones de tipo doble que de tipo suite")
      FIN_SI

      rep.nro_hotel := resg_hotel; rep.tot_dob := cant_dob; rep.tot_sui := cant_sui;
      GRABAR(salida, rep)
      cant_ind := 0; cant_dob := 0; cant_sui := 0; cant_hotel := 0;
      resg_hotel := res.nro_hotel
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (entrada); LEER(entrada, res)
    ABRIR /S (salida)

    cant_ind := 0; cant_dob := 0; cant_sui := 0; cant_hotel := 0;
    resg_hotel := res.nro_hotel; resg_hab := res.hab

    MIENTRAS NO FDA(entrada) HACER
      SI resg_hotel <> res.nro_hotel ENTONCES
        corte_hotel()
      CONTRARIO
        SI resg_hab <> res.hab ENTONCES
          corte_habitacion()
        FIN_SI
      FIN_SI

      SEGUN res.hab HACER
        "IND": cant_ind := cant_ind + res.importe
        "DOB": cant_dob := cant_dob + res.importe
        "SUITE": cant_sui := cant_sui + res.importe
      FIN_SI

      LEER(entrada, res)
    FIN_MIENTRAS

    CERRAR(entrada)
    CERRAR(salida)
FIN_ACCION
```

</details>
