Como vemos, ahora tenemos un gráfico de barras, en el que la información se muestra de forma _discreta_, es decir, dando saltos año a año en lugar de unirlas mediante líneas _continuas_.

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-agrupaciones-y-graficaciones/master/assets/employment_gender_plot_bar_1663775871814.png" alt="employment_gender_plot_bar_1663775871814.png" width="auto" height="auto">

Por otro lado, los datos no siempre estarán discriminados en múltiples series. Por ejemplo, si contáramos con únicamente una tabla con la información de empleo total... 

```python
empleo_total = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=1194930839&single=true&output=csv")
empleo_total.head(5)
```

...podríamos especificar una única serie en el eje y: 

||year|employment_rate|
|---|---|---|
|0|2003|54.3|
|1|2004|56.7|
|2|2005|58.3|
|3|2006|58.4|
|4|2007|59.1|
|(...)|


```python
empleo_total.plot.line(x="year", y="employment_rate")
```
<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-agrupaciones-y-graficaciones/master/assets/employment_rate_plot_line_1663776537522.png" alt="employment_rate_plot_line_1663776537522.png" width="auto" height="auto">
