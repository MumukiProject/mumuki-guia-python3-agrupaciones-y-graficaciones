Lamentablemente, los departamentos y localidades de un país difícilmente son únicas :facepalm:, Por ejemplo, en este dataset hay 11 departamentos llamados   `"Capital"`.

||loc_code|category|province|department|city|name|
|---|---|---|---|---|---|---|
|0|10049030|Salas de cine|Catamarca|Capital|Catamarca|Cinemacenter
|(..)|
|14|42021020|Salas de cine|La Pampa|Capital|Santa Rosa|Milenium
|(..)|
|18|54028030|Salas de cine|Misiones|Capital|Posadas|Del Conocimiento
|(..)|
|20|66028050|Salas de cine|Salta|Capital|Salta|El Teatrino
|(..)|


Cuando suceden estas situaciones, no podremos agrupar despreocupadamente según una sola columna, porque terminaremos mezclando datos accidentalmente 🙅. Por ejemplo, en esta situación, habríamos sumado las butacas de departamentos que se llaman igual pero nada tienen que ver entre sí :crazy_face:.

En su lugar, construiremos nuestros grupos teniendo en cuenta a todas las columnas que sean necesarias para evitar estas ambigüedades, de la siguiente forma:

```python
ム cines.groupby(["province", "department"], as_index=False)["seats"].sum()
```
||province |department |seats|
|---|---|---|---|
|0 |Buenos Aires |9 de julio |90
|1 |Buenos Aires |Adolfo Gonzales Chaves |250
|2 |Buenos Aires |Almirante Brown |3215
|3 |Buenos Aires |Avellaneda |4805
|4 |Buenos Aires |Ayacucho |385
|... |... |... |...
|148 |Tierra del Fuego |Rio Grande |584
|149 |Tierra del Fuego |Ushuaia |861
|150 |Tucumán |Capital |2286
|151 |Tucumán |Tafi Viejo |830
|152 |Tucumán |Yerba Buena |2045
 
Como vemos, cuando en lugar de especificar un nombre de columnas, pasamos como parámetro una lista de nombres, los datos se agrupan según todas ellas y el resultado es una tabla con más de dos columnas.
 
> ¡Este no es el único problema! En este dataset encontraremos que hay dos ciudades llamadas `"Colón"`, una en Buenos Aires y otra en Entre Ríos:
>
> ||loc_code|category|province|department|city|name|
> |---|---|---|---|---|---|---|
> |(...)|
> |9|30008020|Salas de cine|Entre Ríos|Colon|Colón|Starlight
> |(...)|
> |293|6175010|Salas de cine|Buenos Aires|Colon|Colón|Cine Teatro Colon
>
> :seat: Teniendo esto en cuenta, creá un nuevo `DataFrame` que tenga las butacas totales por localidad (`city`), y guardarlo en una variable `butacas_por_localidad`. 


<style>

blockquote .table {
  background: white;
  border-radius: 5px;
  margin: 9px 0;
}

</style>