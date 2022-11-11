class Test(unittest.TestCase):

  def test_pantallas_por_sector_es_un_DataFrame(self):
    self.assertEquals(type(butacas_por_localidad), pd.DataFrame)
    
  def test_genera_el_DataFrame_correcto(self):
    indexadas = butacas_por_localidad.set_index("city")
    self.assertTrue(len(butacas_por_localidad) == 2, "debe tener el tamaño correcto")
    self.assertTrue(indexadas.loc["Bragado", "seats"] == 750, "Tiene la cantidad correcta de Bragado")
    self.assertTrue(indexadas.loc["Salta", "seats"] == 354, "Tiene la cantidad correcta de Salta")
    self.assertTrue(indexadas.loc["Pilar", "seats"] == 1407, "Tiene la cantidad correcta de Pilar")

  def test_tiene_dos_localidades_colon(self):
    assert len(butacas_por_localidad[butacas_por_localidad["city"]== "Colón"]) == 2, "debería tener dos localidades (city) Colón"
  
  def test_genera_las_columnas_correctas(self):  
    self.assertEquals(set(butacas_por_localidad.columns), {'province', 'department', 'city', 'seats'})