## Ejercicio 1
Santa Claus y su equipo de duendes registran toda la información de los niños que
esperan regalos durante la Navidad.

Cada niño está registrado en un archivo secuencial llamado NIÑOS, donde se guarda
información sobre su comportamiento y su deseo principal.

Al final de la temporada previa a Navidad, los duendes recopilan los eventos ocurridos
durante el mes en un archivo secuencial llamado EVENTOS, que detalla las novedades,
incluyendo cambios de comportamiento, solicitudes de regalos, y demás actualizaciones.

**NIÑOS** *ordenado por id_pais, id_niño*
| **id_pais** | **id_niño** | nombre y apellido | puntaje_buen_comportamiento | id_regalo | nombre_regalo | fecha_registro | fecha_retiro |
|-------------|-------------|-------------------|-----------------------------|-----------|---------------|----------------|--------------|

- id_pais: Identificador del País del niño.
- id_niño: Identificador único del niño.
- puntaje_buen_comportamiento: Puntaje que indica el comportamiento del niño (puede ser positivo o negativo).
- regalo_deseado: Nombre del regalo que desea recibir.
- fecha_registro: Fecha en la que se registró al niño.
- fecha_retiro: Fecha en la que fue retirado de la lista de navidad (si corresponde).

**EVENTOS** *ordenado por id_pais, id_niño, cod_evento*
| **id_pais** | **id_niño** | **cod_evento** (0..99) | fecha_evento | detalle | puntaje_cambio | tipo | id_regalo_deseado | regalo_deseado |
|-------------|-------------|------------------------|--------------|---------|----------------|------|-------------------|----------------|

- cod_evento: 0: Alta de un nuevo niño; 99: Retiro de un niño de la lista; 1-98:
Actualización de puntaje de comportamiento o cambio de regalo deseado.
- detalle: Descripción del evento (por ejemplo, "Ayudó a su hermano", "Se peleó
en la escuela", etc.).
- puntaje_cambio: Valor que se sumará o restará al puntaje de comportamiento del niño.
- tipo: "A" si el evento mejora el puntaje (positivo), "R" si lo reduce (negativo),
vacío si es un cambio de regalo.
- regalo_deseado: Nuevo regalo deseado (si corresponde a un cambio).

Se pide:
- Desarrollar un algoritmo que permita mantener actualizado el archivo NIÑOS con
los eventos registrados en el archivo EVENTOS.
- El algoritmo debe ajustar los puntajes de comportamiento y actualizar los regalos deseados si corresponde.
- Informar por pantalla cualquier tipo de error que considere pertinente durante el proceso.

Además indicar:
1. La cantidad total de niños nuevos que se registraron durante el proceso.
2. El nombre del niño con mejor puntaje de buen comportamiento.
