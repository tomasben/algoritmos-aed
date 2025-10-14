## Ejercicio 1
La empresa NIANTIC decidió contratarlo a usted para confeccionar una
solución algorítmica que satisfaga ciertos requerimientos referidos a su reciente
juego, Pokemon GO. Se poseen los siguientes archivos:

**CAPTURAS:** *(ordenado por cod_región, cod_usuario y cod_pokemon)*
| cod_region N(4) | cod_usuario N(10) | cod_pokemon (1..151) | puntos_experiencia N(5) | fecha_captura AAAA/MM/DD | estado_pok | estado_us |
|-----------------|-------------------|----------------------|-------------------------|--------------------------|------------|-----------|

Donde:
estado_pok puede tomar tres valores:
- E: entrenándose
- I: incubándose
- D: descansando

estado_us puede tomar tres valores:
- A: activo
- S: suspendido
- D: descansando

**USUARIOS:** *(ordenado por cod_región y cod_usuario)*
| cod_region N(4) | cod_usuario N(10) | correo AN(50) | experiencia N(7) |
|-----------------|-------------------|---------------|------------------|

Se posee además un arreglo de 151 posiciones con los nombres de los pokemon, con
el siguiente formato: ("Squirtle", "Pikachu", ..., "Mewtwo").

Se desea implementar una solución algorítmica que permita:
1. Actualizar (incrementar) la experiencia del usuario, sumando los puntos de experiencia
de cada pokemon capturado. En caso de que su estado sea "E", se duplican los puntos a sumar.
2. En caso de que el usuario no exista en el archivo de usuarios y su estado en el
archivo de capturas sea "A", debe agregarlo y aplicar lo indicado en el primer punto.
Además, el campo "correo" debe quedar en blanco.
3. Si el usuario existe y su estado en el archivo de capturas es "S", se lo debe dar
de baja (física).
4. Indicar el nombre del pokemon en estado "D" que lo tengan la mayor cantidad de usuarios,
así como la cantidad de usuarios que lo poseen.

## Ejercicio 2
En la preparación del Congreso Nacional de Estudiantes de ISI, se desea obtener
un informe de la cantidad de papers (trabajos de investigación científicos) enviados
por cada regional (31 en total) de la UTN, discriminado según categoría (16 en total).
Para ello, se cuenta con un archivo de entrada secuencial con los datos de los papers:

| DNI | ApellidoyNombre | E_mail | Regional | Categoría | Título_trabajo |
|-----|-----------------|--------|----------|-----------|----------------|

Se cuenta además con dos arreglos que almacenan los nombres tanto de las regionales
como de las categorías:

**Arreglo de regionales (31):**
| "Avellaneda" | ... | "Resistencia" | "Rosario" |
|--------------|-----|---------------|-----------|

**Arreglo de categorías (16):**
| "Seguridad informática" | "Desarrollo de SW" | ... | "Redes y telecomunicaciones" |
|-------------------------|--------------------|-----|------------------------------|

Escribir un algoritmo que cumpla con las siguientes consignas:
1. Calcule y muestre por pantalla los totales de papers por regional y por categoría.
2. Informe el nombre de la regional con más papers enviados. En caso de que haya más
de una, mostrar el nombre de todas.
