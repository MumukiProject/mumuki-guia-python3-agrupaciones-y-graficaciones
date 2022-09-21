¿Y cómo hacemos para crear agrupaciones con `pandas`? Para ello contamos con `groupby` (literalmente, _agrupar según_ en inglés), una operación de `DataFrame`s que se usa así:

```
<tabla>.groupby(<columna_segun_la_que_agrupar>)[<columna_a_agregar>].<agregacion>()
```

Por ejemplo, si tuviéramos nuestra hipotética tabla de multas y quisiéramos _agrupar según patentes y calcular la sumatoria de infracciones_, lo escribiríamos así:    

```python
ム multas.groupby("patente")["infraccion"].sum()
patente
ab16    500
hz15    100
mm12    150
xy40    350
Name: infraccion, dtype: int64
```

De igual forma, así se verían las otras agregaciones que mencionamos:

```python
ム multas.groupby("patente")["infraccion"].mean()
patente
ab16    166.666667
hz15    100.000000
mm12    150.000000
xy40    175.000000
Name: infraccion, dtype: float64
ム multas.groupby("patente")["infraccion"].median()
patente
ab16    200.0
hz15    100.0
mm12    150.0
xy40    175.0
Name: infraccion, dtype: float64
ム multas.groupby("patente")["infraccion"].count()
patente
ab16    3
hz15    1
mm12    1
xy40    2
Name: infraccion, dtype: int64
```


> 🔙  Hagamos un `flashback` y volvamos a nuestros cines. Escribí en la consola la expresión que permite calcular la sumatoria de pantallas por tipo de gestión. Ya dejamos cargado el `DataFrame` `cines`. 
