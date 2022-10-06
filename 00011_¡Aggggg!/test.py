class Test(unittest.TestCase):

  def test_proporcion_cines_comeriales_provinciales_es_un_DataFrame(self):
    self.assertEquals(type(proporcion_cines_comeriales_provinciales), pd.DataFrame)
    
  def test_genera_el_DataFrame_correcto(self):
    indexados = proporcion_cines_comeriales_provinciales.set_index("province")
    self.assertTrue(len(proporcion_cines_comeriales_provinciales) == 4, "debe tener el tamaño correcto")    
    
  def test_genera_las_columnas_correctas(self):  
    self.assertEquals(list(butacas_por_localidad.columns), ['province', 'sector'])    