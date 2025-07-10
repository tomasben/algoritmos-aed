## Ejercicio 1
Una Empresa que distribuye productos farmacéuticos dispone de una secuencia de
caracteres con la siguiente información sobre sus productos:

- Venta libre o con receta: VL - RE (2 caracteres)
- Línea terapéutica: A(antiinflamatorio) – G(gastroenterológica) – R(respiratoria/antialérgica)(1 carácter)
- Nombre del producto: cantidad no conocida de caracteres, finaliza con el carácter #

Se ubican agrupados por Laboratorios, al inicio de cada grupo está el nombre del laboratorio
y luego un guión, y el fin de cada grupo se indica @.

*Ejemplo:*
PharmaS.A.-VLAibuflash#REAcalmidol#REGlanzopral#VLRalerpriv#...#...#@Tecnoquimica-VLGsertal#VLAibuprofeno#...#...#@Bago-...#...#@FDS

La empresa solicita:
1. Generar dos secuencias de salida a fin de disponer, por separado, los datos de
los productos que son de “venta libre” y los que son de venta “con receta”; los datos
que le interesa tener son: línea terapéutica y nombre del producto, indicando el fin
de cada producto con el carácter #.

*Ejemplo:* Aibuflash#Ralerpriv#Gsertal#Aibuprofeno#...#...#...#FDS

2. Se pide además un listado (por pantalla) de cantidad de productos de venta “con receta”
de la línea “gastroenterológica”, por Laboratorio. Por ejemplo:

**Laboratorio**		**Cantidad**
PharmaS.A		      50
Tecnoquimica		  87
Bago		          23

## Ejercicio 2
a misma Empresa del ejercicio 1 dispone de un archivo secuencial con la siguiente
información de su stock de productos, ordenado por laboratorio, código de producto
y lote.

| Laboratorio N(3) | Código Producto N(4) | Lote AN(5) | Descripción AN(150) | Cantidad N(4) | Fecha_vencimiento (dd-mm-aaaa) |
|------------------|----------------------|------------|---------------------|---------------|--------------------------------|

Hay varios registros para cada código de producto, con distintos números de lote,
el cual es único. La Empresa necesita:
1. Generar otro archivo de salida que contenga los lotes vencidos (cuya fecha de
vencimiento sea posterior a la actual), con el siguiente formato:

| Laboratorio N(3) | Código Producto N(4) |	Lote AN(5) | Cantidad N(4) | Fecha_vencimiento (aaaa-mm-dd) |
|------------------|----------------------|------------|---------------|--------------------------------|

2. Mostrar por pantalla la cantidad total de productos vencidos por Laboratorio,
Código de Producto y total General.
3. Al final informar cuál fue el laboratorio con mayor cantidad de productos vencidos
