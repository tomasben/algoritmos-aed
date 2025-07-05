## Ejercicio 1
Se lanzó la preventa del Primavera Sound 2023, la modalidad que se elige es lanzar
una preventa de entradas, sin anunciar los artistas que se presentarán. Los early birds #1
(preventa de entradas), se lanzarán el 1 de mayo de 2023 a las 13:00 hs, pero los fanáticos
pueden hacer “fila virtual” desde las 00:00 para asegurar su lugar en el famoso festival, una
vez que se lance la venta virtual los usuarios pueden ir comprando las entradas de a tandas.

Con la finalidad de analizar si se debe optimizar el rendimiento de la plataforma, se disponen
dos secuencias de caracteres. La primera secuencia contiene a los fanáticos que hacen la
“fila virtual”, esta secuencia contiene la hora en la que se registró en la fila (hhmm), el número
en la fila (6 caracteres), el medio de pago con el que piensa pagar (“T”- tarjeta, “C”-efectivo,
“E”-transferencia) y cuántas entradas piensa comprar (como máximo puede comprar 5 entradas).

**Formato de la secuencia Fila_Virtual:**
horafilanumerofilamediopagocantentradas#

*Ejemplo de la secuencia Fila_Virtual:*
0301123456T3#0345234567E4#

En estos sistemas de fila, al colocarse en ella se obtiene un identificador o número de fila,
pero recién el usuario inicia sesión al llegar a su lugar en la fila y entrar a la sección de Compras.

En una segunda secuencia se encuentran las compras reales realizadas, esta secuencia contiene el número
en la fila (6 caracteres), el nombre de usuario (cantidad indefinida, termina en “+”) y luego contiene
los datos de para quién es cada entrada en la compra, incluyendo su DNI y nombre (separados con ‘.’).
Una compra finaliza con un “?”.

**Formato de la secuencia Compras:**
numerofilanombre_usuario+dninombre.dninombre.dninombre?

*Ejemplo de la secuencia Compras:*
123456unsuario+33254787Juan.27895614Melisa.36257489Pedro?

Si por algún motivo algún fanático deja su lugar en la fila, en la secuencia de Compras en nombre de
usuario aparece un carácter “#”, el signo “+” y luego la marca “?”. Esto implica una correspondencia
1 a 1 entre las dos secuencias.

Se pide:
1. Generar una secuencia de salida con los nombres de usuario y cada DNI de las entradas compradas que
fueron pagadas con tarjeta. Separar cada campo con un + y finalizar con “#” al completar la compra de
un usuario. EJ: nombreusuario+dni+dni#nombreusuario+dni+dni#
2. Se desea conocer cuántos usuarios compraron una cantidad de entradas distinta a la que declararon
en la fila virtual.

## Ejercicio 2
Basados en el escenario del ejercicio 1, se tiene un archivo secuencial que contiene las informaciones
de ventas finales de entradas para el festival, realizadas desde el 1 de mayo del 2023 hasta el 1 de
julio de 2023.

VENTAS: ordenado por provincia, ciudad, plataforma y fecha.

| Provincia | Ciudad | Plataforma | Fecha | Entradas |
|-----------|--------|------------|-------|----------|

Se pide:
1. Generar un archivo de salida que contenga datos de las ciudades en las cuales la cantidad total de
entradas vendidas supera las 1000 con el siguiente formato:

| Provincia | Ciudad | Entradas |
|-----------|--------|----------|

2. Informar el total de ventas del 1 de junio al 1 julio, discriminado por plataforma y ciudad.
