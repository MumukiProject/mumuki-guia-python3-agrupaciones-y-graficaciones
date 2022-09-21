Como vemos, ahora tenemos un gráfico de barras, en el que la información se muestra de forma _discreta_, es decir, dando saltos año a año en lugar de unirlas mediante líneas _continuas_.

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-agrupaciones-y-graficaciones/master/assets/employment_gender_plot_bar_1663775871814.png" alt="employment_gender_plot_bar_1663775871814.png" width="auto" height="auto">


Por otro lado, los datos no siempre estarán discriminados en múltiples series. Por ejemplo, si contáramos con únicamente una tabla con la información de empleo total, podríamos especificar una única serie en el eje y: 

```
empleo_total.head(5)
```


```
empleo_total.plot.line(x="year", y="employment_rate")
```




