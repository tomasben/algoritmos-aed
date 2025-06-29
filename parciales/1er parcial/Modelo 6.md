## Ejercicio 1
El Centro Bioquímico Chaco cuenta con información de análisis realizados durante el día.
Esta información se encuentra almacenada en una secuencia de caracteres, la cual inicia
con el código de protocolo (5 caracteres, el primero siempre una letra), luego el nombre
y apellido del paciente (finaliza en una "," -coma-), cantidad de estudios realizados
(2 caracteres) y los códigos de cada uno (4 caracteres).

El código de cada estudio inicia con una vocal, que indica el tipo. Si es de tipo "A"
cuesta $300, si es de tipo "E" cuesta $420 y si es de tipo "I" cuesta $670. La secuencia
finaliza en "*".

**Formato de la secuencia:**
CódigoProtocoloNombreApellido,CantidadEstudiosRealizadosCódigosEstudios*

*Ejemplo de la secuencia:*
A2462Reina Isabel,03A123E345E333P2342Rey León,01E888*

Se pide:
1. Generar otra secuencia de salida, que almacene los estudios solicitados del tipo "E",
siempre y cuando el protocolo de ese paciente comience con la letra "A".
2. Informar el total recaudado por tipo de estudio.
3. Informar el porcentaje de estudios de tipo "A" en relación al total de estudios.

## Ejercicio 2
Una empresa de servicios agropecuarios con diversas sucursales en el país necesita un
programa que le permita operar con los diferentes servicios que tiene contratados. Para
ello almacena información en un archivo: se tiene la sucursal, el área al que corresponde
el servicio (0: administración de campo, 1: siembra y cosecha de soja, etc), una clave de
identificación del servicio, la descripción o nombre del servicio, la cantidad de clientes
que han contratado el servicio y el monto facturado por el servicio.

SERVICIO (ordenado por SUCURSAL, AREA e ID_SERV)

| SUCURSAL N(4) | ÁREA N(1) | ID_SERV N(6) | DESC AN(45) | CANT_CLI N(4) | MONTO N(6, 2) |
|---------------|-----------|--------------|-------------|---------------|---------------|

Se pide:
1. Informar el monto facturado por la venta de servicios contratados, teniendo en cuenta la
sucursal, el área de servicio y total general, siempre y cuando la cantidad de clientes sea par.
2. Generar un archivo de salida con sucursal y total facturado por el área 1 de la misma.

| SUCURSAL N(4) | TOTAL N(8, 2) |
|---------------|---------------|

3. Informar si el total facturado por la sucursal 50 representa más o menos del 20% del total
facturado por toda la empresa.
