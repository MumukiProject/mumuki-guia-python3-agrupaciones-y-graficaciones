¿Y qué hubiera pasado si necesitáramos la cantidad total de butacas por departamento? ¿Y por localidad (es decir, ciudad o pueblo)?  ¿Podríamos hacer algo como esto?

```python
# ¿total de butacas por departamento?
cines.groupby("Departamento", as_index=False)["Butacas"].sum()
# ¿total de butacas por localidad?
cines.groupby("Localidad", as_index=False)["Butacas"].sum()
```

:timer: Tomate un momento para reflexionar sobre ésto y nos vemos en el siguiente ejercicio. 
