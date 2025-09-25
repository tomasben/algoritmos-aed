## Ejercicio 1
Una empresa dedicada a la venta de pasajes de micros de larga distancia utiliza
el concepto de millas para determinar el precio y la capacidad que tiene un cliente
para realizar un viaje. Esta empresa no posee boleterías y las operaciones se realizan
directamente al abordar el Micro.

El chofer ejecuta el programa e ingresa el origen y el destino del viaje. Por cada
cliente ingresa su DNI y verifica la cantidad de millas del mismo y si son suficientes
para realizar el viaje, caso contrario se informa al cliente la cantidad necesaria de
millas a obtener para poder abordar. Siempre el chofer da la opción al cliente de realizar
cargas de millas adicionales, incluso si no las necesita inmediatamente. Las millas se
compran por un sistema electrónico externo y el chofer carga la cantidad de millas compradas
para que el cliente pueda viajar.

La empresa cuenta con 2 archivos indexados. Un archivo de Millas, donde se encuentra
la cantidad de millas por cliente.

**MILLAS** *Indexado por DNI*
| DNI N(8) | Millas N(10) | Ult_Carga Fecha |
|----------|--------------|-----------------|

Un archivo de destinos, donde se encuentra la distancia en millas entre todos los
destinos posibles de los micros, el origen y el destino se codifican en alfanuméricos
de 3 caracteres.

**DESTINOS** *Indexado por Origen y Destino*
| Origen N(1) | Destino N(1) | Millas N(10) | Duración N(2) |
|-------------|--------------|--------------|---------------|

Se pide realizar el algoritmo que le permita al chofer e:
1. Permitir la carga de millas a los clientes
2. Realizar el descuento de las millas del viaje correspondiente. En caso de que no
posea la cantidad de millas necesaria se informa al cliente y se continúa con el siguiente.
3. Determinar cuántos de los clientes que abordaron el micro cargaron por última vez el
corriente mes.

## Ejercicio 2
La empresa anterior cuenta además con un archivo secuencial de Viajes de 2018 con
todos los viajes realizados en ese año y la cantidad de millas compradas cada vez
que el cliente abordaba el micro. Tener en cuenta que existen 10 orígenes y destinos
distintos y los nombres de los mismos se encuentran en un arreglo de 10 posiciones.

**VIAJES**
| Fecha | Origen N(1) | Destino N(1) | Millas_Compradas N(10) |
|-------|-------------|--------------|------------------------|

Se pide realizar un algoritmo que permita determinar:
1. Cuatrimestre con menor cantidad de millas compradas
2. Origen para el cual los clientes compran la mayor cantidad de millas
3. Origen y trimestre en el que se registró menor cantidad de compras
