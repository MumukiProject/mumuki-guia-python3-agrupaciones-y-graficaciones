No, ¡nos estamos quejando! Sólo queríamos mostrarte otra operación útiles a la hora de hacer agregaciones: `agg` 😅. 

```python
cines.groupby("Provincia", as_index=False).agg({
   "Pantallas": "sum",
   "Butacas": "mean"
})
```
 
A diferencia de las agregaciones anteriores, como `sum` y `max`, `agg` nos permite realizar varias al mismo tiempo y obtener tablas con múltiples resultados: 

…

Con `agg` se vuelve sencillo adicionar agregaciones a nuestras tablas, tan sólo agregando una clave (la columna a agregar) y un valor (la operación a realizar) al diccionario que recibe por parámetro. Por ejemplo, así podemos incluir también la cantidad de cines en la tabla anterior: 

```python
cines.groupby("Provincia", as_index=False).agg({
   "Nombre": "count",
   "Pantallas": "sum",
   "Butacas": "mean"
})
# si te molesta que la columna se llame nombre, ya lo veremos más adelante...
```
 
¡Pero eso no es todo! `agg` permite además usar agregaciones personalizadas, tan solo pasando una función como valor. Por ejemplo, si queremos contar la cantidad de cines que tiene la frase "Centro cultural" en su nombre, podríamos escribir algo así….
 
```python
 cines.groupby("Provincia", as_index=False).agg({
   "Nombre": contar_centros_culturales
})
```
 
… donde en lugar de pasar un string con el nombre de una agregación (como "sum" o "count"), pasamos la referencia a una función. Estas funciones que agg reciben deben tomar una lista con los valores de las filas de cada grupo: 

```python
def contar_centros_culturales(nombres):
 return len([nombre for nombre in nombres if "centro cultural" in nombre.lower()])
``` 

> Ahora te toca a vos. Construí una tabla `proporcion_cines_comeriales_provinciales` que contenga, para cada provincia, la proporción entre 0 y 1 de cines de gestión "Privado comercial", ordenada según esta proporción de mayor a menor. 
