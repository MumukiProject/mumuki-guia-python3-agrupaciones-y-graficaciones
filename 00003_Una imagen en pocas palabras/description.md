Con `pandas` podemos realizar distintos tipos de gráficos con pocas líneas de código. En el ejemplo anterior...

```python
empleo.plot.line(x="year")
```

....vemos como tomando datos de nuestra tabla `empleo`, realizamos un gráfico de líneas en el que nuestro eje x (también llamado _abscisas_ o _eje horizontal_) es el `year`.  Además, implícitamente nuestro eje y (ordenadas, o eje vertical) incluye como _series_ a las demás columnas numéricas, en nuestro caso la `employment_rate_female` y `employment_rate_male`. Lo mismo lo podemos decir de forma más explícita así:

```python
empleo.plot.line(x="year", y = ["employment_rate_female", "employment_rate_male"])
```

> Pero `pandas` no sólo nos permite hacer gráficos de líneas. Probá cambiar en tu cuaderno Colab los ejemplos anteriores `plot.line` por `plot.bar` y ejecutalos nuevamente. ¿Qué sucede?
