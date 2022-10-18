¿Y qué hubiera pasado si necesitáramos la cantidad total de butacas por departamento? ¿Y por localidad (es decir, ciudad o pueblo)?  ¿Podríamos hacer algo como esto?

```python
# ¿total de butacas por departamento?
cines.groupby("department", as_index=False)["seats"].sum()
# ¿total de butacas por localidad?
cines.groupby("city", as_index=False)["seats"].sum()
```

:timer: Tomate un momento para reflexionar sobre ésto y nos vemos en el siguiente ejercicio. 
