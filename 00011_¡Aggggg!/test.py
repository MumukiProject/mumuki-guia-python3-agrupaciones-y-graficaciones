class Test(unittest.TestCase):

  def test_medianas_por_provincia_es_un_DataFrame(self):
    self.assertEquals(type(medianas_por_provincia), pd.DataFrame)
    
  def test_genera_el_DataFrame_correcto(self):
    indexados = medianas_por_provincia.set_index("province")
    self.assertTrue(len(medianas_por_provincia) == 5, "debe tener el tamaño correcto")    
    self.assertTrue(indexados.loc["San Juan", "screens"] == 6, "debe tener el valor correcto de pantallas para San Juan")
    self.assertTrue(indexados.loc["Buenos Aires", "seats"] == 750, "debe tener el valor correcto de butacas para Buenos Aires")
    self.assertTrue(indexados.loc["Santa Fe", "seats"] == 584, "debe tener el valor correcto de butacas para Santa Fe")
    
  def test_genera_las_columnas_correctas(self):  
    self.assertEquals(set(medianas_por_provincia.columns), {'province', 'screens', 'seats'})   
    

  def test_esta_ordenado_de_la_a_a_la_z(self):  
    self.assertTrue(medianas_por_provincia["province"].iloc[0] == "Buenos Aires", "el primer elemento debe ser Buenos Aires") 
    self.assertTrue(medianas_por_provincia["province"].iloc[1] == "Ciudad Autónoma de Buenos Aires", "Ciudad Autónoma de Buenos Aires debe estar después de Buenos Aires")
    self.assertTrue(medianas_por_provincia["province"].iloc[2] == "Salta", "Salta debe estar después de Ciudad Autónoma de Buenos Aires")
    self.assertTrue(medianas_por_provincia["province"].iloc[4] == "Santa Fe", "Santa Fe debe estar después de Ciudad Autónoma de Salta")
  
      
    
    