¡Pero aún hay más! :smile: También es posible hacer gráficos sobre `Series`, usando, nuevamente, `.plot`. Y como los resultados del groupby son `Series`... podemos hacer hacer cosas como ésta:

```python
# barh es una variación de del gráfico de barras que ya vimos,
# que presenta disposición horizontal
ム cines.groupby("tipo_gestion")["Pantallas"].sum().plot.barh()

```

> Cargá en un nuevo cuaderno el `DataFrame` de cines con el que venimos trabajando desde https://... y probá los siguientes gráficos:
>
> `cines.groupby("tipo_gestion")["Pantallas"].sum().plot.pie()`
> `cines.groupby("tipo_gestion")["Pantallas"].sum().plot.sort_values().pie()`
> `cines.groupby("tipo_gestion")["Butacas"].sum().plot.sort_values().pie()`
> `cines.value_counts("tipo_gestion").plot.sort_values().pie()`
>
> ¿Qué conclusiones podés sacar?
>

