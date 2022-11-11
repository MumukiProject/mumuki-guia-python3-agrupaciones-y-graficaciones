🤬 No, ¡no nos estamos quejando! Sólo queríamos mostrarte otra operación útil a la hora de hacer agregaciones: `agg` 😅. 

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
# si te molesta que la columna se llame name, ya lo veremos más adelante...
```
 
> TODO: agrupar por por provincia y sector y ordenar

