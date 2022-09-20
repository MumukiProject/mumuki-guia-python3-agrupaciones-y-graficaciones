Para graficar, definitivamente es muy conveniente que `groupby` devuelva un `Series`, pero a veces nos será más práctico obtener los resultados en forma de un `DataFrame` de dos columnas. 

De hecho, cuando empezamos a analizar nuestros datos de cines, comentamos que nuestra _tabla_ ideal se vería así: 

||tipo_gestion|Pantallas|
|---|---|---|
|0|Privado comercial|879|
|1|Público municipal|57|
|2|Público nacional|14|
|3|Público provincial|11|
|4|Privado independiente|8|
|5|Privado comunitario|4|
|6|Otros|1|
 
📰 La buena noticia es que es que esto es fácil de lograr, tan sólo agregando el parámetro `as_index=False` a `groupby`:

```python
ム cines.groupby("tipo_gestion", as_index=False).Pantallas.sum()
```

¡Y listo :tada:! Ahora tendremos a disposición todas las operaciones que vimos (y que veremos más adelante). 

> 🛑 ¡Alto! Veamos si se entendió: usando lo que acabamos de aprender, generá una tabla que contenga la cantidad total de butacas en cada provincia, y guardala en la variable `butacas_por_provincia`
