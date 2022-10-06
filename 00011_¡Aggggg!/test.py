class Test(unittest.TestCase):

  def test_proporcion_cines_comeriales_provinciales_es_un_DataFrame(self):
    self.assertEquals(type(proporcion_cines_comeriales_provinciales), pd.DataFrame)
    
  def test_genera_el_DataFrame_correcto(self):
    indexados = proporcion_cines_comeriales_provinciales.set_index("province")
    self.assertTrue(len(proporcion_cines_comeriales_provinciales) == 5, "debe tener el tamaño correcto")    
    self.assertTrue(indexados.loc["San Juan", "sector"] == 1, "debe tener el valor correcto para San Juan")
    self.assertTrue(indexados.loc["Buenos Aires", "sector"] == 0.8, "debe tener el valor correcto para Buenos Aires")
    self.assertTrue(indexados.loc["Santa Fe", "sector"] == 1, "debe tener el valor correcto para Santa Fe")
    
  def test_genera_las_columnas_correctas(self):  
    self.assertEquals(list(proporcion_cines_comeriales_provinciales.columns), ['province', 'sector'])    