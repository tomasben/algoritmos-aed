## Ejercicio 1
Consigna: la Secretaría de Turismo de la ciudad de Resistencia habilitó el programa "EcoBici"
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
