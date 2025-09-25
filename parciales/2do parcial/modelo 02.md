## Ejercicio 1
La Secretaría de Turismo de la ciudad de Resistencia habilitó el programa "EcoBici"
para promover el uso de la bici con fines turísticos. Se trata de 6 circuitos para
recorrer 14 barrios de la ciudad. Los paseos tienen un costo dependiendo de su duración:

- Paseos intensivos: superan las 6 hs. Tienen un costo fijo inicial de $1500 más un
costo variable dependiendo del circuito y cantidad de horas utilizadas.
- Paseos recreativos: duran 6 hs. o menos. Tienen un costo fijo inicial de $1000 más
un costo variable dependiendo del circuito y cantidad de horas utilizadas.

Los costos variables de los paseos se encuentran en un arreglo de dos dimensiones donde
cada posición corresponde al número de circuito y tipo de paseo, respectivamente. Se
cuenta con un archivo secuencial con la información de todas las bicicletas disponibles
en la ciudad:

**BICICLETAS:** *(ordenado por nro_serie y modelo)*
| Nro_serie | Modelo | Fecha_adquisición | Fecha_ult_mantenimiento | Disponibilidad |
|-----------|--------|-------------------|-------------------------|----------------|

Además se cuenta con información de todas las novedades para una bicicleta. Las mismas
pueden tratarse de movimientos de préstamos, o bien de una novedad respecto a un
mantenimiento realizado a la unidad.

**NOVEDADES:** *(ordenado por nro_serie, modelo, tipo_novedad y fecha_novedad)*
| Nro_serie | Modelo | Tipo_novedad | Fecha_novedad | Hora_inicio (00..23) | Hora_fin (00..23) | Circuito_nro | ID_usuario |
|-----------|--------|--------------|---------------|----------------------|-------------------|--------------|------------|

Tipo de novedad puede ser:
- 1 (Alta de una nueva unidad): cuando se da de alta, la fecha de último mantenimiento
debe estar vacía.
- 2 (Préstamo): no afecta los datos de las bicicletas, la secretaría lo utiliza con
fines estadísticos.
- 3 (Mantenimiento): implica que deberá actualizarse la fecha de último mantenimiento.
- 4 (Baja de una unidad).

Se pide:
1. Desarrollar un algoritmo que permita mantener actualizado el archivo de bicicletas,
considerando que pueden existir múltiples novedades para un mismo número de serie.
Considerar cualquier tipo de error informando por pantalla al usuario.
2. Indicar la cantidad total de préstamos realizados para un circuito particular que
ingresa el usuario, y el total recaudado.

## Ejercicio 2
La información de los usuarios que contratan el servicio se encuentra dentro de un
archivo indexado por id_usuario.

**USUARIOS:**
| id_usuario | DNI | Sexo ("M" o "F") | Apellido y Nombre | Domicilio | Localidad | Provincia | Edad |
|------------|-----|------------------|-------------------|-----------|-----------|-----------|------|

Considerando las estructuras de datos de entrada utilizadas en el ejercicio anterior
y la información suministrada en el archivo de Novedades, se solicita indicar:

1. Total de préstamos realizados por grupo etario y por tipo de paseo (intensivo o
recreativo), considerando los siguientes rangos de edades:
  a. Menores de 18 años.
  b. Entre 18 y 35 años.
  c. Entre 35 y 75 años.
  d. Mayores de 75 años.
2. Qué rango etario realizó más paseos recreativos.
3. Cuántos préstamos del tipo intensivo se realizaron a mayores de 75.

Considere además la existencia de una función *diff_horas*, que recibe como parámetro
una hora de inicio y una hora de fin (en formato de registros) y devuelve un entero
indicando la diferencia de horas entre ambos registros.
