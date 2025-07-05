## Ejercicio 1
1- Una cadena de restaurantes de la ciudad de Resistencia necesita realizar un
informe con todos los comentarios que realizaron los clientes, para ello cuenta
con dos secuencias de caracteres con el siguiente formato:

**Secuencia Comentarios:**
Contiene los comentarios realizados, cada comentario finaliza con el carácter #,
están agrupados por restaurante, el fin de cada grupo se indica con el carácter @
y el fin de la secuencia con una marca *. Posee la siguiente información: puntuación
(del 01 al 10), la fecha en que se realizó el comentario (en formato AAAAMMDD), si
fue una cena o un almuerzo (C o A), la cantidad de personas que asistieron (2 dígitos),
luego de estos datos posee un comentario (palabras y espacios) con un máximo de 999 caracteres.

**Secuencia Restaurantes:**
Es una secuencia de caracteres, que contiene el nombre y la dirección (palabras y espacios)
separados por una coma. Cada restaurante termina con un . y la secuencia termina con un .

Se pide generar una secuencia de salida de caracteres que posea todos los comentarios donde
la puntuación sea menor o igual a 4, con el siguiente formato:

para cada restaurante se copia el nombre una sola vez y luego todos los comentarios que le
pertenecen, de la siguiente manera:

...nombre del restaurante - puntuación(01, 02, 03 o 04), fecha en que se realizó el comentario
(formato AAAAMMDD), comentario que finaliza con el carácter #, y al finalizar mostrar la cantidad
de palabras del comentario (3 caracteres)....otro comentario...otro comentario...@

Se pide al final:
1. Informar cantidad de comentarios con puntuación perfecta (10 a 8), buena (7 a 5) o mala (de 4 a 1).
2. Cantidad promedio de personas por restaurante.

## Ejercicio 2
Un supermercado se encuentra ante la lamentable situación de aumentar el precio a sus productos.
Para realizar esta acción posee el siguiente archivo secuencial, ordenado por tipo y calidad:

| tipo | calidad | código_producto | nombre AN(150) | precio_unitario | stock_actual |
|------|---------|-----------------|----------------|-----------------|--------------|

El campo tipo se codificó del 1 al 10 y la calidad del producto se codificó del 1 al 5.

Se pide generar un archivo de salida con el siguiente formato:

| código_producto | nombre AN(150) | precio_viejo | precio_nuevo | Porcentaje_de_aumento |
|-----------------|----------------|--------------|--------------|-----------------------|

El aumento que se debe tener en cuenta en cada producto está dado por los campos tipo y calidad
según los siguientes criterios:
- Para el caso de que el stock_actual sea 0, el producto no debe aparecer en el archivo de salida.
- Si el tipo es del 1 al 5: se debe aumentar un 50 % el precio.
- Si el tipo es del 6 al 10: se debe tener en cuenta la calidad, en caso de ser 1 o 2, se aumentará
un 30% el valor del producto. Para los otros casos (calidad 3, 4 o 5) el aumento es del 40%.

Se solicita además: Mostrar por pantalla, para cada tipo y calidad y total general, cuantos productos
existen.
