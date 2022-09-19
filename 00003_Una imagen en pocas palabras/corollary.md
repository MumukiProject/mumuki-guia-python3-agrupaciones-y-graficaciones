Como vemos, ahora tenemos un gráfico de barras, en el que la información se muestra de forma _discreta_, es decir, dando saltos año a año en lugar de unirlas mediante líneas _continuas_.

Por otro lado, los datos no siempre estarán discriminados en múltiples series. Por ejemplo, si contáramos con únicamente una tabla con la información de empleo total, podríamos especificar una única serie en el eje y: 

```
empleo_total.head(5)
```

```
empleo_total.plot.line(x="anio", y="tasa_empleo")
```
