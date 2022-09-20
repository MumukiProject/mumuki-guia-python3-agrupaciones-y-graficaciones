Como habrás notado, al agrupar obtenemos un `Series` con los valores agregados, pero desordenados (1, 879, 4, etc). En su lugar, `groupby` ordena las columnas según los valores de los grupos (`Otro`, `Privado comercial`, `Privado comunitario`, etc):

```python
ム  cines.groupby("tipo_gestion")["Pantallas"].sum()
tipo_gestion
Otros                      1
Privado comercial        879
Privado comunitario        4
Privado independiente      8
(...etc...)
```

Afortunadamente, al igual que los `DataFrame`s, los `Series` pueden ser ordenados  ordenarla usando `sort_values`:

```python
ム cines.groupby("tipo_gestion")["Pantallas"].sum().sort_values()
tipo_gestion
Otros                      1
Privado comunitario        4
Privado independiente      8
Público provincial        11
Público nacional          14
Público municipal         57
Privado comercial        879
Name: Pantallas, dtype: int64
```

:eyes: Notá que aunque `sort_values` devuelve un `DataFrame` al aplicarlo a un `DataFrame`,  si se aplica sobre un `Series`, devuelve… ¡otro `Series`!


> Ahora te toca a vos. Escribí una expresión que devuelva las tres provincias con mayor promedio de butacas.
