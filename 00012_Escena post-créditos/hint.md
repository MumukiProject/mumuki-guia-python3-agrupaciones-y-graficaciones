:sos: ¿Generar un CSV? ¿Cómo hacemos eso? ¡Ayuda, `pandas`!

:arrows_counterclockwise:  Es posible convertir `DataFrames` y `Series` en CSVs usando `to_csv`, de la siguiente forma:

```python
una_columna_o_tabla.to_csv()
```

Esto nos generará un string con el contenido del CSV, que para mayor claridad podemos imprimir usando `print`:

```python
print(una_columna_o_tabla.to_csv())
```

⚠️ Eso sí, hay que tener cuidado con el índice, porque por defecto `to_csv` nos agregará una columna con sus valores, que dependiendo el caso nos puede ser útil o no. Por ejemplo, si cuando hacemos agrupaciones no especificamos `as_index=False`, todo funcionará sin mayores complicaciones...

```python
ム print(cines.groupby("province")["seats"].sum().to_csv())
province,seats
Buenos Aires,93112
Catamarca,3200
Chaco,2469
Chubut,2682
Ciudad Autónoma de Buenos Aires,31386
Corrientes,3370
Córdoba,20799
...
```

... pero si en cambio usamos `as_index=False`, la columna de índice incluida en el CSV será redundante: 

```python
ム print(cines.groupby("province", as_index=False)["seats"].sum().to_csv()) 
,province,seats # notá que ahora hay una columna más, sin nombre
0,Buenos Aires,93112
1,Catamarca,3200
2,Chaco,2469
3,Chubut,2682
4,Ciudad Autónoma de Buenos Aires,31386
5,Corrientes,3370
6,Córdoba,20799
...
```

Por ello, nos convendrá explícitamente excluir el índice, usando `index=False`: 

```python
ム print(cines.groupby("province", as_index=False)["seats"].sum().to_csv(index=False))
province,seats
Buenos Aires,93112
Catamarca,3200
Chaco,2469
Chubut,2682
Ciudad Autónoma de Buenos Aires,31386
Corrientes,3370
Córdoba,20799
...
```

