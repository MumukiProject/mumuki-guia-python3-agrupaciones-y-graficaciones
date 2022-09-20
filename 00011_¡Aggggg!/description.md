No, ¡nos estamos quejando! Sólo queríamos mostrarte otra operación útiles a la hora de hacer agregaciones: `agg` 😅. 

```python
cines.groupby("Provincia", as_index=False).agg({
   "Pantallas": "sum",
   "Butacas": "mean"
})
```
 
A diferencia de las agregaciones anteriores, como `sum` y `max`, `agg` nos permite realizar varias al mismo tiempo y obtener tablas con múltiples resultados: 

||Provincia|Pantallas|Butacas|
|---|---|---|---|
|0|Buenos Aires|358|878.415094|
|1|Catamarca|12|800.000000|
|2|Chaco|14|617.250000|
|3|Chubut|10|298.000000|
|4|Ciudad Autónoma de Buenos Aires|153|896.742857|
|5|Corrientes|17|421.250000|
|(...)|


Con `agg` se vuelve sencillo adicionar agregaciones a nuestras tablas, tan sólo agregando una clave (la columna a agregar) y un valor (la operación a realizar) al diccionario que recibe por parámetro. Por ejemplo, así podemos incluir también la cantidad de cines en la tabla anterior: 

```python
cines.groupby("Provincia", as_index=False).agg({
   "Nombre": "count",
   "Pantallas": "sum",
   "Butacas": "mean"
})
# si te molesta que la columna se llame nombre, ya lo veremos más adelante...
```

||Provincia|Nombre|Pantallas|Butacas|
|---|---|---|---|---|
|0|Buenos Aires|106|358|878.415094|
|1|Catamarca|4|12|800.000000|
|2|Chaco|4|14|617.250000|
|3|Chubut|9|10|298.000000|
|4|Ciudad Autónoma de Buenos Aires|35|153|896.742857|
|5|Corrientes|8|17|421.250000|
|(...)|

 
¡Pero eso no es todo! `agg` permite además usar agregaciones personalizadas, tan solo pasando una función como valor. Por ejemplo, si queremos contar la cantidad de cines que tiene la frase "Centro cultural" en su nombre, podríamos escribir algo así….
 
```python
cines.groupby("Provincia", as_index=False).agg({
   "Nombre": contar_centros_culturales
})
```

||Provincia|Nombre|
|---|---|---|
|0|Buenos Aires|5|
|1|Catamarca|1|
|2|Chaco|0|
|3|Chubut|1|
|4|Ciudad Autónoma de Buenos Aires|3|
|5|Corrientes|0|
|(...)|
 
... donde en lugar de pasar un string con el nombre de una agregación (como "sum" o "count"), pasamos la referencia a una función. Estas funciones que agg reciben deben tomar una lista con los valores de las filas de cada grupo: 

```python
def contar_centros_culturales(nombres):
 return len([nombre for nombre in nombres if "centro cultural" in nombre.lower()])
``` 

> Ahora te toca a vos. Construí una tabla `proporcion_cines_comeriales_provinciales` que contenga, para cada provincia, la proporción entre 0 y 1 de cines de gestión "Privado comercial", ordenada según esta proporción de mayor a menor. 
