Lamentablemente, no siempre contaremos con información en el preciso formato en el que la necesitamos 🤷. Ya sea para comprenderla mejor en tablas o gráficamente, en general terminaremos tomando un lote de datos que _más o menos_ se ajuste a lo que estamos buscando, y luego lo adaptaremos a nuestras necesidades.

Por ejemplo, si estamos estudiando la distribución el tipo de gestión (pública o privada) de los cines de Argentina, probablemente no encontraremos un lote de datos que contenga exactamente esa información, sino más bien algo como ésto:

```python
cines = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTRxjjNANJbRCSqlQxwz4ojLXPaobB5ls9f9CVR-JYzY451LucsDBAFK9RYRim74Ykg3X7_sc-GHVv3/pub?gid=969960562&single=true&output=csv")
cines.head(5)
```


Pero, ¿cómo sería nuestra tabla ideal? 🤔 Debería tener dos columnas...
 
 * el tipo de gestión: una columna categórica (pública provincial, pública municipal, privada comercial,  etc)
 * la cantidad de pantallas de pantallas de cine de cada gestión: una columna numérica que, por cada fila
 
... y verse aproximadamente así:

||tipo_gestion|Pantallas|
|---|---|---|
|0|Privado comercial|879|
|1|Público municipal|57|
|2|Público nacional|14|
|3|Público provincial|11|
|4|Privado independiente|8|
|5|Privado comunitario|4|
|6|Otros|1|

> ¿Es posible construir esta tabla usando únicamente lo que vimos hasta ahora?

