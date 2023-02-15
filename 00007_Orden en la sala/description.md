Como habrás notado, al agrupar obtenemos un `Series` con los valores agregados, pero desordenados (1, 879, 4, etc). En su lugar, `groupby` ordena las columnas según los valores de los grupos (en caso, lexicográficamente: `Otro`, `Privado comercial`, `Privado comunitario`, etc):

```python
ム cines.groupby("sector")["screens"].sum()
sector
Otros                      1
Privado comercial        879
Privado comunitario        4
Privado independiente      8
(...etc...)
```

Afortunadamente, al igual que los `DataFrame`s, los `Series` pueden ser ordenados usando `sort_values`:

```python
ムcines.groupby("sector")["screens"].sum().sort_values()
sector
Otros                      1
Privado comunitario        4
Privado independiente      8
Público provincial        11
Público nacional          14
Público municipal         57
Privado comercial        879
Name: screens, dtype: int64
```

:eyes: Notá que aunque `sort_values` devuelve un `DataFrame` al aplicarlo a un `DataFrame`,  si se aplica sobre un `Series`, devuelve… ¡otro `Series`! Además, a diferencia de cuando ordenamos un `DataFrame`, en este caso no deberemos especificar el nombre de la columna que vamos a ordenar. Al fin y al cabo, ¡ahora estamos trabajando con una sola columna! 😛

> ¡Ahora te toca a vos! Necesitamos un informe con las **tres** provincias con mayor promedio de butacas, que se vea aproximadamente así: 
> 
> ```python
> province
> Santa Fe         590.0
> Rosario         1000.0
> San Juan        1050.0
> ```
>
> :warning: _(los valores del ejemplo no son necesariamente correctos)_
>
> Calculá este informe usando lo visto hasta acá y asignalo a `provincias_con_cines_grandes`.
> 
