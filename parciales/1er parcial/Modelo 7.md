## Ejercicio 1
El régimen de jubilaciones para docentes universitarios establece que, según las leyes
vigentes, podrán acceder al beneficio jubilatorio quienes cumplan determinados requisitos:

- Edad: entre 65 y 70 años para los hombres, entre 60 y 70 para las mujeres.
- Aportes: mínimo 30 años de aportes.

La Facultad Regional Resistencia cuenta con dos secuencias, una de caracteres y otra de
enteros, con las siguientes características:

**Formato de la secuencia Docentes (de caracteres):**
RegionalSexoLegajoNombreCompleto#SexoLegajoNombreCompleto+RegionalSexoLegajoNombreCompleto#SexoLegajoNombreCompleto+FDS

Donde:
- Regional: tres caracteres que indican la facultad regional.
- Sexo: un carácter, que puede ser "M" o "F".
- Legajo: cinco caracteres que indican el legajo.
- NombreCompleto: cantidad indefinida de caracteres que indica el nombre, que finaliza con
el signo "#".

Consideraciones de la secuencia Docentes:
- Los docentes de una misma regional terminan con el signo "+".
- La regional siempre es FR seguido de un carácter, que es la inicial de la provincia.

*Ejemplo de la secuencia Docentes:*
FRMM22711Pedro González#F19245Mónica Martínez+...#...+...#...+FDS

**Formato de la secuencia Edad (de enteros):**
EdadAportes

Donde:
- Edad: dos dígitos que indican la edad.
- Aportes: dos dígitos que indican los años de aportes.

Consideraciones de la secuencia Edad:
- Existe una correspondencia uno a uno entre cada subsecuencia de Docentes y cada par
Edad-Aportes de la secuencia Edad.

*Ejemplo de la secuencia Edad:*
67205030...FDS

Para el primer par de valores, la persona tiene 67 años y 20 años de aportes.

Se pide:
1. Generar una secuencia de caracteres llamada Jubilar, solo para docentes de una región
específica ingresada por el usuario, que debe contener el legajo y nombre completo de los
docentes en condiciones de jubilarse.
2. Informar por regional la cantidad de docentes que pueden jubilarse y la cantidad de
docentes que no pueden.
