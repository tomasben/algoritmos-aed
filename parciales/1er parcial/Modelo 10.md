## Ejercicio 1
**cortado** ...surge, a pedido de la Coordinación General, la necesidad de conocer determinada
información de los estudiantes que residen en el Complejo. Para ello se cuenta
con una secuencia con información de Residentes, y presenta el siguiente formato:

La secuencia contiene el Nro. de Torre seguido por un -, luego se almacenan los
nombres de los Residentes junto al código de ciudad de origen (2 caracteres),
información separada por espacio en blanco. La información de cada residente se
separa de otro mediante una coma. La información de cada Torre finaliza con el

Por ejemplo:
1-Amelia R1,Patricio M1,Juan C1,Humberto C1,2-Jonny R1,Thiago R1,Luana R1,%

Se solicita:
1. Generar dos secuencias de salida:
  - En una incluir los residentes de la Torre 1 y de la Torre 2 separados por coma.
  - En la otra almacenar los residentes de la ciudad de Misiones, código M1.
3. Informar qué porcentaje representan los residentes de la torre 2, sobre el total
de residentes del Complejo.

## Ejercicio 2
El Ministerio de Salud Pública de la Nación posee información almacenada en un archivo
secuencial producto de relevamiento realizado en Hospitales Públicos respecto a cantidad
de pacientes vacunados contra el contagio del virus del papiloma humano.

Los datos se almacenan en registros con el siguiente formato:
VACUNACIONES (ordenado por COD_CIU, COD_HOSP Y FCH_ANALISIS)

| COD_CIU AN(4) | COD_HOSP AN(4) | FCH_VACUNACION Fecha | CANTIDAD N(4) | DOSIS_COMPLETA N(4) |
|---------------|----------------|----------------------|---------------|---------------------|

Elaborar un algoritmo que permita:
a. Se desea un informe con el formato que se muestra a continuación, teniendo en cuenta datos del primer semestre del año actual:
CIUDAD HOSPITAL FECHA DE VACUNACION CANTIDAD PACIENTES VACUNADOS
b. Mostrar por pantalla el Hospital con mayor cantidad de pacientes que hayan completado la dosis.
