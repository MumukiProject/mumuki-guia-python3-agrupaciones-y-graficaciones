En ocasiones, de todas formas, podemos evitar este tipo de problemas si el dataset original tiene algún tipo de código único para cada elemento sobre el que queremos agrupar. Por ejemplo, en este dataset contamos con la columna `loc_code` que nos da, en teoría, un identificador numérico único para cada localidad. Por eso, también hubiera tenido sentido construir a `butacas_por_localidad` así: 

```python
ム cines.groupby("loc_code", as_index=False)["seats"].sum()
```

||loc_code|seats|
|---|---|---|
|0|2000010|31386|
|1|6014010|250|
|2|6028010|3215|
|3|6035010|4805|
|4|6042010|385|
|...|...|...|

O si queremos además preservar el nombre de la localidad: 

```python
ム  cines.groupby(["loc_code", "city"], as_index=False)["seats"].sum()
```

||loc_code|city|seats|
|---|---|---|---|
|0|2000010|Ciudad Autónoma de Buenos Aires|31386|
|1|6014010|Gonzales Chaves|250|
|2|6028010|Adrogué|3215|
|3|6035010|Avellaneda|4805|
|4|6042010|Ayacucho|385|
|...|...|...|...|


