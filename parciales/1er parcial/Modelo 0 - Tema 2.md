## Ejercicio 1
Se acerca el Mundial de fútbol de Qatar 2022 y los organizadores desean conocer las estadísticas de
reservas realizadas a cada uno de los estadios de fútbol que serán sedes del torneo mundial durante
la primera jornada de partidos.

Para esto se cuenta con información de todas las reservas realizadas a cada una de las plazas de los
estadios en una secuencia de datos con la siguiente estructura:

NombreEstadio%Capacidad#TipoReservaRazónSocial%!AsientosReservados_TipoReservaRazónSocial%AsientosReservados_
@NombreEstadio#TipoReservaRazónSocial%!AsientosReservados_TipoReservaRazónSocial%AsientosReservados_@...@FDS

En donde:
- NombreEstadio: cantidad de caracteres indefinida, indica el nombre del estadio.
- Capacidad: Dos caracteres que indican la capacidad de espectadores del estadio en miles de espectadores.
- TipoReserva: 1 carácter que indica quién realiza la reserva, posibles valores: E (Empresa) - P (Particular) - Y (Protocolo)
- RazónSocial: el nombre de quien realiza la reserva.
- AsientosReservados: cantidad de caracteres indefinida, teniendo en cuenta la siguiente estructura:
3 caracteres con el formato CAA, donde C indica la zona (A..Z) y AA indica el número de asiento (2 caracteres).

Escribir un algoritmo que permita:

Informar, para cada estadio:
  a) La cantidad de reservas de cada tipo (Empresa-Particular-Protocolo).
  b) La cantidad de reservas realizadas en una zona en particular del estadio, ingresada por el usuario.

Generar una secuencia de salida de enteros, donde cada elemento indicará la cantidad de reservas para cada estadio.

```
ACCION ejercicio ES
  AMBIENTE
    entrada: secuencia de caracter
    car: caracter
    salida: secuencia de entero
    cant_emp, cant_par, cant_pro: entero
    asientos_tot, asientos: entero
    zona: caracter
    i: N(1)
  PROCESO
    ARR(entrada); AVZ(entrada, car)
    CREAR(salida)

    cant_emp := 0; cant_par := 0; cant_pro := 0;
    asientos_tot := 0; asientos := 0;

    ESC("Ingrese un caracter de acuerdo a la zona que se desea conocer la cantidad de reservas: A-Z")
    LEER(zona)

    MIENTRA NO FDS(entrada) HACER
      MIENTRAS car <> '%' HACER
        AVZ(entrada, car)
      FIN_MIENTRAS
      AVZ(entrada, car)

      PARA i := 1 HASTA 2 HACER
        AVZ(entrada, car)
      FIN_PARA
      AVZ(entrada, car)

      SEGUN car HACER
        'E': cant_emp := cant_emp + 1
        'P': cant_par := cant_par + 1
        'Y': cant_pro := cant_pro + 1
      FIN_SEGUN
      AVZ(entrada, car)

      MIENTRAS car <> '%' HACER
        AVZ(entrada, car)
      FIN_MIENTRAS
      AVZ(entrada, car)

      MIENTRAS car <> '_' HACER
        SI car = zona ENTONCES
          asientos := asientos + 1
        FIN_SI
        asientos_tot := asientos_tot + 1
        AVZ(entrada, car)
        AVZ(entrada, car)
        AVZ(entrada, car)
      FIN_MIENTRAS
      AVZ(entrada, car)

      SEGUN car HACER
        'E': cant_emp := cant_emp + 1
        'P': cant_par := cant_par + 1
        'Y': cant_pro := cant_pro + 1
      FIN_SEGUN
      AVZ(entrada, car)

      MIENTRAS car <> '%' HACER
        AVZ(entrada, car)
      FIN_MIENTRAS
      AVZ(entrada, car)

      MIENTRAS car <> '_' HACER
        SI car = zona ENTONCES
          asientos := asientos + 1
        FIN_SI
        asientos_tot := asientos_tot + 1
        AVZ(entrada, car)
        AVZ(entrada, car)
        AVZ(entrada, car)
      FIN_MIENTRAS
      AVZ(entrada, car)
      AVZ(entrada, car)

      ESCRIBIR(salida, asientos_tot)
      ESCRIBIR("La cantidad de reservas según el tipo fueron: ")
      ESCRIBIR("Tipo 'Empresa': ", cant_emp)
      ESCRIBIR("Tipo 'Particular': ", cant_par)
      ESCRIBIR("Tipo 'Protocolo': ", cant_pro)

      ESCRIBIR("Y la cantidad de asientos reservados para la zona elegida ", zona,
      " fuerob: ", asientos)

      cant_emp := 0; cant_par := 0; cant_pro := 0;
      asientos_tot := 0; asientos := 0;
    FIN_MIENTRAS

    CERRAR(entrada)
    CERRAR(salida)
FIN_ACCION
```

## Ejercicio 2
Además, en pos de analizar la capacidad hotelera de Qatar, el Ministerio de Turismo, solicitó a todos
los hoteles el estado habitacional de cada cadena de hoteles.
Luego realizó la carga de toda esa información en un archivo secuencial con la siguiente estructura:

| codigo_cadena AN(15) | nivel_hotel (1..5) | codigo_hotel N(4) | nombre_hotel AN(50) | es_ciudad_sede (logico) | cantidad_habitaciones N(4) |
|----------------------|--------------------|-------------------|---------------------|-------------------------|----------------------------|

Ejemplos de cadenas hoteleras: Sheraton - hilton - NH.
El archivo se encuentra ordenado por los campos codigo_cadena y nivel.

El Ministerio organizó un concurso para todos los alumnos de ISI que hayan aprobado Algoritmos y Estructuras de datos, ofreciendo un premio en dólares para quien desarrolle la mejor solución.

La consigna solicita:
- Generar un informe que muestre por nivel, cadena y total general: Total de hoteles con más de 300 habitaciones que se encuentren en ciudades sedes del Mundial de fútbol.
- Generar un fichero de salida que contenga los siguientes datos de los hoteles que se encuentran en ciudades sede del Mundial de fútbol: codigo_cadena, nivel_hotel, codigo_hotel, nombre_hotel y cantidad_habitaciones.

```
ACCION ejercicio2 ES
  AMBIENTE
    Cadena = REGISTRO
      codigo_cadena: AN(15)
      nivel_hotel: N(1)
      codigo_hotel: N(4)
      nombre_hotel: AN(50)
      es_ciudad_sede: logico
      cantidad_habitaciones: N(4)
    FIN_REGISTRO

    Reporte = REGISTRO
      codigo_cadena: AN(15)
      nivel_hotel: N(1)
      codigo_hotel: N(4)
      nombre_hotel: AN(50)
      cantidad_habitaciones: N(4)
    FIN_REGISTRO

    entrada: archivo de Cadena ordenado por codigo_cadena, nivel_hotel
    cad: Cadena
    salida: archivo de Reporte
    rep: Reporte

    cant_nivel, cant_cadena, cant_gral: entero
    resg_nivel: N(1)
    resg_cadena: AN(15)

    PROCEDIMIENTO corte_nivel() ES
      ESCRIBIR("La cantidad de hoteles de nivel ", resg_nivel, " con más de
      300 habitaciones y en ciudad sede es de: ", cant_nivel)
      cant_cadena := cant_cadena + cant_nivel
      cant_nivel := 0
      resg_nivel := cad.nivel_hotel
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO corte_cadena() ES
      corte_nivel()
      ESCRIBIR("La cantidad de hoteles pertenecientes a la cadena ", resg_cadena,
      " que cumplen con las condiciones es de: ", cant_cadena)
      cant_gral := cant_gral + cant_cadena
      cant_cadena := 0
      resg_cadena := cad.codigo_cadena
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (entrada); LEER(entrada, cad)
    ABRIR /S (salida)

    resg_cadena := cad.codigo_cadena; resg_nivel := cod.nivel_hotel
    cant_nivel := 0; cant_cadena := 0; cant_gral := 0

    MIENTRAS NO FDA(entrada) HACER
      SI resg_cadea <> cad.codigo_cadena ENTONCES
        corte_cadena()
      CONTRARIO
        SI resg_nivel <> cad.nivel_hotel ENTONCES
          corte_nivel()
        FIN_SI
      FIN_SI

      SI cad.cantidad_habitaciones > 300 Y cad.es_ciudad_sede ENTONCES
        cant_nivel := cant_nivel + 1
      FIN_SI

      SI cad.es_ciudad_sede ENTONCES
        rep.codigo_cadena := cad.codigo_cadena
        rep.nivel_hotel := cad.nivel_hotel
        rep.codigo_hotel := cad.codigo_hotel
        rep.nombre_hotel := cad.nombre_hotel
        rep.cantidad_habitaciones := cad.cantidad_habitaciones

        ESCRIBIR(salida, rep)
      FIN_SI

      LEER(entrada, cad)
    FIN_MIENTRAS

    ESCRIBIR("La cantidad total de hoteles ubicados en ciudades sede del
    evento y con más de 300 habitaciones es de: ", cant_gral)

    CERRAR(entrada)
    CERRAR(salida)
FIN_ACCION
```
