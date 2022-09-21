👀 Si miraste con detenimiento la tabla anterior….

|year|employment_rate_female|employment_rate_male|
|---|---|---|
|2003|45.800.000|64.600.000|
|2004|48.700.000|66.600.000|
|2005|50.500.000|67.500.000|
|2006|49.700.000|68.900.000|
|2007|50.700.000|69.100.000|
|2008|51.191.836|68.559.467|
|2009|51.367.572|67.717.618|
|2010|51.215.647|67.620.266|
|2011|50.559.132|66.769.163|
|(...)|

….posiblemente hayas reconocido que los datos del lote representan una estadística de porcentajes de empleo anuales . Quizás hayas notado que en esta estadística, los mismos están en torno a los 50 o 60 puntos.

Los datos, además, están discriminados por género, es decir, que en lugar de mostrarnos el nivel de empleo total, lo hacen diferenciando entre hombres y mujeres. ¿Notaste también alguna relación, año a año, entre estos dos valores?

> :mag: ¡Analicemos los datos! Escribí el siguiente código en tu cuaderno y respondé cuáles afirmaciones son verdaderas:
>
> ```python
> empleo.plot.line(x="anio")
> ```
>
