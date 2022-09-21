👀 Si miraste con detenimiento la tabla anterior….

|year|employment_rate_female|employment_rate_male|
|---|---|---|
|2003|45.80|64.60|
|2004|48.70|66.60|
|2005|50.50|67.50|
|2006|49.70|68.90|
|2007|50.70|69.10|
|2008|51.19|68.56|
|2009|51.37|67.72|
|2010|51.22|67.62|
|2011|50.56|66.77|
|(...)|

….posiblemente hayas reconocido que los datos del lote representan una estadística de porcentajes de empleo anuales . Quizás hayas notado que en esta estadística, los mismos están en torno a los 50 o 60 puntos.

Los datos, además, están discriminados por género, es decir, que en lugar de mostrarnos el nivel de empleo total, lo hacen diferenciando entre hombres y mujeres. ¿Notaste también alguna relación, año a año, entre estos dos valores?

> :mag: ¡Analicemos los datos! Escribí el siguiente código en tu cuaderno y respondé cuáles afirmaciones son verdaderas:
>
> ```python
> empleo.plot.line(x="year")
> ```
>
