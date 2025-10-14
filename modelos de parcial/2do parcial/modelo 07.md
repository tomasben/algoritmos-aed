## Ejercicio 1
La biblioteca de un colegio necesita un programa para que los bibliotecarios registren
los préstamos de los libros. Para esto cuentan con 3 archivos: SOCIOS, LIBROS, y cada
transacción se registra en un archivo de PRÉSTAMOS.

**SOCIOS** *Indexado por DNI*
| DNI N(8) | Ape_Nom AN(30) | Edad (18..80) | Ciudad AN(30) | Deudor (Si-No) | Cantidad_de_Prestamos |
|----------|----------------|---------------|---------------|----------------|-----------------------|

**LIBROS** *Indexado por ID*
| ID (1..100) | Título AN(30) | Genero N(2) | Disponible (booleano) |
|-------------|---------------|-------------|-----------------------|

**PRÉSTAMOS** *Indexado por ID_prestamo*
| ID_prestamo N(8) | DNI_socio N(8) | ID_libro N(8) | Fecha_prestamo | Fecha_devolucion | Devolución (Si-No) |
|------------------|----------------|---------------|----------------|------------------|--------------------|

El archivo de préstamos está vacío por lo que arrancamos en id=1 y se incrementa.

Se pide realizar un algoritmo que permita :
1. La carga interactiva que hace el bibliotecario de nuevos préstamos al archivo
PRÉSTAMOS, donde el usuario brinda el dni del socio y TÍTULO DEL LIBRO. Actualizar
el campo de disponible en el archivo LIBROS e incrementar la cantidad de préstamos
en el archivo SOCIOS. (Para obtener el ID del libro necesario para el acceso indexado,
se cuenta con un arreglo arr_libros con dicha información.)
- Si el socio no existe, darlo de alta, completar los datos necesarios (pedirlos al
usuario) y completar el préstamo.
- Si el Libro no existe o no está disponible, informar y no se completa el préstamo.
- La fecha de devolución es 14 días después de la del préstamo. Pero si el cliente
realizó más de 10 préstamos y su condición de deudor es NO, se le da 20 días. La
fecha actual la pueden obtener de la función “fecha_sistema()” (no es necesario
definirla) y además a la misma se le puede sumar directamente un entero.
2. Además calcular:
- Total de préstamos realizados
- Total de socios dados de alta

**ARR_LIBROS:** es un arreglo de 100 libros, donde el contenido es el título y la posición
dentro del arreglo corresponde al ID.

## Ejercicio 2
Una biblioteca cuenta con 5 sucursales y requiere de usted algunos informes, para
eso cuenta con un archivo de EJEMPLARES, donde indican información de sus ejemplares
por libro, y además si el mismo se encuentra en forma física o digital (claramente
puede haber más de un ejemplar por cada libro).

**EJEMPLARES** *Ordenado por ID_ejemplar, ID_libro*
| ID_ejemplar N(8) | ID_Libro (30) | Sucursal (1-5) | Digital (SI-NO) | Disponible (booleano) |
|------------------|---------------|----------------|-----------------|-----------------------|

Se pide:
1. Informar por sucursal y discriminando si es digital o no:
  a) Cantidad total de ejemplares disponibles
  b) Cantidad total de ejemplares no disponibles
2. Informar de qué sucursal se tiene mayor cantidad de ejemplares disponibles.
3. Informar el total de libros digitales y el total de físicos.
4. ¿Cuántos ejemplares hay en la sucursal 2? Independientemente de que estén o no
disponibles.
