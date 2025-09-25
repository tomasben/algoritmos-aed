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
  de días y una fecha, y devuelve verdadero o falso si la fecha actual supera en días a
  la fecha que recibe como parámetro.
2. En caso de coincidencias, se deberá verificar si la figurita permite duplicados. En
caso de permitirlo, se deberá incrementar la cantidad disponible en el archivo ÁLBUM.
3. Pueden existir múltiples solicitudes de intercambios con el mismo cod_figurita.

Al finalizar, indicar la cantidad de figuritas duplicadas que se admitieron en
el álbum.

## Ejercicio 2
Teniendo en cuenta que la información de los álbumes de todos los usuarios se encuentra
en el archivo ÁLBUM, y que se tiene además el archivo AMIGOS descripto más abajo:

**ÁLBUM:** (ordenado por cod_usuario)*
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
