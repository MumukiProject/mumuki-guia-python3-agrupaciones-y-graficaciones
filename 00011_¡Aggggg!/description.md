No, ¡nos estamos quejando! 🤬 Sólo queríamos mostrarte otra operación útil a la hora de hacer agregaciones: `agg` 😅. 

```python
cines.groupby("province", as_index=False).agg({
   "screens": "sum",
   "seats": "mean"
})
```
 
A diferencia de las agregaciones anteriores, como `sum` y `max`, `agg` nos permite realizar varias al mismo tiempo y obtener tablas con múltiples resultados: 

||province|screens|seats|
|---|---|---|---|
|0|Buenos Aires|358|878.415094|
|1|Catamarca|12|800.000000|
|2|Chaco|14|617.250000|
|3|Chubut|10|298.000000|
|4|Ciudad Autónoma de Buenos Aires|153|896.742857|
|5|Corrientes|17|421.250000|
|6|Córdoba|105|594.257143|
|(...)|

Con `agg` se vuelve sencillo adicionar agregaciones a nuestras tablas, tan sólo agregando una clave (la columna a agregar) y un valor (la operación a realizar) al diccionario que recibe por parámetro. Por ejemplo, así podemos incluir también la cantidad de cines en la tabla anterior: 

```python
cines.groupby("province", as_index=False).agg({
   "name": "count",
   "screens": "sum",
   "seats": "mean"
})
# si te molesta que la columna se llame nombre, ya lo veremos más adelante...
```
 
¡Pero eso no es todo! `agg` permite además usar agregaciones personalizadas, tan solo pasando una función como valor. Por ejemplo, si queremos contar la cantidad de cines que tiene la frase `"Centro cultural"` en su nombre...

||province|name|
|---|---|---|
|0|Buenos Aires|5|
|1|Catamarca|1|
|2|Chaco|0|
|3|Chubut|1|
|4|Ciudad Autónoma de Buenos Aires|3|
|5|Corrientes|0|
|6|Córdoba|2|
|(...)|

 ...podríamos escribir algo así....
 
```python
cines.groupby("province", as_index=False).agg({
   "name": contar_centros_culturales
})
```
 
... donde en lugar de pasar un string con el nombre de una agregación (como `"sum"` o `"count"`), pasamos la referencia a una función. Estas funciones que `agg` recibe deben tomar una lista con los valores de las filas de cada grupo: 

```python
def contar_centros_culturales(nombres):
 return len([nombre for nombre in nombres if "centro cultural" in nombre.lower()])
``` 

> :first_place: ¡Ahora te toca a vos! Construí una tabla `proporcion_cines_comeriales_provinciales` que contenga, para cada provincia, la proporción entre 0 y 1 de cines de gestión `"Privado comercial"`, ordenada según esta proporción de menor a mayor. 
