## Ejercicio 1
Luego de la consagración de nuestra selección en el Mundial de Fútbol, la famosa
marca de ropa que viste a la Selección Argentina ha decidido realizar la preventa,
desde su página web, de sus nuevos lanzamientos con las tres estrellas, y ha ofrecido
importantes descuentos para la indumentaria preexistente.

La información de los productos se encuentra en un archivo secuencial ordenado por
id_producto, donde cada registro contiene los siguientes campos:

| id_producto | nombre | descripción | categoría | nuevo_lanzamiento ("SI", "NO") | porcentaje_descuento | stock |
|-------------|--------|-------------|-----------|--------------------------------|----------------------|-------|

Donde la categoría puede ser:
- C (camisetas)
- R (remeras)
- G (gorras)
- S (shorts)

porcentaje_descuento es un valor numérico entre 0 y 1, con decimales.

La información de las preventas se encuentra en un archivo secuencial que
contiene los siguientes datos, y está ordenado por id_producto e id_cliente:

| id_producto | id_cliente | cantidad | es_personalizado | nro_jugador (1..26) | nombre_jugador | talle |
|-------------|------------|----------|------------------|---------------------|----------------|-------|

Se pide:
1. Actualizar el stock del archivo de productos considerando que si algún producto
queda con stock cero, no deberá figurar en el archivo actualizado.
2. Emitir un mensaje de error por cada pedido que no haya podido concretarse por
falta de stock.
3. Informar el nombre del jugador que vendió más camisetas. Los nombres de los
jugadores se encuentran en un arreglo, donde cada posición corresponde al número
de camiseta.
4. Cantidad de productos que no se han podido procesar por falta de stock. Para
calcular tener en cuenta el siguiente criterio: si cantidad (preventa) supera la
cantidad en stock, se contabiliza el faltante. Si el producto no existe, se
contabiliza el total de la cantidad pedida.
5. Nombre de la categoría menos solicitada.
6. Informar el importe total vendido en la preventa lanzada, teniendo en cuenta
los descuentos.

## Ejercicio 2
En la empresa de venta de electrodomésticos "La Cafetera está que Hierve" se implementaron
5 promociones por el verano, y ahora nos solicitan desarrollar un algoritmo para obtener
información sobre las mismas implementadas en cada sucursal.

Para ello, cuentan con información almacenada en un archivo, cuyo registro cuenta
con:

| CodSuc (1..10) | CodPromocion (0..5) | CodProd AN(7) | Cantidad N(4) |
|----------------|---------------------|---------------|---------------|

Si el CodPromocion es igual a cero, significa que en esa venta no se aplicó ninguna promoción.
Existe además una función externa, ya desarrollada, llamada getImporte, a la cual pasándole
el código del producto, nos devuelve el importe del mismo.

Se pide:
1. Importe promedio por venta de cada sucursal (solo venta con promociones).
2. La promoción que mayor importe recaudó.
3. Para cada promoción, indicar en qué sucursal obtuvo el mejor resultado (es decir, el mayor
monto de ventas).
