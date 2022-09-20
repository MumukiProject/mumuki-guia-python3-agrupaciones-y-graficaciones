Con `pandas` podemos realizar distintos tipos de gráficos con pocas líneas de código. En el ejemplo anterior...

```python
empleo.plot.line(x="anio")
```

....vemos como tomando datos de nuestra tabla `empleo`, realizamos un gráfico de líneas en el que nuestro eje x (también llamado abscisas o eje horizontal) es el `anio`.  Además, implícitamente nuestro eje y (ordenadas, o eje vertical) incluye como _series_ a las demás columnas numéricas, en nuestro caso la `tasa_empleo_mujer` y `tasa_empleo_varon`. Lo mismo lo podemos decir de forma más explícita así:

```python
empleo.plot.line(x="anio", y = ["tasa_empleo_mujer", "tasa_empleo_varon"])
```

> Pero `pandas` no sólo nos permite hacer gráficos de líneas. Probá cambiar en tu cuaderno Colab los ejemplos anteriores `plot.line` por `plot.bar` y ejecutalos nuevamente. ¿Qué sucede?
>
