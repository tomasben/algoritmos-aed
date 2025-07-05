## Ejercicio 1
Un programa de becas para estudiantes de Ingeniería desea obtener la lista de postulantes
que están en condiciones de acceder a la ayuda económica.
Para ello se posee una secuencia de caracteres con los datos de los postulantes que ya han
aprobado la etapa de análisis de datos previo, y pueden ser evaluados respecto a sus
condiciones económicas. La secuencia, SEC1, posee la siguiente información:

Apellido y Nombre (separados por un espacio en blanco entre sí), Sexo (M o F),
DNI (8 caracteres), Correo Electrónico, Universidad y Carrera.

Todos los datos de un mismo postulante se separan por “|”, y a la vez cada postulante se
separa del otro por un “$”.

*Por ejemplo:*
Perez Juan|M|37878923|jp@gmail.com|UTN|ISI$Romero Maria|F|37234124|mr@gmail.com|UTN|IQ$*

Además se cuenta con una secuencia de números que posee el ingreso familiar.
Por ejemplo, teniendo en cuenta el ejemplo anterior de postulantes: 8000	6000

Ambas secuencias poseen la misma cantidad de datos, es decir al primer postulante de la
primera secuencia le corresponde el primer ingreso familiar de la segunda secuencia y así
sucesivamente.

Se desea una secuencia de salida de los postulantes que no superen los $10000 de ingreso familiar
con el siguiente formato:

Apellido y Nombre (separados por un espacio en blanco entre sí), CUIT y Correo Electrónico.
Todos los datos de un mismo postulante se separan por “|”, y a la vez cada postulante se separa
del otro por un “$”.

Para calcular el CUIT se debe seguir el siguiente procedimiento:
1. Agregar los primeros dos dígitos en función del sexo (27 si es femenino, 20 si es masculino).
2. Agregar un guion medio y seguido el DNI original.
3. Seguido a lo último agregar un guion medio y el código verificador del que se obtiene de la
siguiente forma:
  - Si el primer y último digito del DNI son pares entonces el código es 1.
  - Si en el DNI, el primer digito es impar y el último es par entonces el código es 2.
  - Si en el DNI, el primer digito es par y el último es impar entonces el código es 3.
  - Si el primer y último digito del DNI son impares entonces el código es 4.

La salida quedaría (teniendo en cuenta los ejemplos anteriores) de la siguiente forma:
Perez Juan|20-37878923-4|jp@gmail.com|$Romero Maria|27-37234124-2|mr@gmail.com|$*

Además se pide porcentaje de postulantes que cumplieron la condición económica y porcentaje de
postulantes que no la pudieron cumplir sobre el total.

## Ejercicio 2
Dado un Archivo que contiene información de los estudiantes a los que se asignaron becas durante
el 2014, cuyos registros tienen el siguiente formato:

ESTUD (Ordenado por Provincia, Universidad, Carrera, CUIT)

| PROVINCIA AN(10) | UNIVERSIDAD AN(20) | CARRERA AN(30) | CUIT N(11) | APE_NOM AN(60) | MONTO N(10, 2) |
|------------------|--------------------|----------------|------------|----------------|----------------|

Se desea obtener el total de estudiantes beneficiarios cuyo monto de beca no supere los $800, informados
por Universidad, Provincia y total general.
