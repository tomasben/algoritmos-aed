[filmina teórica 1](https://docs.google.com/presentation/d/1FlhGIvC8bVVELO1vune0LqpluJsugZPYCM5Ejx6DzME/edit?slide=id.g1f3c798447e_0_0#slide=id.g1f3c798447e_0_0)

# INTRODUCCIÓN

**¿Qué es un algoritmo?**

Es una secuencia finita de instrucciones o reglas que describen de modo preciso las operaciones que una computadora debe realizar para ejecutar una tarea en un tiempo determinado.

Pasos para desarrollar un algoritmo:
1. entender el problema y la necesidad de solución es imprescindible para poder avanzar
2. definir los datos de entrada con los que vas a trabajar para lograr el resultado
3. plantear los procesos necesarios para pasar los datos de entrada a datos de salida transformados
4. validar el algoritmo

**Pseudocódigo**

Estructura general:

```
Accion [nombre] es
	Ambiente
		var1 : [tipo de dato]
		... denominación y/o asignación de constantes a utilizar
		Subacción [nombre](parámetros):
		FinSubacción
	Algoritmo
		... instrucciones
FinAcción
```

# OPERADORES

| concepto        | sintaxis       | tipo       |
| --------------- | -------------- | ---------- |
| igualdad        | A = B          | relacional |
| desigualdad     | A >< B         | relacional |
| menor a         | A < B          | relacional |
| menor o igual a | A <= B         | relacional |
| mayor a         | A > B          | relacional |
| mayor o igual a | A >= B         | relacional |
| o               | A o B          | lógico     |
| y               | A y B          | lógico     |
| negación        | No(A) \| No(B) | lógico     |

# ESTRUCTURAS DE CONTROL

# SUBACCIONES
Las subacciones son acciones menores que forman parte de una acción principal, son módulos que están escritos para ejecutar tareas específicas. Se definen en el ambiente para ser utilizadas en el proceso del algoritmo, y se definen 1 sola vez para poder ser referenciadas varias veces en el algoritmo y así reducir la duplicación de código.

**Control de ejecución:** El algoritmo principal se ejecuta en primera instancia y da el orden de inicio de ejecución de las subacciones un número _n_ de veces. Cuando se realiza la solicitud o llamado de la subacción, el algoritmo se detiene hasta que la subacción finalice su tarea.

## Elementos de las subacciones
1. Nombre: nombre único que define a las subacciones y es utilizado para llamarlas. Debe ser representativo del subalgoritmo y no puede ser una palabra reservada
2. Parámetros: conjunto de datos que se pasan a la subacción para que esta pueda ejecutarse hacer uso de ellas. Los parámetros puede ser de tipo formales/ficticios o actuales/argumentos, donde los primeros van en la definición de la subacción y definen el tipo de dato que se ingresará y donde se utilizará en el proceso del mismo y el segundo, las variables, constantes o expresiones que se pasan a la función para su ejecución. Cuando se ejecuta una subacción, se establece una correspondencia entre los parámetros formales y los actuales, verificando que la cantidad de datos pasados y el tipo sean los esperados de acuerdo a su definición en el ambiente.

# Las funciones como subacciones
Una función es un subalgoritmo que recibe como **parámetros actuales** datos numéricos o no, y que devuelve un único resultado. Las funciones pueden ser internas, ya definidas en el sistema, o pueden ser externas y definidas por el usuario.

## Estructura de las funciones en pseudocódigo
```
Función nombrefun(lista de parámetros): Tipo
..
...(declaración de variables locales si fuera necesario > Ambiente)
..
...(acciones de la función)
..
nombrefun := <valor de la función>
Fin Función
```

- nombrefun: el nombre de la Función
- lista de parámetros: lista de parámetros formales que **no puede ser vacía**
- tipo: es el tipo de dato que devolverá la función

Ejemplo
```
FUNCION ES_PRIMO(A: entero): lógico
  AMBIENTE
    i: entero
  PROCESO
    ES_PRIMO := V <- habilito la función como bandera
    PARA i:=2 hasta (A-1) HACER
      SI A mod i = 0 ENTONCES
        ES_PRIMO := F <- ya no es primo
      FIN_SI
    FIN_PARA
FIN_FUNCION
```
# PROCEDIMIENTOS
Un procedimiento también es una subacción diseñada con un fin específico, pero que a diferencia de las funciones no devuelve ningún valor, solo ejecuta acciones. Un ejemplo de procedimiento puede ser una subacción que reciba el input de un usuario, su contraseña y el valor para su validación, la cuál evaluaria si la contraseña y el usuario son correctos para autorizar al usuario, pero no devolvería ningún valor.

**¿Por qué usar proceedimientos?**
- facilitar el diseño top-down de las soluciones
- se pueden ejecutar varias veces a lo largo de un algoritmo con tan solo definirlos en el ambiente
- su uso facilita la división de tareas de un problema complejo

# ÁMBITOS DE VARIABLES
Nos referiremos al ámbito de variables como al conjunto de partes de un algoritmo en que una variable es conocida. Las variables pueden ser *locales*, las cuales son definidas en el ambiente de un algoritmo y solo son conocidas por esa función o procedimiento en que fueron definidas, y estas desaparecen al terminarse la ejecución de su subacción. Por otro lado, están las variables *globales*, que son aquellas definidas en el algoritmo principal y que pueden ser leidas dentro de cualquier subacción en él

# PASO DE PARÁMETROS
El paso de parámetros es el proceso por el cuál se envía variables a otra función o procedimiento de forma que esta pueda utilizarlos, esto puede hacerse *por valor* o *por referencia*. Cuando surge la necesidad de obtener el valor de una variable desde el algoritmo principal hacia una subacción se utiliza el paso de parámetros por valor, el cual produce una copia de la variable enviada desde el algoritmo. La distinción principal de esta es que si usamos el paso por valor, nunca podremos producir redefinir la variable original que fue copiada, y el espacio de memoria donde esta alojada esta copia se liberará cuando termine la ejecución del subalgoritmo.
