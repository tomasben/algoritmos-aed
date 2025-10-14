## Ejercicio 1
Debido a la euforia desatada por las figuritas de Catar 2022, un grupo de estudiantes
de Algoritmos y Estructuras de Datos de Ingeniería de Sistemas ha decidido desarrollar
un algoritmo para poder administrar sus álbumes. Para esto, han generado un archivo
secuencial de movimientos con las figuritas disponibles para intercambios:

**INTERCAMBIOS:** *(ordenado por cod_figurita, cod_amigo)*
| cod_figurita N(5) | cod_amigo N(5) | fecha_solicitud |
|-------------------|----------------|-----------------|

Cada estudiante dispone de la información de su álbum, con las figuritas disponibles
al momento, en un archivo secuencial con el siguiente formato:

**ÁLBUM:** *(ordenado por cod_figurita)*
| cod_figurita N(5) | cantidad N(2) | permitir_duplicados ("SI", "NO") |
|-------------------|---------------|----------------------------------|

Se necesita generar un algoritmo en pseudocódigo que permita actualizar el álbum de
figuritas de un estudiante, teniendo en cuenta que:
1. En caso de no existir la figurita en ÁLBUM, se deberá crear un registro en el archivo,
con la cantidad inicializada en 1 y con el campo permitir_duplicados en "NO", siempre
y cuando la fecha de solicitud no haya expirado (debe ser inferior a siete días de la
fecha actual). Caso contrario, el registro no debe ser incorporado al archivo, ni tampoco
sus movimientos siguientes.

NOTA: considerar que existe una función **diff_días** que recibe como parámetro el número
de días y una fecha, y devuelve verdadero o falso si la fecha actual supera en días ala
fecha que recibe como parámetro.
2. En caso de coincidencias, se deberá verificar si la figurita permite duplicados. En
caso de permitirlo, se deberá incrementar la cantidad disponible en el archivo ÁLBUM.
3. Pueden existir múltiples solicitudes de intercambios con el mismo cod_figurita.

Al finalizar, indicar la cantidad de figuritas duplicadas que se admitieron en
el álbum.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Intercambio = REGISTRO
      cod_fig: N(5)
      cod_ami: N(5)
      solicitud = REGISTRO
        año: N(4)
        mes: 1..12
        dia: 1..31
      FIN_REGISTRO
    FIN_REGISTRO

    Figura = REGISTRO
      cod_figura: N(5)
      cantidad: N(2)
      perm_dup: ("SI", "NO")
    FIN_REGISTRO

    HV = 99999
    intercambios: archivo de Intercambio ordenado por cod_fig y cod_ami
    int: Intercambio
    album: archivo de Figura ordenado por cod_fig
    fig, aux: Figura
    salida: archivo de Figura ordenado
    regsal: Figura

    cant_dup: entero

    PROCEDIMIENTO leer_intercambio() ES
      LEER(intercambios, int)
      SI FDA(intercambios) ENTONCES
        int.cod_fig := HV
      FIN_SI
    FIN_PROCEDIMIENTO

    PROCEDIMIENTO leer_album() ES
      LEER(album, fig)
      SI FDA(album) ENTONCES
        fig.cod_fig := HV
      FIN_SI
    FIN_PROCEDIMIENTO
  PROCESO
    ABRIR E/ (intercambios)
    ABRIR E/ (album)
    ABRIR /S (salida)

    leer_intercambio()
    leer_album()

    cant_dup := 0

    MIENTRAS (fig.cod_fig <> HV) O (int.cod_fig <> HV) HACER
      SI (fig.cod_fig < int.cod_fig) ENTONCES
        regsal := fig
        ESCRIBIR(salida, regsal)
        leer_album()
      CONTRARIO
        SI (fig.cod_fig > int.cod_fig) ENTONCES
          aux.cod_fig := int.cod_fig
          aux.cantidad := 1
          aux.perm_dup := "NO"

          MIENTRAS (aux.cod_fig = int.cod_fig) HACER
            leer_intercambio()
          FIN_MIENTRAS

          regsal := aux
          ESCRIBIR(salida, regsal)
        CONTRARIO
          SI (fig.perm_dup = "SI") ENTONCES
            aux := fig

            MIENTRAS (aux.cod_fig = int.cod_fig) HACER
              cant_dup := cant_dup + 1
              aux.cantidad := aux.cantidad + 1
            FIN_MIENTRAS
          FIN_SI
        FIN_SI
      FIN_SI
    FIN_MIENTRAS

    ESCRIBIR("Se admitieron ", cant_dup, " figuras duplicadas en el álbum.")

    CERRAR(intercambios)
    CERRAR(album)
    CERRAR(salida)
FIN_ACCION
```

</details>

## Ejercicio 2
Teniendo en cuenta que la información de los álbumes de todos los usuarios se encuentra
en el archivo ÁLBUM, y que se tiene además el archivo AMIGOS descrito más abajo:

**ÁLBUM:** *(ordenado por cod_usuario)*
| cod_usuario N(5) | cod_figurita N(5) | cantidad N(2) | tipo |
|------------------|-------------------|---------------|------|

El campo tipo indica:
- Álbum Dorado (D)
- Álbum Común (C)
- Álbum Virtual (V)

La información de los amigos se encuentra dentro de un archivo indexado por
cod_usuario:

**AMIGOS:**
| cod_usuario N(5) | apellido | nombre | celular |
|------------------|----------|--------|---------|

Escriba un algoritmo que permita obtener totales por usuarios y tipo de álbum, que
los muestre por pantalla y además informe al final lo siguiente (considerando que
en el archivo ÁLBUM solo existen 10 usuarios en total):
1. El nombre y apellido del usuario que más figuritas coleccionó.
2. Porcentaje de figuritas descubiertas de cada usuario.

<details>
<summary>Solución</summary>

```
ACCION ejercicio ES
  AMBIENTE
    Figura = REGISTRO
      cod_usu: N(5)
      cod_fig: N(5)
      cantidad: N(2)
      tipo: ('D', 'C', 'V')
    FIN_REGISTRO

    Usuario = REGISTRO
      cod_usu: N(5)
      ape: N(20)
      nom: N(20)
      celular: N(10)
    FIN_REGISTRO

    album: archivo de Figura ordenado por cod_usu
    fig: Figura
    amigos: archivo de Usuario indexado por cod_usu
    usu: Usuario

    i, j, may_cart: entero
    may_cart_nom, may_cart_ape: AN(20)
    cartas: arreglo [1..11, 1..4] de entero

    FUNCION inferir_tipo(car: caracter): entero ES
      SEGUN car HACER
        'D': inferir_tipo := 1
        'C': inferir_tipo := 2
        'V': inferir_tipo := 3
      FIN_SEGUN
    FIN_FUNCION
  PROCESO
    ABRIR E/ (album); LEER(album, fig)
    ABRIR E/S (amigos)

    PARA i := 1 HASTA 10 HACER
      PARA j := 1 HASTA 3 HACER
        cartas[i, j] := 0
      FIN_PARA
    FIN_PARA

    MIENTRAS NO FDA(album) HACER
      i := fig.cod_usu
      j := inferir_tipo(fig.tipo)

      cartas[i, j] := cartas[i, j] + fig.cantidad
      cartas[i, 4] := cartas[i, 4] + fig.cantidad
      cartas[11, j] := cartas[11, j] + fig.cantidad
      cartas[11, 4] := cartas[11, 4] + fig.cantidad

      LEER(album, fig)
    FIN_MIENTRAS

    may_cart := 0
    PARA i := 1 HASTA 10 HACER
      SI may_cart < cartas[i, 4] ENTONCES
        may_cart := cartas[i, 4]

        usu.cod_usu := i
        LEER(amigos, usu)

        SI EXISTE ENTONCES
          may_cart_nom := usu.nom
          may_cart_ape := usu.ape
        CONTRARIO
          ESCRIBIR("ERROR: no se encontró la información asociada al código de usuario: ", usu.cod_usu)
        FIN_SI
      FIN_SI

      ESCRIBIR("Para el usuario N°", i)
      ESCRIBIR("El total de figuritas descubiertas fue de: ", cartas[i, 4])
      ESCRIBIR("El porcentaje en posesión sobre el total de cartas es de: ", (cartas[i, 4] / cartas[11, 4]) * 100, "%")
    FIN_PARA

    ESCRIBIR("El usuario con la mayor cantidad de cartas coleccionadas fue: ", may_cart_ape, ", ", may_cart_nom)

    CERRAR(album)
    CERRAR(amigos)
FIN_ACCION
```

</details>
